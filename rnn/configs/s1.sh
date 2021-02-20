#!/bin/bash
export TZ=Asia/Shanghai
export CUDA_VISIBLE_DEVICES=1
cd /home/chenzw/mydarts-rnn/rnn

python train_search.py --unrolled --save s1 --seed 1