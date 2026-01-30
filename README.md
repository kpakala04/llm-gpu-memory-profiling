## Setup
This project assumes there is a similar install and setup of vllm and supporting packages as in [assignment 2](https://github.com/EricDinging/CS5470/blob/main/assignment_2/README.md). 

### Downloading ShareGPT Dataset
We use the following ShareGPT dataset for our experiments: Dans-DiscountModels/ConversationChronicles-sharegpt. Download this dataset using the following command:
```bash
python download_dataset.py
```

### The Scheduler
We use a CFS scheduler for our experiments. Copy `scheduler.py` to the vLLM directory to replace the `scheduler.py` file at `vllm/vllm/core/scheduler.py`. This scheduler prioritizes requests based on generated token length, checking to preempt at every iteration of the scheduler. 

### The Models
The models are expected to be downloaded from HuggingFace. Then using the templates in `server.sh` and `client.sh`, run the server and client scripts to start the benchmark on the desired model with the ShareGPT dataset.

Execute `burst_client.sh` to utilize the traffic pattern provided by the BurstGPT dataset. For example, `./burst_client.sh 26 1500 ./burstgpt_dataset.csv` to send 1500 total prompts at a base rate of 26 requests per second.

To use `mistralai/Mixtral-8x7B-v0.1` with the vLLM version specified in Assignment 2, copy the provided `fp8_utils.py` file into `vllm/vllm/model_executor/layers/quantization/utils/` and copy `fused_moe.py` into `vllm/vllm/model_executor/layers/fused_moe/`.

### Configuring the Client
The request rate and the number of prompts can be configured in the `client.sh` script via command line arguments. 

### Running experiments. 
Run the `server.sh` file to start the server. After the server is running, run the `client.sh` file to start benchmarking. 

## Using SGLang 
Follow the instructions in the [sglang branch README](https://github.coecis.cornell.edu/rgl78/cs5470final/blob/sglang/sglang_tests/README.md) to setup SGLang. Then using the templates in `sglang_server_cfs.sh` and `sglang_client.sh`, run the server and client scripts to start the benchmark on the desired model with the ShareGPT dataset. 
```bash
git checkout sglang
cd sglang_tests
```
