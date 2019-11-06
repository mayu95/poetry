#!/bin/sh

# print commands
set -x

# 1 step: remove previous .txt and generate xx
input_tang="./tang.txt"
# rm -f $input_tang
# python ./poetry_tang.py 

input_song1='./song1.txt'
input_song2='./song2.txt'
input_song3='./song3.txt'
input_song4='./song4.txt'
# rm -f $input_song1 $input_song2 $input_song3 $input_song4
# python ./poetry_song.py


# 2 step: remove repeated lines and random
tangout="./tangout.txt"
# rm -f $tangout
sort $input_tang | uniq | shuf > $tangout

Songout="./Songout.txt"
songout="./songout.txt"
song1out="./song1out.txt"
song2out="./song2out.txt"
song3out="./song3out.txt"
song4out="./song4out.txt"
# rm -f $songout $song1out $song2out $song3out  $song4out

# sort $input_song1 $input_song2 $input_song3 $input_song4 | uniq | shuf > $Songout
# 可以不要下面这个sort，直接用上一个sort的结果
# sort $Songout | uniq | shuf > $songout

# head -n 62836 $songout > $song1out
# head -n 125672 $songout | tail -n +62836 > $song2out
# tail -n 125672 $songout | head -n -62836 > $song3out
# tail -n 62836 $songout > $song4out


# 3 step: split to .train and .valid
tangvalid='./tangout.valid'
tangtrain='./tangout.train'
rm -f $tangvalid $tangtrain
tail -n 5600 $tangout > $tangvalid
head -n 50938 $tangout > $tangtrain 

song1valid='./song1out.valid'
song1train='./song1out.train'
rm -f $song1valid $song1train
tail -n 6280 $song1out > $song1valid
head -n 56555 $song1out > $song1train

song2valid='./song2out.valid'
song2train='./song2out.train'
rm -f $song2valid $song2train
tail -n 6280 $song2out > $song2valid
head -n 56555 $song2out > $song2train

song3valid='./song3out.valid'
song3train='./song3out.train'
rm -f $song3valid $song3train
tail -n 6280 $song3out > $song3valid
head -n 56555 $song3out > $song3train

song4valid='./song4out.valid'
song4train='./song4out.train'
rm -f $song4valid $song4train
tail -n 6280 $song4out > $song4valid
head -n 56555 $song4out > $song4train

# 4 step: merge .train and .valid
train1='train1.train'
valid1='valid1.valid'
rm -f $train1 $valid1
cat song1out.train tangout.train | shuf > $train1
cat song1out.valid tangout.valid > $valid1

train2='train2.train'
valid2='valid2.valid'
rm -f $train2 $valid2
cat song2out.train tangout.train | shuf > $train2
cat song2out.valid tangout.valid > $valid2

train3='train3.train'
valid3='valid3.valid'
rm -f $train3 $valid3
cat song3out.train tangout.train | shuf > $train3
cat song3out.valid tangout.valid > $valid3

train4='train4.train'
valid4='valid4.valid'
rm -f $train4 $valid4
cat song4out.train tangout.train | shuf > $train4
cat song4out.valid tangout.valid > $valid4
