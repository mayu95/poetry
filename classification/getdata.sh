#!/bin/sh

# ----------------------------------------------------------------------
# Author      : Jia Li
# Date        : 2018/12/21
# Email       : lijia@gmail.com
# Description :  process data
# ----------------------------------------------------------------------

set -x

# 1 step: remove previous .txt and generate xx
input_tang="./tang.txt"
rm -f $input_tang
python ./poetry_tang.py 

input_song1='./song1.txt'
input_song2='./song2.txt'
input_song3='./song3.txt'
input_song4='./song4.txt'
rm -f $input_song1 $input_song2 $input_song3 $input_song4
python ./poetry_song.py


# 2 step: remove repeated lines and random
tangout="./tangout.txt"
rm -f $tangout
sort $input_tang | uniq | shuf > $tangout

song1out="./song1out.txt"
rm -f $song1out
sort $input_song1 | uniq | shuf > $song1out

song2out="./song2out.txt"
rm -f $song2out
sort $input_song2 | uniq | shuf > $song2out

song3out="./song3out.txt"
rm -f $song3out
sort $input_song3 | uniq | shuf > $song3out

song4out="./song4out.txt"
rm -f $song4out
sort $input_song4 | uniq | shuf > $song4out


# 3 step: split to .train and .valid
tangvalid='./tangout.valid'
tangtrain='./tangout.train'
rm -f $tangvalid $tangtrain
tail -n 5600 $tangout > $tangvalid
head -n 50380 $tangout > $tangtrain 

song1valid='./song1out.valid'
song1train='./song1out.train'
rm -f $song1valid $song1train
tail -n 5600 $song1out > $song1valid
head -n 57200 $song1out > $song1train

song2valid='./song2out.valid'
song2train='./song2out.train'
rm -f $song2valid $song2train
tail -n 5600 $song2out > $song2valid
head -n 57200 $song2out > $song2train

song3valid='./song3out.valid'
song3train='./song3out.train'
rm -f $song3valid $song3train
tail -n 5600 $song3out > $song3valid
head -n 56480 $song3out > $song3train

song4valid='./song4out.valid'
song4train='./song4out.train'
rm -f $song4valid $song4train
tail -n 5600 $song4out > $song4valid
head -n 58950 $song4out > $song4train

