#!/bin/bash


REQUEST_RATE=${1:-5}
NUM_PROMPTS=${2:-100}

echo "Running benchmark with request_rate=$REQUEST_RATE, num_prompts=$NUM_PROMPTS"

# --model Qwen/Qwen3-32B \
# --model deepseek-ai/deepseek-coder-33b-instruct \
# --model mistralai/Mixtral-8x7B-v0.1 \


python3 benchmark.py \
    --backend openai \
    --model nvidia/Llama-3_3-Nemotron-Super-49B-v1 \
    --request-rate $REQUEST_RATE \
    --num-prompts $NUM_PROMPTS \
    --dataset-name sharegpt \
    --dataset-path ./sharegpt_dataset.json \
    --trust-remote-code \