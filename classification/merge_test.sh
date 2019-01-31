#!/bin/sh

# ----------------------------------------------------------------------
# Author      : Jia Li
# Date        : 2018/12/21
# Email       : lijia@gmail.com
# Description :  process data
# ----------------------------------------------------------------------

set -x

# 1 step: merge .train and .valid
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


# 2 step: run fasttext
model1="model_train1"
rm -f $model1.bin $model1.vec
/home/lr/lijia/fastText/fasttext supervised -input $train1 -output $model1
/home/lr/lijia/fastText/fasttext test $model1.bin $valid1 

model2="model_train2"
rm -f $model2.bin $model2.vec
/home/lr/lijia/fastText/fasttext supervised -input $train2 -output $model2
/home/lr/lijia/fastText/fasttext test $model2.bin $valid2 

model3="model_train3"
rm -f $model3.bin $model3.vec
/home/lr/lijia/fastText/fasttext supervised -input $train3 -output $model3
/home/lr/lijia/fastText/fasttext test $model3.bin $valid3 

model4="model_train4"
rm -f $model4.bin $model4.vec
/home/lr/lijia/fastText/fasttext supervised -input $train4 -output $model4
/home/lr/lijia/fastText/fasttext test $model4.bin $valid4 

