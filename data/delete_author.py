#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import numpy as np
import pandas as pd

if __name__ == "__main__":
    
    file1 = './train4.train'
    with open(file1) as f:
        df = pd.read_csv(file1, delimiter='\t', error_bad_lines=False, warn_bad_lines=True)
        df.pop('author')
        df.to_csv('/home/lr/lijia/poetry/text_cl2/data_title/train_4.title', index=False, sep='\t')

    file2 = './valid4.valid'
    with open(file2) as f:
        df = pd.read_csv(file2, delimiter='\t', error_bad_lines=False, warn_bad_lines=True)
        df.pop('author')
        df.to_csv('/home/lr/lijia/poetry/text_cl2/data_title/test_4.title', index=False, sep='\t')
        
    file3 = './train3.train'
    with open(file3) as f:
        df = pd.read_csv(file3, delimiter='\t', error_bad_lines=False, warn_bad_lines=True)
        df.pop('author')
        df.to_csv('/home/lr/lijia/poetry/text_cl2/data_title/train_3.title', index=False, sep='\t')

    file4 = './valid3.valid'
    with open(file4) as f:
        df = pd.read_csv(file4, delimiter='\t', error_bad_lines=False, warn_bad_lines=True)
        df.pop('author')
        df.to_csv('/home/lr/lijia/poetry/text_cl2/data_title/test_3.title', index=False, sep='\t')

    file5 = './train2.train'
    with open(file5) as f:
        df = pd.read_csv(file5, delimiter='\t', error_bad_lines=False, warn_bad_lines=True)
        df.pop('author')
        df.to_csv('/home/lr/lijia/poetry/text_cl2/data_title/train_2.title', index=False, sep='\t')

    file6 = './valid2.valid'
    with open(file6) as f:
        df = pd.read_csv(file6, delimiter='\t', error_bad_lines=False, warn_bad_lines=True)
        df.pop('author')
        df.to_csv('/home/lr/lijia/poetry/text_cl2/data_title/test_2.title', index=False, sep='\t')

    file7 = './train1.train'
    with open(file7) as f:
        df = pd.read_csv(file7, delimiter='\t', error_bad_lines=False, warn_bad_lines=True)
        df.pop('author')
        df.to_csv('/home/lr/lijia/poetry/text_cl2/data_title/train_1.title', index=False, sep='\t')

    file8 = './valid1.valid'
    with open(file8) as f:
        df = pd.read_csv(file8, delimiter='\t', error_bad_lines=False, warn_bad_lines=True)
        df.pop('author')
        df.to_csv('/home/lr/lijia/poetry/text_cl2/data_title/test_1.title', index=False, sep='\t')
