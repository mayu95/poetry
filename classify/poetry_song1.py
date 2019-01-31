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
        if num > 63:
            print(num)
            exit(0)

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
                    line = re.sub(r'）|；|？|，|。|》|《|”|“', '', line)
                    l += line
                    
                #  add label
                l = str("__label__-1") + '\t' + l + '\n'
                write_file.write(l)

            write_file.close()


