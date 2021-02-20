#!/bin/bash
export TZ=Asia/Shanghai
export CUDA_VISIBLE_DEVICES=2
cd /home/chenzw/mydarts-rnn/rnn

python train.py --arch s2_2 --save eval2_2