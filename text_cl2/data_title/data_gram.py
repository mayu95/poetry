#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import csv
#  import pandas as pd

if __name__ == "__main__":
    
    file1 = './test1'
    with open(file1) as f, open('/home/lr/lijia/poetry/text_classification/data_punc_title/test_1.noTitle', 'w') as fw:
        writer = csv.writer(fw, delimiter='\t')
        for line in f:
            l = line.split('\n')[0] 
            l = l.split('\t')
            label = l[0]
            title = l[1]
            body = l[2]
            alist = title + ' e ' + body 

            writer.writerow([label, alist])

    file2 = './test2'
    with open(file2) as f, open('/home/lr/lijia/poetry/text_classification/data_punc_title/test_2.noTitle', 'w') as fw:
        writer = csv.writer(fw, delimiter='\t')
        for line in f:
            l = line.split('\n')[0] 
            l = l.split('\t')
            label = l[0]
            title = l[1]
            body = l[2]
            alist = title + ' e ' + body 

            writer.writerow([label, alist])

    file3 = './test3'
    with open(file3) as f, open('/home/lr/lijia/poetry/text_classification/data_punc_title/test_3.noTitle', 'w') as fw:
        writer = csv.writer(fw, delimiter='\t')
        for line in f:
            l = line.split('\n')[0] 
            l = l.split('\t')
            label = l[0]
            title = l[1]
            body = l[2]
            alist = title + ' e ' + body 

            writer.writerow([label, alist])

    file4 = './test4'
    with open(file4) as f, open('/home/lr/lijia/poetry/text_classification/data_punc_title/test_4.noTitle', 'w') as fw:
        writer = csv.writer(fw, delimiter='\t')
        for line in f:
            l = line.split('\n')[0] 
            l = l.split('\t')
            label = l[0]
            title = l[1]
            body = l[2]
            alist = title + ' e ' + body 

            writer.writerow([label, alist])

    file5 = './train1'
    with open(file5) as f, open('/home/lr/lijia/poetry/text_classification/data_punc_title/train_1.noTitle', 'w') as fw:
        writer = csv.writer(fw, delimiter='\t')
        for line in f:
            l = line.split('\n')[0] 
            l = l.split('\t')
            label = l[0]
            title = l[1]
            body = l[2]
            alist = title + ' e ' + body 

            writer.writerow([label, alist])

    file6 = './train2'
    with open(file6) as f, open('/home/lr/lijia/poetry/text_classification/data_punc_title/train_2.noTitle', 'w') as fw:
        writer = csv.writer(fw, delimiter='\t')
        for line in f:
            l = line.split('\n')[0] 
            l = l.split('\t')
            label = l[0]
            title = l[1]
            body = l[2]
            alist = title + ' e ' + body 
            writer.writerow([label, alist])

    file7 = './train3'
    with open(file7) as f, open('/home/lr/lijia/poetry/text_classification/data_punc_title/train_3.noTitle', 'w') as fw:
        writer = csv.writer(fw, delimiter='\t')
        for line in f:
            l = line.split('\n')[0] 
            l = l.split('\t')
            label = l[0]
            title = l[1]
            body = l[2]
            alist = title + ' e ' + body 
            writer.writerow([label, alist])

    file8 = './train4'
    with open(file8) as f, open('/home/lr/lijia/poetry/text_classification/data_punc_title/train_4.noTitle', 'w') as fw:
        writer = csv.writer(fw, delimiter='\t')
        for line in f:
            l = line.split('\n')[0] 
            l = l.split('\t')
            label = l[0]
            title = l[1]
            body = l[2]
            alist = title + ' e ' + body 
            writer.writerow([label, alist])

