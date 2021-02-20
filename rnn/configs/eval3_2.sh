#!/bin/bash
export TZ=Asia/Shanghai
export CUDA_VISIBLE_DEVICES=3
cd /home/chenzw/mydarts-rnn/rnn

python train.py --arch s3_2 --save eval3_2