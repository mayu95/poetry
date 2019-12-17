#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import csv
#  import pandas as pd

if __name__ == "__main__":
    
    file1 = 'Train'
    with open(file1) as f, open('./Train_data', 'w') as fw:
        writer = csv.writer(fw, delimiter='\t')
        for line in f:
            l = line.split('\n')[0] 
            l = l.split('\t')
            label = l[0]
            t = l[1] 
            author = l[2]
            body = l[3]
            #  body2 = '' 
            #  for i in body:
                #  body2 += ' ' + i
            writer.writerow([label, t, body])

    file2 = './Test'
    with open(file2) as f, open('Test_data', 'w') as fw:
        writer = csv.writer(fw, delimiter='\t')
        for line in f:
            l = line.split('\n')[0] 
            l = l.split('\t')
            label = l[0]
            title = l[1]
            author = l[2]
            body = l[3]
            #  body = l[2]
            #  title2 = '' 
            #  for i in title:
                #  title2 += ' ' + i
            writer.writerow([label, title, body])

    file3 = './Dev'
    with open(file3) as f, open('Dev_data', 'w') as fw:
        writer = csv.writer(fw, delimiter='\t')
        for line in f:
            l = line.split('\n')[0] 
            l = l.split('\t')
            label = l[0]
            title = l[1]
            author = l[2]
            body = l[3]
            #  body = l[2]
            #  title2 = '' 
            #  for i in title:
                #  title2 += ' ' + i
            writer.writerow([label, title, body])

    #  file4 = './test_4.title'
    #  with open(file4) as f, open('/home/lr/lijia/poetry/text_cl2/data_title/test4', 'w') as fw:
        #  writer = csv.writer(fw, delimiter='\t')
        #  for line in f:
            #  l = line.split('\n')[0] 
            #  l = l.split('\t')
            #  label = l[0]
            #  title = l[1]
            #  body = l[2]
            #  title2 = '' 
            #  for i in title:
                #  title2 += ' ' + i
            #  writer.writerow([label, title2, body])

    #  file5 = './train_1.title'
    #  with open(file5) as f, open('/home/lr/lijia/poetry/text_cl2/data_title/train1', 'w') as fw:
        #  writer = csv.writer(fw, delimiter='\t')
        #  for line in f:
            #  l = line.split('\n')[0] 
            #  l = l.split('\t')
            #  label = l[0]
            #  title = l[1]
            #  body = l[2]
            #  title2 = '' 
            #  for i in title:
                #  title2 += ' ' + i
            #  writer.writerow([label, title2, body])

    #  file6 = './train_2.title'
    #  with open(file6) as f, open('/home/lr/lijia/poetry/text_cl2/data_title/train2', 'w') as fw:
        #  writer = csv.writer(fw, delimiter='\t')
        #  for line in f:
            #  l = line.split('\n')[0] 
            #  l = l.split('\t')
            #  label = l[0]
            #  title = l[1]
            #  body = l[2]
            #  title2 = '' 
            #  for i in title:
                #  title2 += ' ' + i
            #  writer.writerow([label, title2, body])

    #  file7 = './train_3.title'
    #  with open(file7) as f, open('/home/lr/lijia/poetry/text_cl2/data_title/train3', 'w') as fw:
        #  writer = csv.writer(fw, delimiter='\t')
        #  for line in f:
            #  l = line.split('\n')[0] 
            #  l = l.split('\t')
            #  label = l[0]
            #  title = l[1]
            #  body = l[2]
            #  title2 = '' 
            #  for i in title:
                #  title2 += ' ' + i
            #  writer.writerow([label, title2, body])

    #  file8 = './train_4.title'
    #  with open(file8) as f, open('/home/lr/lijia/poetry/text_cl2/data_title/train4', 'w') as fw:
        #  writer = csv.writer(fw, delimiter='\t')
        #  for line in f:
            #  l = line.split('\n')[0] 
            #  l = l.split('\t')
            #  label = l[0]
            #  title = l[1]
            #  body = l[2]
            #  title2 = '' 
            #  for i in title:
                #  title2 += ' ' + i
            #  writer.writerow([label, title2, body])

