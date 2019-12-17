#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import collections

if __name__ == "__main__":
    
    file = 'final_result'
    t_dic = {}
    s_dic = {}
    all_dic = {}
    t_dictionary = {}
    s_dictionary = {}
    all_dictionary = {}
    t_freq = {}
    s_freq = {}
    all_freq = {}
    t = 0
    s = 0
    poem = 0
    sentence = []
    attn = 0 
    with open(file) as f:
        lines = f.readlines()

        write_file_all = open('freq_all', 'a')
        d_all = "word" + '\t' + "count in all" + '\n'
        write_file_all.write(d_all)
        
        write_file_tang = open('freq_tang', 'a')
        d_tang = "word" + '\t' + "count in tang" + '\n'
        write_file_tang.write(d_tang)
       
        write_file_song = open('freq_song', 'a')
        d_song = "word" + '\t' + "count in song" + '\n'
        write_file_song.write(d_song)

        for line in lines:
            line = line.split()
            #  tang(1) or song(0)
            if line[0] == '0': 
                s = 1
                poem = 1
                continue
            elif line[0] == '1':
                t = 1
                poem = 1
                continue
            
            #  sencent line
            if poem == 1:
                poem = 0
                attn = 1
                sentence = line
                continue

            #  attention line
            if attn == 1: 
                attn = 0
                attention = []
                for i in line:
                    attention.append(float(i))
                #  attn_sorted = sorted(attention, reverse=True)
                sort_index = np.argsort(attention)[::-1][:5]
                for i in sort_index:
                    w = sentence[i]
                    all_dic[w] = all_dic.setdefault(w,0) + 1
                    if s == 1:
                        s_dic[w] = s_dic.setdefault(w,0) + 1
                    elif t == 1:
                        t_dic[w] = t_dic.setdefault(w,0) + 1
                if s == 1:
                    s = 0
                    for w in sentence:
                        all_dictionary[w] = all_dictionary.setdefault(w,0) + 1
                        s_dictionary[w] = s_dictionary.setdefault(w,0) + 1
                elif t == 1:
                    t = 0
                    for w in sentence:
                        all_dictionary[w] = all_dictionary.setdefault(w,0) + 1
                        t_dictionary[w] = t_dictionary.setdefault(w,0) + 1
                sentence = []

                #  for i,j in all_dic.items():
                    #  print(i,j)

        for k,v in all_dic.items():
            if v < 1000:
                continue
            f = v/all_dictionary[k]
            all_freq[k] = all_freq.setdefault(k,0) + f 
        for k,v in s_dic.items():
            if v < 1000:
                continue
            f = v/s_dictionary[k]
            s_freq[k] = s_freq.setdefault(k,0) + f 
        for k,v in t_dic.items():
            if v < 250: 
                continue
            f = v/t_dictionary[k]
            t_freq[k] = t_freq.setdefault(k,0) + f 

        all_freq = sorted(all_freq.items(), key=lambda x:x[1], reverse=True)
        all_freq = collections.OrderedDict(all_freq)
        for i,j in all_freq.items():
            allwrite = i + '\t' + str(j) + '\n' 
            write_file_all.write(allwrite)
        t_freq = sorted(t_freq.items(), key=lambda x:x[1], reverse=True)
        t_freq = collections.OrderedDict(t_freq)
        for i,j in t_freq.items():
            allwrite = i + '\t' + str(j) + '\n'
            write_file_tang.write(allwrite)
        s_freq = sorted(s_freq.items(), key=lambda x:x[1], reverse=True)
        s_freq = collections.OrderedDict(s_freq)
        for i,j in s_freq.items():
            allwrite = i + '\t' + str(j) +'\n'
            write_file_song.write(allwrite)
            

        #  output the frequncy count dictionary
        #  all_dic = sorted(all_dic.items(), key=lambda x:x[1], reverse=True)
        #  all_dic = collections.OrderedDict(all_dic)
        #  for i,j in all_dic.items():
            #  allwrite = i + '\t' + str(j) + '\n' 
            #  write_file_all.write(allwrite)
        #  t_dic = sorted(t_dic.items(), key=lambda x:x[1], reverse=True)
        #  t_dic = collections.OrderedDict(t_dic)
        #  for i,j in t_dic.items():
            #  allwrite = i + '\t' + str(j) + '\n'
            #  write_file_tang.write(allwrite)
        #  s_dic = sorted(s_dic.items(), key=lambda x:x[1], reverse=True)
        #  s_dic = collections.OrderedDict(s_dic)
        #  for i,j in s_dic.items():
            #  allwrite = i + '\t' + str(j) +'\n'
            #  write_file_song.write(allwrite)

        write_file_all.close()
        write_file_tang.close()
        write_file_song.close()

