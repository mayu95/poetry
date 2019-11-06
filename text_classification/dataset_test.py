#!/usr/bin/env python3

from tqdm import tqdm
import numpy as np
import pandas as pd
from torchtext.data import Field
from torchtext import data as data
from torchtext.data import TabularDataset
from torchtext.data import Iterator, BucketIterator


def word_ids_to_sentence(id_tensor, vocab):
    """Converts a sequence of word ids to a sentence
    id_tensor: torch-based tensor
    vocab: torchtext vocab
    """
    orig_shape = id_tensor.shape
    id_tensor = id_tensor.view(-1)
    res = []
    for i in id_tensor:
        res.append(vocab.itos[i])
    res = np.array(res).reshape(orig_shape)
    #  return res.T
    return res


train_path = 'data_punc_title/train1.no_title'
test_path = 'data_punc_title/test1.no_title'
validation = 'data_punc_title/dev1.no_title'


#  class Mydataset(data.Dataset):
    #  def __init__(self, path, text_field, label_field, test=False, aug=False, **kwargs):
        #  fields = [("label", LABEL), ("text", TEXT), ("len", LEN)]
        #  examples = []
        #  csv_data = pd.read_csv(path, delimiter='\t', error_bad_lines=False, warn_bad_lines=True)
        #  print('read data from {}'.format(path))

        #  super(MyDataset, self).__init__(examples, fields, **kwargs)

    #  def countlen(self, csv_data, fields):
        #  for text in tqdm(csv_data['text']):
            #  sent = text.split('#')
            #  a = []
            #  for n in range(len(sent)-1):
                #  l = sent[n]
                #  a.append = len(l)
            #  seqlen = ' '.join(str(e) for e in a)
            #  print(seqlen)
            #  exit(0)
            #  examples.append(data.Example.fromlist([label, text, seqlen], fields))
        #  return examples, fields





def create_data_iter(batch_size, device, data_root):
    tokenize = lambda x: x.split()
    tokenize_s = lambda x: x.split('#')

    TEXT = Field(
        sequential=True,
        tokenize=tokenize,
        lower=True,
        include_lengths=True,
        batch_first=True
    )
    #  LABEL = Field(sequential=False, use_vocab=True, unk_token=None)
    LABEL = Field(sequential=False, use_vocab=False, unk_token=None)
    # Training and valid data fields 
    tv_datafields = [("label", LABEL), ("text", TEXT)] 
    train, val, test = TabularDataset.splits(
        path=data_root,
        #  train='train_#.tsv', validation="valid_#.tsv", test="test_#.tsv",
        train='train1.no_title', validation="dev1.no_title", test="test1.no_title",
        format='tsv',
        skip_header=False,
        fields=tv_datafields
    )

    TEXT.build_vocab(train)
    LABEL.build_vocab(train)

    train_iter, val_iter, test_iter = BucketIterator.splits(
        (train, val, test),
        batch_sizes=(batch_size, batch_size, batch_size),
        device=device, 
        sort_key=lambda x: len(x.text),
        sort_within_batch=True,
        repeat=False
    )

    return TEXT, LABEL, train_iter, val_iter, test_iter

if __name__ == "__main__":
    #  TEXT, LABEL, train_iter, val_iter, test_iter = create_data_iter(20, -1, "data_2gram_no_oov")
    TEXT, LABEL, train_iter, val_iter, test_iter = create_data_iter(20, -1, "data_punc_title")
    padding_index = TEXT.vocab.stoi["<pad>"]
    print(f"padding_index: {padding_index}")
    print(f"index 0 in vocab: {TEXT.vocab.itos[0]}")
    for counter, batch in enumerate(test_iter, 1):
        text_int, text_len = batch.text[0], batch.text[1]
        label_int = batch.label
        print(word_ids_to_sentence(text_int, TEXT.vocab))
        print(word_ids_to_sentence(label_int, LABEL.vocab))
        print(f"len: {text_len}")
        print(label_int)
        break
