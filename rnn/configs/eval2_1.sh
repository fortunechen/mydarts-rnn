#!/bin/bash
export TZ=Asia/Shanghai
export CUDA_VISIBLE_DEVICES=5
cd /home/chenzw/mydarts-rnn/rnn

python train.py --arch s2_1 --save eval2_1