# Project Structure

- Here's a simple project structure for this project:

```
vlc-playlist-generator
├── README.md
├── vlc_playlist_generator.py
└── .gitignore
```
---
## 2. Problem Statement

- Creating individual VLC playlists across multiple subdirectories for `.mp4` files can be tedious and time-consuming. 
- This project aims to automate the playlist creation process, generating `.xspf` files for each subdirectory containing `.mp4` files, complete with properly formatted paths for compatibility with VLC.

### 3. Pseudocode

```plaintext
1. Import necessary libraries (os, ElementTree, quote from urllib.parse).
2. Define the function `create_vlc_playlist`:
    a. Use `os.walk()` to scan the directory and subdirectories.
    b. For each subdirectory:
        i. Collect all `.mp4` files, excluding hidden files.
        ii. If `.mp4` files exist:
            - Create an XML structure for the VLC playlist.
            - Encode each file path.
            - Add each `.mp4` file as a track in the playlist.
            - Save the playlist as `playlist.xspf` in the subdirectory.
3. Run the function with a specified directory path.
```
---
## 4. How the program works

- Directory and Subdirectory Scanning: The program scans the specified directory and all its subdirectories.
- File Filtering: Only .mp4 files are considered, and hidden files are skipped.
- Playlist Creation:
-- A VLC-compatible playlist (.xspf file) is created for each subdirectory containing .mp4 files.
-- Each file path is URL-encoded to ensure VLC compatibility.
-- **Playlist Output**: The .xspf file is saved in the same folder as the video files, making it convenient for VLC playback.

---
# VLC Playlist Generator

A Python script that scans a specified directory and its subdirectories for `.mp4` files and generates VLC-compatible playlist files (`.xspf`) in each folder.

## Problem Statement

Creating a VLC playlist manually can be time-consuming when there are many `.mp4` files distributed across multiple folders. This project automates the process, allowing users to quickly generate playlists for all `.mp4` files within a directory and its subdirectories.

## Solution

- This script recursively scans the given directory and generates a VLC-compatible `.xspf` playlist in each subdirectory containing `.mp4` files. 
- The playlist is created with properly encoded file paths to ensure VLC can read them, even with special characters.

## Features

- Scans a directory and all its subdirectories for `.mp4` files.
- Generates an `.xspf` playlist in each subdirectory containing `.mp4` files.
- Automatically encodes file paths to avoid compatibility issues with VLC.
- Skips hidden files to prevent errors.

## Pseudocode

1. Import necessary libraries: `os`, `xml.etree.ElementTree`, and `urllib.parse`.
2. Define a function `create_vlc_playlist`:
   - Traverse the given directory recursively using `os.walk()`.
   - For each subdirectory:
     - Check for `.mp4` files, excluding hidden files.
     - If `.mp4` files are found:
       - Create XML structure for VLC playlist.
       - Encode file paths to ensure VLC compatibility.
       - Add each `.mp4` file to the playlist.
       - Write the playlist to a `.xspf` file in the current subdirectory.
3. Run the function with the specified directory path.

## How the Program Works

1. **Input**: The program takes a directory path as input. Replace `directory_path` with the path to the top-level directory containing `.mp4` files.
2. **Directory Scanning**: It scans all folders and subfolders for `.mp4` files.
3. **Playlist Generation**: For each folder with `.mp4` files, it generates an `.xspf` file with properly formatted paths.
4. **Output**: Each `.xspf` playlist file is saved in its respective subdirectory.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/vlc-playlist-generator.git
   cd vlc-playlist-generator

---

### Example
- Assume the directory structure is as follows:

```
media/
├── folder1/
│   ├── video1.mp4
│   └── video2.mp4
├── folder2/
│   └── video3.mp4
└── folder3/
    └── subfolder/
        └── video4.mp4
```
- After running the script, .xspf files will be generated in folder1, folder2, and folder3/subfolder.


### Requirements
- Python 3.x

