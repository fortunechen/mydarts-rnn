#!/bin/bash
export TZ=Asia/Shanghai
export CUDA_VISIBLE_DEVICES=4
cd /home/chenzw/mydarts-rnn/rnn

python train_search.py --unrolled --save s4 --seed 4