import re
import sys

def find_max_gpu_kv_cache_usage(log_path: str) -> float:
    # Regex to capture "GPU KV cache usage: X%"
    pattern = re.compile(r"GPU KV cache usage:\s*([\d.]+)%")

    max_usage = 0.0

    with open(log_path, "r") as f:
        for line in f:
            match = pattern.search(line)
            if match:
                usage = float(match.group(1))
                max_usage = max(max_usage, usage)

    return max_usage


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python max_kv_cache_usage.py <log_file>")
        sys.exit(1)

    log_file = sys.argv[1]
    max_usage = find_max_gpu_kv_cache_usage(log_file)

    print(f"Max GPU KV cache usage: {max_usage:.2f}%")
