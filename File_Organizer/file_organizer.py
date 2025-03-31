import os
import shutil
import time
from pathlib import Path

def organize_files():
    source_folder = Path.home() / "Downloads"  # Change this to your desired source folder
    destination = {
        "jpg": "Image Folder",
        "jpeg": "Image Folder",
        "png": "Image Folder",
        "xlsx": "Excel Folder",
        "xls": "Excel Folder",
        "mp3": "MP3 Folder",
        "pdf": "PDF Folder"
    }
    
    for folder in set(destination.values()):
        dest_folder = source_folder / folder
        if not dest_folder.exists():
            dest_folder.mkdir()
            print(f"Created folder: {dest_folder}")
    
    for file in source_folder.iterdir():
        if file.is_file():
            ext = file.suffix[1:].lower()  # Get file extension without dot
            if ext in destination:
                dest_folder = source_folder / destination[ext]
                shutil.move(str(file), str(dest_folder / file.name))
                print(f"Moved: {file} -> {dest_folder / file.name}")

if __name__ == "__main__":
    time.sleep(300)  # Wait for 5 minutes after startup
    organize_files()
