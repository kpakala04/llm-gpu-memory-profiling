# Setting up SGLang

## 1. Clone the SGLang repository
Clone the SGLang repository from GitHub:
```bash
git clone https://github.com/sglang/sglang.git
```
It should be in your $PSCRATCH directory.

## 2. Pip install SGLang from source
```bash
cd sglang
pip install -e "python[all]"
```
## 3. Pip install torch-c-dlpack-ext
```bash
pip install torch-c-dlpack-ext
```
## 4. Copy SGLang files 
Move/copy the files from this repo into the sglang directory:

sglang/python/sglang/srt/managers/schedule_policy.py 

sglang/python/sglang/srt/managers/scheduler.py 

sglang/python/sglang/srt/server_args.py

## 5. When using CFS
Load the following module:
```bash
module load cudatoolkit/12.9
```
## Key differences
1. This implementation attempts to use heirarchal caching. HiCache is used to simulate vllm's behavior of ofloading KV cache to CPU when preempted. There is no "swapped" queue in SGLang's scheduler. Unfortunately, this is not correctly implemented so request's kv cache are recomputed when the request is resumed.
2. Current implementation only supports preempting a single request at a time, unlike vllm's behavior of preempting until there is no priority inversion. I couldn't get preempting multiple requests to work without the scheduler hanging/slowing down significantly.


## Running experiments
Download the ShareGPT dataset with 
```bash 
python download_dataset.py
```
Then run the server and client scripts in a similar fashion to the main README.
```bash
./sglang_tests/sglang_server_cfs.sh
./sglang_tests/sglang_client.sh
```

## Configuring the client
The request rate and number of prompts can be configured in the `sglang_tests/sglang_client.sh` script at the top of the file. 


## Notes
1. Preemption only occurs every 10 iterations. (scheduler.py line 1832)
2. The server files set the caches to be in the $PSCRATCH directory. This is because the default home directory has issues with locking/unlocking.
