#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import re

if __name__ == '__main__':

    your_directory = "/home/lr/lijia/poetry/chinese-poetry-zhCN/poetry/tang"
    file_names = os.listdir(your_directory)
    num = 0

    for file_name in file_names:
        file_path = your_directory + "/" + file_name
        num += 1
        
        with open(file_path) as f:
            data = json.load(f)
            write_file = open("tang.txt", "a")
           
            for item in data:
                paragraphs = item['paragraphs']
                title = item['title']
                title = re.sub(r'\t', ' ', title)
                author = item['author']
                l = ''

                # delete ,.() and add lines together
                for line in paragraphs:
                    if len(line) < 10:
                        continue
                    #  line = line.strip()
                    line = ' '.join(line)
                    if line == '':
                        continue
                    if line.find('：') >=0 or line.find('｛') >= 0 or line.find('[') >=0 or line.find('𡒄') >=0 or line.find('（') >=0:
                        continue
                    if line.find('□') >=0 or line.find('-') >=0 or line.find('〗') >=0 or line.find('、') >= 0:
                        continue
                    line = re.sub(r'1|2|3|4|5|6|7|8|9|0', '', line)
                    line = re.sub("(.*)", '', line)
                    line = re.sub(r'；|<|>|》|#|《|”|“', '', line)
                    line = re.sub(r'，|。|？',' # ',line)
                    l += line

                #  add label
                if l != '':
                    l = str("1") + '\t' + title + '\t' + author +  '\t' + l + '\n'
                    write_file.write(l)

            write_file.close()

    print(num)


