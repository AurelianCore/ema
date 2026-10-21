import os
import yt_dlp

PLAYLIST_URL = "https://youtube.com/playlist?list=PLZTgvQHkvuFE&si=kLYvTRapFvD7aVnr"
OUTPUT_DIR = "music/general"

os.makedirs(OUTPUT_DIR, exist_ok=True)

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': os.path.join(OUTPUT_DIR, '%(title)s.%(ext)s'),
    'ignoreerrors': True,
}

print("Starting playlist download...")

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([PLAYLIST_URL])

print("Download complete!")