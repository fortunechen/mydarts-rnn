#!/bin/bash
export TZ=Asia/Shanghai
export CUDA_VISIBLE_DEVICES=4
cd /home/chenzw/mydarts-rnn/rnn

python train.py --arch s1_3 --save eval1_3