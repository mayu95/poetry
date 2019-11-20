#!/bin/sh

set -x

# rnn, cnn avg
# data/train.tsv data/test.tsv data/valid.tsv
# python -u main_test.py --encoder "rnn" --bidirectional --data "data_punc_title" --emsize 200 --nhid 200 --nlayers 1 --epochs 30 --batch_size 128 --dropout 0.2 --lr 0.005
# python -u main.py --encoder "rnn" --bidirectional --data "data_punc_title" --emsize 200 --nhid 200 --nlayers 2 --epochs 30 --batch_size 128 --dropout 0.2 --lr 0.005 > log1 &

# python -u main.py --encoder "rnn" --data "data" --emsize 200 --nhid 200 --nlayers 1 --epochs 30 --batch_size 128 --dropout 0.2 --lr 0.005
# python -u main.py --encoder "cnn" --data "data" --emsize 30 --nhid 128 --nlayers 1 --epochs 30 --batch_size 128 --dropout 0.5 --lr 0.005
# python -u main.py --encoder "cnn" --data "trec" --emsize 50 --nhid 128 --nlayers 1 --epochs 30 --batch_size 128 --dropout 0.5 --lr 0.005


# *_test.py
python -u main_sent.py --encoder "rnn" --bidirectional --data "data_no_title" --emsize 200 --nhid 200 --nlayers 1 --epochs 30 --batch_size 128 --dropout 0.2 --lr 0.005 > ./log/log1_1 &
# python -u main_test.py --encoder "rnn" --bidirectional --data "data_punc_title" --emsize 200 --nhid 200 --nlayers 1 --epochs 30 --batch_size 128 --dropout 0.2 --lr 0.005
