import yt_dlp
import os

# Read URLs from file
with open('video_urls.txt', 'r') as f:
    urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]

output_dir = 'youtube_subs'
os.makedirs(output_dir, exist_ok=True)

def download_subs(url):
    try:
        ydl_opts = {
            'skip_download': True,
            'writesubtitles': True,
            'writeautomaticsub': True,
            'subtitlesformat': 'vtt',
            'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
            'quiet': False,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"✅ Downloaded subs for: {url}")
    except Exception as e:
        print(f"❌ Failed for {url}: {e}")

for url in urls:
    download_subs(url)

print("All downloads attempted.")
