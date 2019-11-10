#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import numpy as np
import pandas as pd

if __name__ == "__main__":
    
    file = './train_4.noTitle'
    with open(file) as f:
        df = pd.read_csv(file, delimiter='\t', error_bad_lines=False, warn_bad_lines=True)
        label = df['label']
        line = df['body']

        write_file = open('train_4.num', 'a')
        d = "label" + '\t' + "text" + '\t' + "leng" + '\n'
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
                #  a[n] = len(ll)
                if n == 0:
                    lll = ll.split('e')   # 以title_end来分割
                    t,s1 = lll[0], lll[1]
                    #  a.append(len(t)-9)
                    a.append(len(t)+1)
                    a.append(len(s1))
                else:
                    a.append(len(ll))
            
            l = ''.join(l)
            l = ' '.join(l)
            a_str = ' '.join(str(e) for e in a)
            a_str += '\n' 
            #  write_file.write(a_str)
            allwrite = str(label[num]) + '\t' + l1 + '\t' + a_str
            #  print(allwrite)
            #  exit(0)
            write_file.write(allwrite)

        write_file.close()

