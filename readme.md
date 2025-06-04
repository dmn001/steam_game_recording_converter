# Steam Game Recording Converter

This Python script converts Steam game recordings saved in fragmented `.m4s` files with a `.mpd` manifest into a single `.mp4` video file using `ffmpeg`.

---

## Features

- Automatically detects your Steam userdata folder.
- Converts all Steam game recording sessions found in subfolders.
- Skips conversion if output `.mp4` file already exists to save time.
- Detects and skips output files that were renamed but still start with the original session folder name. Allows renaming output files appending text without causing duplicate file output.
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
python convert_steam_recordings_to_mp4.py
```

3. Converted .mp4 files will be saved in the output_dir defined in the script (M:/VIDEO/steam_background_recordings/ by default). Rename as necessary.