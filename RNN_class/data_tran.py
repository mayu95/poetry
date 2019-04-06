#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import re

if __name__ == '__main__':

    your_directory = "/home/lr/lijia/Pytorch-RNN-text-classification/data_poetry"
    file_names = os.listdir(your_directory)
    num = 0

    for file_name in file_names:
        file_path = your_directory + "/" + file_name
        num += 1

        #  make file song1.txt
        with open(file_path) as f:
            write_file = open(your_directory + "/rnn_" + file_name, 'w')
            for line in f:
                line = line.replace("𫎩", '')
                line = line.replace('__label__-1', '0')
                line = line.replace("__label__1", "1")
                
                write_file.write(line)

            
            write_file.close()

        print(num, ' : ', file_name)

