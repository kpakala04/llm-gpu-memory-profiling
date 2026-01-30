#!/bin/bash

REQUEST_RATE=${1:-10}
NUM_PROMPTS=${2:-500}

echo "Running SGLang CFS benchmark with request_rate=$REQUEST_RATE, num_prompts=$NUM_PROMPTS"

python3 bench_serving.py \
    --backend sglang \
    --model mistralai/Mixtral-8x7B-v0.1 \
    --base-url http://127.0.0.1:30000 \
    --request-rate $REQUEST_RATE \
    --num-prompts $NUM_PROMPTS \
    --dataset-name sharegpt\
    --dataset-path ../sharegpt_dataset.json \

    #--trust-remote-code
    # --dataset-path ../sharegpt_dataset.json \
    # --random-input 256 \
    # --random-output 512 \
    # --random-range-ratio 1.0 \
