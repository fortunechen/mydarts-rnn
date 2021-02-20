#!/bin/bash
export TZ=Asia/Shanghai
export CUDA_VISIBLE_DEVICES=0
cd /home/chenzw/mydarts-rnn/rnn

python train.py --arch s4_1 --save eval4_1