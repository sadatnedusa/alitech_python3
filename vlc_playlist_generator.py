import os
import xml.etree.ElementTree as ET
from urllib.parse import quote

def create_vlc_playlist(directory_path, playlist_name="playlist.xspf"):
    # Traverse directory and subdirectories
    for root, _, files in os.walk(directory_path):
        # Filter .mp4 files in the current directory, skip hidden files
        mp4_files = [f for f in files if f.endswith(".mp4") and not f.startswith("._")]
        
        if not mp4_files:
            # Skip if there are no .mp4 files in the current directory
            continue
        
        # Initialize XML structure for the VLC playlist
        playlist = ET.Element("playlist", attrib={"xmlns": "http://xspf.org/ns/0/", "version": "1"})
        title = ET.SubElement(playlist, "title")
        title.text = "VLC Playlist"

        trackList = ET.SubElement(playlist, "trackList")
        
        # Add each .mp4 file as a track in the playlist
        for filename in mp4_files:
            file_path = os.path.join(root, filename)
            encoded_path = quote(file_path.replace("\\", "/"))

            track = ET.SubElement(trackList, "track")
            location = ET.SubElement(track, "location")
            location.text = "file:///" + encoded_path
            title = ET.SubElement(track, "title")
            title.text = filename

        # Define the playlist path in the current subdirectory
        playlist_path = os.path.join(root, playlist_name)
        
        # Create the XML tree and write it to an .xspf file
        tree = ET.ElementTree(playlist)
        with open(playlist_path, "wb") as f:
            tree.write(f, encoding="utf-8", xml_declaration=True)
        
        print(f"Playlist '{playlist_name}' created in '{root}' with {len(mp4_files)} .mp4 files.")

# Usage example
directory_path = "F:/Network_Troubleshooting_and_Tools"  # Replace with the top-level directory path
create_vlc_playlist(directory_path)
