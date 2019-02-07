#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import re

if __name__ == '__main__':

    your_directory = "/home/lr/lijia/poetry/chinese-poetry-zhCN/poetry/song"
    file_names = os.listdir(your_directory)
    num = 0

    for file_name in file_names:
        file_path = your_directory + "/" + file_name
        num += 1

        #  make file song1.txt
        if num <=  63:
            with open(file_path) as f:
                data = json.load(f)
                write_file = open("song1.txt", "a")
           
                for item in data:
                    paragraphs = item['paragraphs']
                    l = ''
                    # delete ,.() and add lines together
                    for line in paragraphs:
                        #  line = line.strip()
                        line = ' '.join(line)
                        if line == '':
                            continue
                        if line.find('：') >=0 or line.find('{') >= 0 or line.find('[') >=0 or line.find('𡒄') >=0 or line.find('（') >=0:
                            continue
                        if line.find('□') >=0 or line.find('-') >=0 or line.find('〗') >=0 or line.find('、') >= 0:
                            continue
                        line = re.sub(r'！|）|；|？|，|。|》|《|”|“', '', line)
                        l += line
                    
                    #  add label
                    l = str("__label__-1") + '\t' + l + '\n'
                    write_file.write(l)

                write_file.close()

    #  make file song2.txt
        elif num > 63 and num <= 126:
            with open(file_path) as f:
                data = json.load(f)
                write_file = open("song2.txt", "a")
           
                for item in data:
                    paragraphs = item['paragraphs']
                    l = ''
                    # delete ,.() and add lines together
                    for line in paragraphs:
                        #  line = line.strip()
                        line = ' '.join(line)
                        if line == '':
                            continue
                        if line.find('：') >=0 or line.find('{') >= 0 or line.find('[') >=0 or line.find('𡒄') >=0 or line.find('（') >=0:
                            continue
                        if line.find('□') >=0 or line.find('-') >=0 or line.find('〗') >=0 or line.find('、') >= 0:
                            continue
                        line = re.sub(r'！|）|；|？|，|。|》|《|”|“', '', line)
                        l += line
                    
                    #  add label
                    l = str("__label__-1") + '\t' + l + '\n'
                    write_file.write(l)

                write_file.close()

    #  make file song3.txt
        elif num > 126 and num <= 189:
            with open(file_path) as f:
                data = json.load(f)
                write_file = open("song3.txt", "a")
           
                for item in data:
                    paragraphs = item['paragraphs']
                    l = ''
                    # delete ,.() and add lines together
                    for line in paragraphs:
                        #  line = line.strip()
                        line = ' '.join(line)
                        if line == '':
                            continue
                        if line.find('：') >=0 or line.find('{') >= 0 or line.find('[') >=0 or line.find('𡒄') >=0 or line.find('（') >=0:
                            continue
                        if line.find('□') >=0 or line.find('-') >=0 or line.find('〗') >=0 or line.find('、') >= 0:
                            continue
                        line = re.sub(r'！|）|；|？|，|。|》|《|”|“', '', line)
                        l += line
                    
                    #  add label
                    l = str("__label__-1") + '\t' + l + '\n'
                    write_file.write(l)

                write_file.close()

    #  make file song4.txt
        elif num > 189 and num <= 254:
            with open(file_path) as f:
                data = json.load(f)
                write_file = open("song4.txt", "a")
           
                for item in data:
                    paragraphs = item['paragraphs']
                    l = ''
                    # delete ,.() and add lines together
                    for line in paragraphs:
                        #  line = line.strip()
                        line = ' '.join(line)
                        if line == '':
                            continue
                        if line.find('：') >=0 or line.find('{') >= 0 or line.find('[') >=0 or line.find('𥩟') >=0 or line.find('（') >=0:
                            continue
                        if line.find('□') >=0 or line.find('-') >=0 or line.find('〗') >=0 or line.find('、') >= 0:
                            continue
                        line = re.sub(r'！|）|；|？|，|。|》|《|”|“', '', line)
                        l += line
                      
                    #  add label
                    l = str("__label__-1") + '\t' + l + '\n'
                    write_file.write(l)

                write_file.close()
