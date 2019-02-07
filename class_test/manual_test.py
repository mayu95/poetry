#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import re

if __name__ == '__main__':

    with open('./manual_tang.txt','r') as file:
        data = file.readlines()  
        write_file = open("./manutal_tang.valid", "a")

        for line in data:
            line = ' '.join(line)
            line = re.sub(r'！|）|；|？|，|。|》|《|”|“', '', line)
            line = str("__label__1") + '\t' + line
            write_file.write(line)

        write_file.close()
