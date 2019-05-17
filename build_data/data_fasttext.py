#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import numpy as np
import pandas as pd

if __name__ == "__main__":
    
    file1 = './valid1.space2fast'
    with open(file1) as f:
        df = pd.read_csv(file1, delimiter='\t', error_bad_lines=False, warn_bad_lines=True)
        df.pop('title')
        df.pop('author')
        df.to_csv('./valid1.space2fasttext', index=False, sep='\t')

    file2 = './train1.space2fast'
    with open(file1) as f:
        df = pd.read_csv(file2, delimiter='\t', error_bad_lines=False, warn_bad_lines=True)
        df.pop('title')
        df.pop('author')
        df.to_csv('./train1.space2fasttext', index=False, sep='\t')
