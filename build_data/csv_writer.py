#!/usr/bin/env python3

import csv

if __name__ == "__main__":
    
    headers = ['label', 'title', 'author', 'body']

    with open('valid1.valid_s', 'a') as f:

        #  write_file = open('valid1.valid_ss', 'a')
        f_tsv = csv.writer(f, delimiter='\t')
        f_tsv.writerow(headers)


        f.close()
