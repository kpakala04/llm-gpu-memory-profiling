#!/bin/bash

# Clear previous log
rm -f sglang_server.log

# Enable millisecond logging (like vLLM)
export SGLANG_LOG_MS=1

# ===== CACHE DIRECTORIES (persistent on $PSCRATCH) =====
# Flashinfer JIT cache (this is the key one!)
export FLASHINFER_WORKSPACE_BASE=$PSCRATCH/.cache/flashinfer

# TVM cache
export TVM_HOME=$PSCRATCH/.cache/tvm
export TVM_FFI_CACHE_DIR=$PSCRATCH/.cache/tvm-ffi

# Override HOME to prevent ~/.cache from being used

# General XDG cache
export XDG_CACHE_HOME=$PSCRATCH/.cache

# PyTorch extensions cache
export TORCH_EXTENSIONS_DIR=$PSCRATCH/.cache/torch_extensions

# Triton kernel cache
export TRITON_CACHE_DIR=$PSCRATCH/.cache/triton

# CUDA compilation cache
export CUDA_CACHE_PATH=$PSCRATCH/.cache/cuda

# Create all directories
mkdir -p $FLASHINFER_WORKSPACE_BASE $TVM_HOME $TVM_FFI_CACHE_DIR $XDG_CACHE_HOME $TORCH_EXTENSIONS_DIR $TRITON_CACHE_DIR $CUDA_CACHE_PATH

# Set custom logging configuration (equivalent to VLLM_LOGGING_CONFIG_PATH)
export SGLANG_LOGGING_CONFIG_PATH=./sglang_logging_config.json

CUDA_VISIBLE_DEVICES=0,1,2,3 \
python -m sglang.launch_server \
    --model-path mistralai/Mixtral-8x7B-v0.1 \
    --schedule-policy cfs\
    --enable-priority-scheduling \
    --schedule-low-priority-values-first \
    --priority-scheduling-preemption-threshold 0 \
    --max-running-requests 2048 \
    --context-length 4096 \
    --enable-metrics \
    --tp 4 \
    --trust-remote-code \
    --disable-cuda-graph \
    --port 30000
    
# Optional CFS arguments (uncomment to enable):
# --enable-priority-scheduling \
# --priority-scheduling-preemption-threshold 0 \
# --enable-metrics \
# --max-total-tokens 8192 \

    # --enable-hierarchical-cache \
    # --hicache-ratio 2.0 \
    # --hicache-io-backend kernel\