#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import numpy as np
import pandas as pd

if __name__ == "__main__":
    
    file = '../data_title/Data_dev'
    with open(file) as f:
        df = pd.read_csv(file, delimiter='\t', error_bad_lines=False, warn_bad_lines=True)
        label = df['label']
        title = df['title']
        line = df['body']

        write_file = open('Data_dev', 'a')
        d = "label" + '\t' + "title" + '\t' + 'text' + '\t' + "length" + '\n'
        write_file.write(d)
        
        l = ''
        num = n = 0

        for num in range(len(line)):
            l1 = line[num]
            l = ''.join(l1.split())
            l = l.split('#')

            #  a = np.zeros(len(l)-1, dtype=int)
            a = []
            for n in range(len(l)-1):  # ...#
                ll = l[n]
                a.append(len(ll))
            
            #  l = ''.join(l)
            #  l = ' '.join(l)
            a_str = ' '.join(str(e) for e in a)
            a_str += '\n' 
            allwrite = str(label[num]) + '\t' + str(title[num]) + '\t' + l1 + '\t' + a_str
            write_file.write(allwrite)

        write_file.close()

