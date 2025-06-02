import os
import subprocess

# Set base Steam userdata path
base_path = r"C:\Program Files (x86)\Steam\userdata"
target_subpath = os.path.join("gamerecordings", "video")

# Manual fallback Steam user ID (used if auto-detection fails)
manual_steam_id = "123456789"  # 🔁 <-- Replace this with your actual Steam user ID

steam_user_folder = ""

# Try to auto-detect a valid folder that is not /0/
for entry in os.listdir(base_path):
    if entry.isdigit():
        full_path = os.path.join(base_path, entry, target_subpath)
        if os.path.isdir(full_path) and not full_path.endswith("\\0\\"):
            steam_user_folder = entry
            break  # Just pick the first valid one

# Use manual ID if auto-detection failed
if not steam_user_folder:
    user_path = os.path.join(base_path, manual_steam_id, target_subpath)
    if os.path.isdir(user_path):
        steam_user_folder = manual_steam_id
    else:
        print("No valid folder found, and fallback ID is invalid. Exiting.")
        exit()

# Final path to use
video_dir = os.path.join(base_path, steam_user_folder, target_subpath)
print(f"Searching in: {video_dir}")

output_dir = 'M:/VIDEO/steam_background_recordings/'

# Loop over all subfolders like: bg_1903340_20250601_093500
for folder in os.listdir(video_dir):
    full_folder_path = os.path.join(video_dir, folder)
    if os.path.isdir(full_folder_path):
        session_mpd = os.path.join(full_folder_path, "session.mpd")
        if os.path.isfile(session_mpd):
            output_filename = f"{folder}.mp4"
            output_path = os.path.join(output_dir, output_filename)

            # Skip if output file already exists
            if os.path.isfile(output_path):
                print(f"Skipping: {output_filename} already exists.")
                continue

            print(f"Converting: {folder} -> {output_filename}")

            # Run ffmpeg command
            result = subprocess.run([
                "ffmpeg",
                "-y",
                "-i", session_mpd,
                "-c", "copy",
                output_path
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            if result.returncode == 0:
                print(f"Success: {output_filename}")
            else:
                print(f"Failed to convert {folder}: {result.stderr}")
