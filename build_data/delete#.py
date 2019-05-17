#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import numpy as np
import pandas as pd

if __name__ == "__main__":
    
    file = 'train1.train_cp'
    with open(file) as f:
        df = pd.read_csv(file, delimiter='\t', error_bad_lines=False, warn_bad_lines=True)
        line = df['body']
        write_file = open('train1.train_num', 'a')
        l = ''
        num = n = 0

        for num in range(len(line)):
            l = line[num]
            l = ''.join(l.split())
            l = l.split('#')

            #  a = np.zeros(len(l)-1, dtype=int)
            a = []
            for n in range(len(l)-1):  # ...#
                ll = l[n]
                #  a[n] = len(ll)
                a.append(len(ll))
            
            l = ''.join(l)
            l = ' '.join(l)
            a_str = ' '.join(str(e) for e in a)
            a_str += '\n' 
            write_file.write(a_str)

        write_file.close()

