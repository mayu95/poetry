import torch
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence


class RNN(nn.Module):

    def __init__(self, vocab_size, embed_size, num_output, rnn_model='LSTM', use_last=False, embedding_tensor=None,
                 padding_index=0, hidden_size=64, num_layers=1, batch_first=True,
                 encoder_model="rnn", dropout_p=0, bidirectional=True, cnn_config=None):
        """

        Args:
            vocab_size: vocab size
            embed_size: embedding size
            num_output: number of output (classes)
            rnn_model:  LSTM or GRU
            use_last:  bool
            embedding_tensor:
            padding_index:
            hidden_size: hidden size of rnn module
            num_layers:  number of layers in rnn module
            batch_first: batch first option
        """

        super(RNN, self).__init__()
        self.use_last = use_last
        self.encoder_model = encoder_model
        self.hidden_size = hidden_size
        self.bidirectional = bidirectional
        self.config = cnn_config
        # embedding
        self.encoder = None
        if torch.is_tensor(embedding_tensor):
            self.encoder = nn.Embedding(vocab_size, embed_size, padding_idx=padding_index, _weight=embedding_tensor)
            self.encoder.weight.requires_grad = False
        else:
            self.encoder = nn.Embedding(vocab_size, embed_size, padding_idx=padding_index)

        #  self.drop_en = nn.Dropout(p=0.6)
        self.dropout_p = dropout_p
        self.drop_en = nn.Dropout(self.dropout_p)

        self.hi = nn.Linear(self.hidden_size*2, self.hidden_size*2, bias=False) 
        self.attn_weights = nn.Linear(self.hidden_size*2, 1, bias=False) 
        self.energy = nn.Linear(1, 1, bias=False)
        

        # rnn module
        if rnn_model == 'LSTM':
            self.rnn = nn.LSTM(
                input_size=embed_size,
                hidden_size=hidden_size,
                num_layers=num_layers,
                dropout=self.dropout_p,
                batch_first=True,
                bidirectional=self.bidirectional
            )
        elif rnn_model == 'GRU':
            self.rnn = nn.GRU(
                input_size=embed_size,
                hidden_size=hidden_size,
                num_layers=num_layers,
                dropout=self.dropout_p,
                batch_first=True,
                bidirectional=self.bidirectional
            )
        else:
            raise LookupError(' only support LSTM and GRU')


        if self.bidirectional:
            out_hidden_size = hidden_size * 2
        else:
            out_hidden_size = hidden_size
        if self.encoder_model == "avg":
            out_hidden_size = embed_size

        if self.encoder_model == "cnn":
            self.char_conv = nn.ModuleList([nn.Conv2d(
                    self.config.char_dim_cnn, self.config.char_conv_fn[i],
                    (self.config.char_conv_fh[i], self.config.char_conv_fw[i]),
                    stride=1) for i in range(len(self.config.char_conv_fn))])
            out_hidden_size = sum(self.config.char_conv_fn) 

        #  self.bn2 = nn.BatchNorm1d(out_hidden_size)
        self.fc = nn.Linear(out_hidden_size, num_output)

    def forward_cnn(self, x, seq_lengths):
        # inputs shape: ([20, 35, 21]) batch, bptt, max_wordlen
        #  embeds shape: ([700, 21, 15])
        embeds = self.encoder(x)
        # unsqueeze shape: [700, 21, 1, 15]
        # transpose shape: ([700, 15, 1, 21])
        embeds = torch.transpose(torch.unsqueeze(embeds, 2), 1, 3).contiguous()
        conv_result = []
        for i, conv in enumerate(self.char_conv):
            # Note some error may happen where some batch are very short when meeting a large filter
            # conv(embeds) shape: ([700, 25, 1, 21])
            char_conv = torch.squeeze(conv(embeds))
            # after squeeze shape: [700, 25, 21])
            #  torch.max out: (max, max_indices)
            char_mp = torch.max(torch.tanh(char_conv), 2)[0]
            conv_result.append(char_mp)
            #  char_mp = char_mp.view(-1, x.size(1), char_mp.size(1))
            # char_mp shape: ([20, 35, 25])
        conv_result = torch.cat(conv_result, 1)
        # conv_result shape: ([20, 35, 525])
        out = self.fc(conv_result)
        return out


    def forward_avg(self, x, seq_lengths):
        '''
        Args:
            x: (batch, time_step, input_size)
        Returns:
            num_output size
        '''

        x_embed = self.encoder(x)
        # shape: batch_size, seq_len, embed_size
        x_embed = self.drop_en(x_embed)
        output = x_embed.sum(dim=1)
        output = output / seq_lengths.type(output.dtype).unsqueeze(1).expand(output.shape)
        #  fc_input = self.bn2(output)
        # shape: (batch_size, label_num)
        out = self.fc(output)
        return out

    def forward(self, x, seq_lengths):
        if self.encoder_model == "avg":
            return self.forward_avg(x, seq_lengths)
        if self.encoder_model == "rnn":
            #  return self.forward_rnn(x, seq_lengths)
            return self.forward_rnn_attn(x, seq_lengths)
        if self.encoder_model == "cnn":
            return self.forward_cnn(x, seq_lengths)


    def forward_rnn(self, x, seq_lengths):
        '''
        Args:
            x: (batch, time_step, input_size)
        Returns:
            num_output size
        '''

        x_embed = self.encoder(x)
        x_embed = self.drop_en(x_embed)


        packed_input = pack_padded_sequence(x_embed, seq_lengths.cpu().numpy(),batch_first=True)

        # out_rnn shape (batch, seq_len, hidden_size * num_directions)
        # None is for initial hidden state
        packed_output, ht = self.rnn(packed_input, None)
        out_rnn, _ = pad_packed_sequence(packed_output, batch_first=True)

        row_indices = torch.arange(0, x.size(0)).long()
        col_indices = seq_lengths - 1
        if next(self.parameters()).is_cuda:
            row_indices = row_indices.cuda()
            col_indices = col_indices.cuda()

        if self.bidirectional:
            if self.use_last:
                last_tensor=out_rnn[row_indices, col_indices, :]
            else:
                # use mean
                batch_size, seq_len, out_size = out_rnn.shape  # out_rnn.shape = ([128, 42 , 400])
                # forward + backward
                bilstm_out = out_rnn.view(batch_size, seq_len, 2, self.hidden_size)
                #  bilstm_out = ([128, 42, 2, 200])
                bilstm_out = bilstm_out[:, :, 0, :] + bilstm_out[:, :, 1, :]
                #  bilstm_out = ([128, 76, 200])
                # batch_size, hidden_size
                bilstm_out = torch.sum(bilstm_out, dim=1)
                #  bilstm_out = ([128, 200])
                last_tensor = bilstm_out / seq_lengths.type(bilstm_out.dtype).unsqueeze(1).expand(bilstm_out.shape)
                #  last_tensor = out_rnn[row_indices, :, :]
                #  last_tensor = torch.mean(last_tensor, dim=1)
        else:
            out_rnn = out_rnn.sum(dim=1)
            last_tensor = out_rnn / seq_lengths.type(out_rnn.dtype).unsqueeze(1).expand(out_rnn.shape)

        #  fc_input = self.bn2(last_tensor)
        # shape: (batch_size, label_num)
        out = self.fc(last_tensor)
        return out



    def forward_rnn_attn(self, x, seq_lengths):
        x_embed = self.encoder(x)
        x_embed = self.drop_en(x_embed)

        packed_input = pack_padded_sequence(x_embed, seq_lengths.cpu().numpy(),batch_first=True)

        # out_rnn shape (batch, seq_len, hidden_size * num_directions)
        # None is for initial hidden state
        packed_output, ht = self.rnn(packed_input, None)
        out_rnn, _ = pad_packed_sequence(packed_output, batch_first=True)

        if self.bidirectional:

            batch_size, seq_len, out_size = out_rnn.shape  # out_rnn.shape = ([128, 42 , 400])
            #  bilstm_out = out_rnn[:, :, :self.hidden_size] + out_rnn[:, :, self.hidden_size:]
            # batch_size, hidden_size -->  bilstm_out = ([128, 200])
            #  bilstm_out = torch.sum(bilstm_out, dim=1)
            bilstm_out = self.hi.cuda() 
            bilstm_out = bilstm_out(out_rnn)
            bilstm_out = torch.tanh(bilstm_out)

            #  attention part:
            #  sum
            #  attn_weights = torch.sum(bilstm_out, dim=2) # BxS

            #  paper
            attn_weights = self.attn_weights.cuda()
            attn_weights = attn_weights(bilstm_out)  # BxSxN --> BxSx1
            attn_weights = torch.tanh(attn_weights)
            #  attn_weights = attn_weights.squeeze(2)
            #  soft_attn = F.softmax(attn_weights, 1)

            energy = self.energy.cuda()
            energy = energy(attn_weights)    # BxSx1
            energy = energy.squeeze(2)       # BxS

            #  creat mask: BxS
            mask = torch.arange(seq_len)[None, :] < seq_lengths[:, None].cpu()
            mask = mask.float()
            mask[mask==0] = -10000000
            energy = energy * mask.cuda()

            #  soft_attn = F.softmax(energy, 1)
            soft_attn = torch.sigmoid(energy)
            soft_attn_sum = torch.sum(soft_attn, dim=1).reshape(-1,1)
            soft_attn = torch.div(soft_attn, soft_attn_sum)


            attn = torch.bmm(bilstm_out.transpose(1,2), soft_attn.unsqueeze(2)).squeeze(2) # BxN
            last_tensor = attn
        else:
            out_rnn = out_rnn.sum(dim=1)
            last_tensor = out_rnn / seq_lengths.type(out_rnn.dtype).unsqueeze(1).expand(out_rnn.shape)

        # shape: (batch_size, label_num)
        out = self.fc(last_tensor)
        return out
