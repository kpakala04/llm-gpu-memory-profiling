REQUEST_RATE=${1:-5}

NUM_PROMPTS=${2:-100}

BURSTGPT_TRACE=${3:-""}



echo "Running benchmark with request_rate=$REQUEST_RATE, num_prompts=$NUM_PROMPTS"



python3 benchmark.py \

CMD="python3 benchmark.py \
    --backend openai \
    --model nvidia/Llama-3_3-Nemotron-Super-49B-v1 \
    --request-rate $REQUEST_RATE \
    --num-prompts $NUM_PROMPTS \
    --dataset-name sharegpt \
    --dataset-path ./sharegpt_dataset.json \
    --trust-remote-code"

if [ -n "$BURSTGPT_TRACE" ]; then

    CMD="$CMD --burstgpt-trace-path $BURSTGPT_TRACE"

    echo "Using BurstGPT trace: $BURSTGPT_TRACE"

fi

eval $CMD
