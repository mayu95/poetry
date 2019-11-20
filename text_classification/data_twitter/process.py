#!/usr/bin/env python3

import pandas as pd

if __name__ == "__main__":
    file = 'twitdataB_part5.tsv'
    with open(file) as f:
        df = pd.read_csv(file, delimiter='\t', quoting=3, escapechar=None, error_bad_lines=False, warn_bad_lines=True)
        label = df['label']
        line = df['body']

        write_file = open('train_pos', 'a')
        
        for num in range(len(line)):
            l1 = line[num]
            lb = label[num]
            #  choose positive and negative labels
            #  if lb == 'positive' or lb == 'negative':
            #  choose positive and not positive labels
            if lb != 'positive':
                lb = 1 
            else:
                lb = 0 
            #  delete not available
            if l1 == 'Not Available':
                continue
            a = str(lb) + '\t' + str(l1)
            write_file.write(str(lb) + '\t' + str(l1) + '\n')
        
        write_file.close()

