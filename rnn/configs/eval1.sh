#!/bin/bash
export TZ=Asia/Shanghai
export CUDA_VISIBLE_DEVICES=0
cd /home/chenzw/mydarts-rnn/rnn

python train.py --arch s1_1 --save eval1_1