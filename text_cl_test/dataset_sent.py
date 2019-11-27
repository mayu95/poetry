#!/usr/bin/env python3

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


def create_data_iter(batch_size, device, data_root):
    tokenize = lambda x: x.split()
    #  tokenize_s = lambda x: x.split('#')

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
    tv_datafields = [("label", LABEL), ("text", TEXT), ("leng", TEXT)] 
    train, val, test = TabularDataset.splits(
        path=data_root,
        #  train='train_#.tsv', validation="valid_#.tsv", test="test_#.tsv",
        #  train='train1.no_title_num', validation="dev1.no_title_num", test="test1.no_title_num",
        train='train_1.num', validation="test_2.num", test="test_1.num",
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
    TEXT, LABEL, train_iter, val_iter, test_iter = create_data_iter(20, -1, "data_punc_title")
    padding_index = TEXT.vocab.stoi["<pad>"]
    print(f"padding_index: {padding_index}")
    print(f"index 0 in vocab: {TEXT.vocab.itos[0]}")
    for counter, batch in enumerate(test_iter, 1):
        text_int, text_len = batch.text[0], batch.text[1]
        leng_int, leng_len = batch.leng[0], batch.leng[1]
        label_int = batch.label
        print(word_ids_to_sentence(text_int, TEXT.vocab))
        print(word_ids_to_sentence(leng_int, TEXT.vocab))
        print(word_ids_to_sentence(label_int, LABEL.vocab))
        print(f"len: {text_len}")
        print(f"len: {leng_len}")
        print(label_int)
        #  print(f"len:{leng_int}")
        break