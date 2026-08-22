from datasets import load_dataset

print("Loading Yahoo! Answers... This may take a minute to download (~300MB).")

# Load the main training split
dataset = load_dataset('yahoo_answers_qa', split='train')

print(f"Dataset loaded! Total entries: {len(dataset)}")
print("Saving to yahoo_answers_dumb.txt...")

with open('yahoo_answers_dumb.txt', 'w', encoding='utf-8') as f:
    for i, item in enumerate(dataset):
        # Combine question and the best answer
        question = item['question']
        answer = item['answer']
        
        # Write it in a simple Q&A format
        f.write(f"Q: {question}\nA: {answer}\n\n")
        
        # Show progress every 10,000 entries
        if (i + 1) % 10000 == 0:
            print(f"  Processed {i+1} entries...")

print("✅ Done! Saved to yahoo_answers_dumb.txt")
