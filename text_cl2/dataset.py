#!/usr/bin/env python3

import numpy as np
from torchtext.data import Field
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


def create_data_iter(batch_size, device, data_root):
    tokenize = lambda x: x.split()
    TEXT = Field(
        sequential=True,
        tokenize=tokenize,
        lower=True,
        include_lengths=True,
        batch_first=True
    )
    LABEL = Field(sequential=False, use_vocab=True, unk_token=None)
    # Training and valid data fields 
    tv_datafields = [("label", LABEL), ("title", TEXT), ("text", TEXT)] 
    train, val, test = TabularDataset.splits(
        path=data_root,
        #  train='Train_data', validation="Dev_data", test="Test_data",
        train='Data_train', validation="Data_dev", test="Data_test",
        #  train='Train11', validation="Dev11", test="test1",
        format='tsv',
        skip_header=False,
        fields=tv_datafields,
        #  csv_reader_params=(error_bad_lines=False, warn_bad_lines=True)
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
    TEXT, LABEL, train_iter, val_iter, test_iter = create_data_iter(20, -1, "data_title")
    padding_index = TEXT.vocab.stoi["<pad>"]
    print(f"padding_index: {padding_index}")
    print(f"index 0 in vocab: {TEXT.vocab.itos[0]}")
    for counter, batch in enumerate(test_iter, 1):
        text_int, text_len = batch.text[0], batch.text[1]
        title_int, title_len = batch.title[0], batch.title[1]
        label_int = batch.label
        print(word_ids_to_sentence(text_int, TEXT.vocab))
        print(text_int)
        sp = TEXT.vocab.stoi["#"]
        print(f"# is : {sp}")
        unk = TEXT.vocab.stoi["<unk>"]
        print(f"unk_token is : {unk}")
        #  print(word_ids_to_sentence(title_int, TEXT.vocab))
        #  print(word_ids_to_sentence(label_int, LABEL.vocab))
        print(f"len: {text_len}")
        #  print(f"len: {title_len}")
        #  print(label_int)
        break
