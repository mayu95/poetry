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
    with open(file1) as f:
        df = pd.read_csv(file2, delimiter='\t', error_bad_lines=False, warn_bad_lines=True)
        df.pop('author')
        df.to_csv('/home/lr/lijia/poetry/text_cl2/data_title/test_4.title', index=False, sep='\t')
        
    #  file1 = './test1.title'
    #  with open(file1) as f:
        #  df = pd.read_csv(file1, delimiter='\t', error_bad_lines=False, warn_bad_lines=True)
        #  df.pop('title')
        #  df.to_csv('/home/lr/lijia/poetry/text_classification/data_punc_title/test1.no_title', index=False, sep='\t')
