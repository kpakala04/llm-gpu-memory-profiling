#!/bin/bash

# Clear previous log
# rm -f vllm_server.log

# --model Qwen/Qwen3-32B \
# --model deepseek-ai/deepseek-coder-33b-instruct \
# --model mistralai/Mixtral-8x7B-v0.1 \


CUDA_VISIBLE_DEVICES=0,1,2,3 \
VLLM_USE_V1=0 \
VLLM_LOGGING_CONFIG_PATH=./logging_config2.json \
python3 -m vllm.entrypoints.openai.api_server \
    --model nvidia/Llama-3_3-Nemotron-Super-49B-v1 \
    --preemption-mode swap \
    --swap-space 16 \
    --enforce-eager \
    --max-num-seqs 2048 \
    --tensor-parallel-size 4 \
    --trust-remote-code \
    --max_model_len 4096