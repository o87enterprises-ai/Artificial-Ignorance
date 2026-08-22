from datasets import load_dataset

print("Loading IKEA dataset from Hugging Face...")
dataset = load_dataset("tsazan/ikea-us-commercetxt", split="train")

print(f"Loaded {len(dataset)} products.")
print("Saving to ikea_dumb.txt...")

with open("ikea_dumb.txt", "w", encoding="utf-8") as f:
    for i, item in enumerate(dataset):
        # The dataset has a 'text' field with product info
        if "text" in item:
            f.write(item["text"] + "\n\n")
        if (i + 1) % 5000 == 0:
            print(f"  Processed {i+1} products...")

print("✅ Done! Saved to ikea_dumb.txt")
