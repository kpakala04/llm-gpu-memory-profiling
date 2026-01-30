#!/usr/bin/env python3
"""Download ShareGPT and BurstGPT datasets from HuggingFace."""

from datasets import load_dataset
import json
import os
import subprocess
import argparse


def download_sharegpt():
    """Download and convert ShareGPT dataset to expected format."""
    print("Downloading ShareGPT dataset from HuggingFace...")
    
    # Load the dataset
    dataset = load_dataset("Dans-DiscountModels/ConversationChronicles-sharegpt", split="train")
    
    # Convert to the format expected by benchmark.py
    # Format: list of {"conversations": [{"value": "..."}, {"value": "..."}]}
    converted = []
    for item in dataset:
        if "conversations" in item:
            # Already in correct format
            converted.append(item)
        elif "messages" in item:
            # Convert from messages format
            conversations = [
                {"value": msg.get("content", msg.get("value", ""))}
                for msg in item["messages"]
            ]
            converted.append({"conversations": conversations})
    
    # Save to JSON file
    output_path = "sharegpt_dataset.json"
    with open(output_path, "w") as f:
        json.dump(converted, f)
    
    print(f"Dataset saved to {output_path}")
    print(f"Total conversations: {len(converted)}")
    
    return output_path


def download_burstgpt():
    """Download BurstGPT dataset from HuggingFace."""
    print("Downloading BurstGPT dataset from HuggingFace...")
    
    # URL for the raw file
    url = "https://huggingface.co/datasets/lzzmm/BurstGPT/resolve/main/data/BurstGPT_1.csv"
    output_path = "burstgpt_dataset.csv"
    
    print(f"Downloading from {url} to {output_path}...")
    try:
        subprocess.run(["wget", "-O", output_path, url], check=True)
        print(f"Dataset saved to {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading dataset: {e}")
        print(
            "Please try downloading manually: "
            "wget https://huggingface.co/datasets/lzzmm/BurstGPT/resolve/main/BurstGPT_1.csv "
            "-O burstgpt_dataset.csv"
        )
        raise

    return output_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download datasets for benchmarking.")
    parser.add_argument(
        "--dataset",
        type=str,
        choices=["sharegpt", "burstgpt", "all"],
        default="all",  # Changed default so both datasets download
        help="Which dataset to download (default: all)"
    )
    args = parser.parse_args()

    if args.dataset in ["sharegpt", "all"]:
        download_sharegpt()
    if args.dataset in ["burstgpt", "all"]:
        download_burstgpt()
