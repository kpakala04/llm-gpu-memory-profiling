#!/usr/bin/env python3
"""Download ShareGPT dataset from HuggingFace."""

from datasets import load_dataset
import json
import os

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
            conversations = [{"value": msg.get("content", msg.get("value", ""))} 
                           for msg in item["messages"]]
            converted.append({"conversations": conversations})
    
    # Save to JSON file
    output_path = "sharegpt_dataset.json"
    with open(output_path, "w") as f:
        json.dump(converted, f)
    
    print(f"Dataset saved to {output_path}")
    print(f"Total conversations: {len(converted)}")
    
    return output_path

if __name__ == "__main__":
    download_sharegpt()