from datasets import load_dataset

print("Loading ELI5 dataset... This may take a few minutes to download (~1.5GB).")
dataset = load_dataset('eli5', split='train_eli5')
print(f"Loaded {len(dataset)} questions.")

print("Saving to eli5_dumb.txt...")
with open('eli5_dumb.txt', 'w', encoding='utf-8') as f:
    for i, item in enumerate(dataset):
        question = item['title']
        # There can be multiple answers; we take the first one (it's usually the top-voted)
        answer = item['answers']['text'][0] if item['answers']['text'] else "No answer"
        f.write(f"Q: {question}\nA: {answer}\n\n")
        
        if (i + 1) % 5000 == 0:
            print(f"  Processed {i+1} entries...")

print("✅ Done! Saved to eli5_dumb.txt")
