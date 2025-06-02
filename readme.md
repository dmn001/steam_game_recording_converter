# Steam Game Recording Converter

This Python script converts Steam game recordings saved in fragmented `.m4s` files with a `.mpd` manifest into a single `.mp4` video file using `ffmpeg`.

---

## Features

- Automatically detects your Steam userdata folder.
- Converts all Steam game recording sessions found in subfolders.
- Skips conversion if output `.mp4` file already exists to save time.
- Supports manual fallback to specify your Steam user ID if auto-detection fails.

---

## Prerequisites

- **Python 3.x** installed on your system.
- **ffmpeg** installed and added to your system PATH.  
  Download from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)

---

## Usage

1. Replace the `manual_steam_id` variable in the script with your Steam user ID if auto-detection does not work.

2. Run the script:

```bash
python steam_recordings_to_mp4.py
