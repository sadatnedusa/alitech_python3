# VLC Playlist Generator

A Python script that scans a specified directory and its subdirectories for `.mp4` files and generates VLC-compatible playlist files (`.xspf`) in each folder.

## Problem Statement

Creating a VLC playlist manually can be time-consuming when there are many `.mp4` files distributed across multiple folders. This project automates the process, allowing users to quickly generate playlists for all `.mp4` files within a directory and its subdirectories.

## Solution

This script recursively scans the given directory and generates a VLC-compatible `.xspf` playlist in each subdirectory containing `.mp4` files. The playlist is created with properly encoded file paths to ensure VLC can read them, even with special characters.

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
