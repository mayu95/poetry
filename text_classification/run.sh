#!/bin/sh

set -x

# rnn, cnn avg
# data/train.tsv data/test.tsv data/valid.tsv
# python -u main.py --encoder "rnn" --bidirectional --data "data_punc_title" --emsize 200 --nhid 200 --nlayers 1 --epochs 30 --batch_size 128 --dropout 0.2 --lr 0.005 
# python -u main.py --encoder "rnn" --bidirectional --data "data_punc_title" --emsize 200 --nhid 200 --nlayers 2 --epochs 30 --batch_size 128 --dropout 0.2 --lr 0.005 > log1 &
# python -u main.py --encoder "rnn" --bidirectional --data "data_punc_title" --emsize 200 --nhid 200 --nlayers 1 --epochs 30 --batch_size 128 --dropout 0.2 --lr 0.005 > word_bias_log3 &
# python -u main.py --encoder "rnn" --bidirectional --data "data_punc_title" --emsize 200 --nhid 200 --nlayers 1 --epochs 30 --batch_size 128 --dropout 0.2 --lr 0.005 > new_data3 &

# python -u main.py --encoder "rnn" --data "data" --emsize 200 --nhid 200 --nlayers 1 --epochs 30 --batch_size 128 --dropout 0.2 --lr 0.005
# python -u main.py --encoder "cnn" --data "data" --emsize 30 --nhid 128 --nlayers 1 --epochs 30 --batch_size 128 --dropout 0.5 --lr 0.005
# python -u main.py --encoder "cnn" --data "trec" --emsize 50 --nhid 128 --nlayers 1 --epochs 30 --batch_size 128 --dropout 0.5 --lr 0.005


# *_test.py
# python -u main_test.py --encoder "rnn" --bidirectional --data "data_punc_title" --emsize 200 --nhid 200 --nlayers 1 --epochs 30 --batch_size 128 --dropout 0.2 --lr 0.005 > testlog2 &
# python -u main_test.py --encoder "rnn" --bidirectional --data "data_punc_title" --emsize 200 --nhid 200 --nlayers 1 --epochs 30 --batch_size 128 --dropout 0.2 --lr 0.005


# SemEval 2013 
python -u main_F1.py --encoder "rnn" --bidirectional --data "data_twitter" --emsize 350 --nhid 350 --nlayers 2 --epochs 20 --batch_size 128 --dropout 0.2 --lr 0.005
