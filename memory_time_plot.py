import re
from datetime import datetime
import matplotlib.pyplot as plt
import argparse
import math

# --------------------------
# Parse command-line arguments
# --------------------------
parser = argparse.ArgumentParser(description="Plot GPU KV cache usage over time from vLLM logs.")
parser.add_argument(
    "log_file",
    type=str,
    help="Path to the vLLM log file"
)
parser.add_argument(
    "--output",
    type=str,
    default="gpu_kv_cache_usage.png",
    help="Output image file name (default: gpu_kv_cache_usage.png)"
)
parser.add_argument(
    "--tick_interval",
    type=int,
    default=30,
    help="X-axis tick interval in seconds (default: 30s)"
)
args = parser.parse_args()

log_file = args.log_file
output_file = args.output
tick_interval = args.tick_interval
max_duration = 120  # seconds

# --------------------------
# Extract timestamps and GPU KV cache usage
# --------------------------
timestamps = []
gpu_usage = []

pattern = re.compile(
    r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d+) - .*GPU KV cache usage: (?P<gpu>\d+\.?\d*)%'
)

with open(log_file, "r") as f:
    for line in f:
        match = pattern.search(line)
        if match:
            ts_str = match.group("timestamp")
            gpu_val = float(match.group("gpu"))

            ts = datetime.strptime(ts_str, "%Y-%m-%d %H:%M:%S,%f")
            timestamps.append(ts)
            gpu_usage.append(gpu_val)

if not timestamps:
    raise ValueError("No GPU KV cache usage entries found in the log file.")

# Convert timestamps to seconds since first benchmark entry
start_time = timestamps[0]
time_sec = [(ts - start_time).total_seconds() for ts in timestamps]

# --------------------------
# Filter points after max_duration
# --------------------------
filtered_time = []
filtered_gpu = []

for t, g in zip(time_sec, gpu_usage):
    if t < max_duration:
        filtered_time.append(t)
        filtered_gpu.append(g)

print(filtered_time)
print(filtered_gpu)

# --------------------------
# Plot
# --------------------------
plt.figure(figsize=(12, 6))
plt.plot(filtered_time, filtered_gpu, marker='o', linestyle='-')
plt.xlabel("Time (s)")
plt.ylabel("GPU KV Cache Usage (%)")
plt.title(f"GPU KV Cache Usage Over Time (first {max_duration} seconds)")
plt.grid(True)

# Set x-axis ticks every tick_interval seconds
plt.xticks(range(0, max_duration + tick_interval, tick_interval))

plt.tight_layout()
plt.savefig(output_file, dpi=300)
print(f"Plot saved to {output_file}")
