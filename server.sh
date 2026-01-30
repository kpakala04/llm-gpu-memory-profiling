#!/bin/bash

# Clear previous log
rm -f vllm_server.log

CUDA_VISIBLE_DEVICES=0,1 \
VLLM_USE_V1=0 \
VLLM_LOGGING_CONFIG_PATH=./logging_config.json \
python3 -m vllm.entrypoints.openai.api_server \
    --model Qwen/Qwen3-32B \
    --swap-space 16 \
    --enforce-eager \
    --max-num-seqs 256 \
    --preemption-mode swap \
    --tensor-parallel-size 2 \
    --trust-remote-code \
    --max_model_len 8192

