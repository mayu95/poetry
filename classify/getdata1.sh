#!/bin/sh

# ----------------------------------------------------------------------
# Author      : Jia Li
# Date        : 2018/12/21
# Email       : lijia@gmail.com
# Description :  process data
# ----------------------------------------------------------------------

# 1 step: remove previous .txt and generate xx
input_tang="./tang.txt"
rm -f $input_tang
python ./poetry_tang.py 

input_song1='./song1.txt'
rm -f $input_song1
python ./poetry_song1.py


# 2 step: remove repeated lines and random
tangout="./tangout.txt"
rm -f $tangout
sort $input_tang | uniq | shuf > $tangout

song1out="./song1out.txt"
rm -f $song1out
sort $input_song1 | uniq | shuf > $song1out


# 3 step: split to .train and .valid
tangvalid='./tangout.valid'
rm -f $tangvalid
tail -n 5600 $tangout > $tangvalid

tangtrain='./tangout.train'
rm -f $tangtrain
head -n 50380 $tangout > $tangtrain 

song1valid='./song1out.valid'
rm -f $song1valid
tail -n 5600 $song1out > $song1valid

song1train='./song1out.train'
rm -f $song1train
head -n 57200 $song1out > $song1train
