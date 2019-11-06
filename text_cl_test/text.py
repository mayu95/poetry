#!/usr/bin/env python3

from torchtext.data import Field
from torchtext.data import NestedField
import pprint

def sent_split(poem):
    return [sent for sent in doc.split('#')]


def get_iter(poem):
    nesting_field = Field(sequential=True, include_lengths=False,
            batch_first=True)
    nestedField = NestedField(nesting_field=nesting_field, include_lengths=False, 
            tokenize=sent_split)
    return NestedField



if __name__ == "__main__":
    poem = "一 去 二 三 里 #烟 村 四 五 家# 亭 台 六 七 座# 八九十枝花 #"
    padded = get_iter(poem)
    pprint(padded)
