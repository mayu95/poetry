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
rm -f $train1
cat song1out.train tangout.train | shuf > $train1

valid1='valid1.valid'
rm -f $valid1
cat song1out.valid tangout.valid > $valid1



# 2 step: run fasttext
model="model_train1"
rm -f $model.bin $model.vec
/home/lr/lijia/fastText/fasttext supervised -input $train1 -output $model

/home/lr/lijia/fastText/fasttext test $model.bin $valid1 
