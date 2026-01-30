from datasets import load_dataset

ds = load_dataset("Dans-DiscountModels/ConversationChronicles-sharegpt")

train = ds["train"]
train.to_json("/pscratch/sd/r/rm2346/sharegpt.jsonl", lines=True)

