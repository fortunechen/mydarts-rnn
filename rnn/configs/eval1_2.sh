#!/bin/bash
export TZ=Asia/Shanghai
export CUDA_VISIBLE_DEVICES=1
cd /home/chenzw/mydarts-rnn/rnn

python train.py --arch s1_2 --save eval1_2