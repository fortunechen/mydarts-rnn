#!/bin/bash
export TZ=Asia/Shanghai
export CUDA_VISIBLE_DEVICES=3
cd /home/chenzw/mydarts-rnn/rnn

python train_search.py --unrolled --save s3 --seed 3