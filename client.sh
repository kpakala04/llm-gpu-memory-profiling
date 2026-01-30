#!/bin/bash


REQUEST_RATE=${1:-5}
NUM_PROMPTS=${2:-100}

echo "Running benchmark with request_rate=$REQUEST_RATE, num_prompts=$NUM_PROMPTS"

python3 benchmark.py \
    --backend openai \
    --model Qwen/Qwen3-32B \
    --request-rate $REQUEST_RATE \
    --num-prompts $NUM_PROMPTS \
    --dataset-name sharegpt \
    --dataset-path ./sharegpt_dataset.json \
    --trust-remote-code
