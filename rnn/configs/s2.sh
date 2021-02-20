#!/bin/bash
export TZ=Asia/Shanghai
export CUDA_VISIBLE_DEVICES=2
cd /home/chenzw/mydarts-rnn/rnn

python train_search.py --unrolled --save s2 --seed 2