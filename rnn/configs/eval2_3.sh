#!/bin/bash
export TZ=Asia/Shanghai
export CUDA_VISIBLE_DEVICES=5
cd /home/chenzw/mydarts-rnn/rnn

python train.py --arch s2_3 --save eval2_3