#!/bin/bash
export TZ=Asia/Shanghai
export CUDA_VISIBLE_DEVICES=7
cd /home/chenzw/mydarts-rnn/rnn

python train.py --arch s3_3 --save eval3_3