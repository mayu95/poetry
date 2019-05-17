#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import csv
import pandas as pd

if __name__ == "__main__":
    
    file1 = './valid1.valid_cp'
    with open(file1) as f, open('./valid1.space2', 'w') as fw:
        writer = csv.writer(fw, delimiter='\t')
        writer.writerow(['label','title', 'author',  'body'])

        for line in f:
            l = line.split('\n')[0] 
            l = l.split('\t')
            label = l[0]
            title = l[1]
            author = l[2]
            body = l[3].split('#')
            body.pop()
            alist = ''
            for b in body:
                b = b.split()
                if len(b)%2 != 0:
                    b.append(' ')
                for i in range(0, len(b), 2):
                    alist += b[i] + b[i+1] + ' '
                alist += '#'
            writer.writerow([label, title, author,alist])

    file2 = './train1.train_cp'
    with open(file2) as f, open('./train1.space2', 'w') as fw:
        writer = csv.writer(fw, delimiter='\t')
        writer.writerow(['label','title', 'author',  'body'])

        for line in f:
            l = line.split('\n')[0] 
            l = l.split('\t')
            label = l[0]
            title = l[1]
            author = l[2]
            body = l[3].split('#')
            body.pop()
            alist = ''
            for b in body:
                b = b.split()
                if len(b)%2 != 0:
                    b.append(' ')
                for i in range(0, len(b), 2):
                    alist += b[i] + b[i+1] + ' '
                alist += '#'
            writer.writerow([label, title, author,alist])

