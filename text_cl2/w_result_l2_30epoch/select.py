#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import collections

if __name__ == "__main__":
    
    file = 'w_result_l2_13'
    poem = 0
    sentence = []
    attention = []
    attn = 0 
    t = 0
    s = 0

    with open(file) as f:
        lines = f.readlines()
        write_file_all = open('peach_all', 'a')

        for line in lines:
            line = line.split()
            # title line
            if line[0] == '0' or line[0] == '1':
                # if peach
                if "桃花" in line[1]:
                    poem = 1
                    title_line = line[0] + '\t' + line[1] + '\n'
                    write_file_all.write(title_line)
                    if line[0] == '0':
                        s += 1
                    else:
                        t += 1
                continue

            #  sentence line
            if poem == 1:
                poem, attn = 0, 1
                sentence = ' '.join(line) + '\n'
                write_file_all.write(sentence)
                continue

            #  attention line
            if attn == 1:
                attn = 0
                attention = ' '.join(line) + '\n'
                write_file_all.write(attention)
                continue

        d = 'tang poem: ' + str(t) + '\t' + 'song poem: ' + str(s)
        write_file_all.write(d)
        write_file_all.close()

