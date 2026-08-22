import os
import re

input_dir = 'youtube_subs'
output_file = 'youtube_dumb.txt'

with open(output_file, 'w', encoding='utf-8') as outfile:
    for filename in os.listdir(input_dir):
        if filename.endswith('.vtt'):
            with open(os.path.join(input_dir, filename), 'r', encoding='utf-8') as infile:
                content = infile.read()
                # Remove WEBVTT header and timestamp lines
                clean = re.sub(r'WEBVTT.*?\n', '', content, flags=re.DOTALL)
                clean = re.sub(r'\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}.*?\n', '', clean)
                # Remove cue index numbers (lines with only digits)
                clean = re.sub(r'^\d+$', '', clean, flags=re.MULTILINE)
                # Collapse multiple newlines
                clean = re.sub(r'\n\s*\n', '\n', clean).strip()
                outfile.write(clean + '\n\n')
                print(f"Cleaned {filename}")

print(f"All subtitles saved to {output_file}")
