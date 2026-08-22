from datasets import load_dataset

# Load a CHILDES dataset (VanHouten corpus)
dataset = load_dataset('chunksin/CHILDES', 'VanHouten', split='train')

# Filter for English utterances
english_utts = dataset.filter(lambda x: x['language'] == 'eng')

# Save to a text file
with open('childes_dumb.txt', 'w', encoding='utf-8') as f:
    for item in english_utts:
        f.write(item['gloss'] + '\n')

print(f"Saved {len(english_utts)} utterances to childes_dumb.txt")
