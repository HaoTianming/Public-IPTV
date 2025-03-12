import sys
import os
import json
from urllib.parse import urlparse

def is_url(path):
    """Check if a string is a URL."""
    try:
        result = urlparse(path)
        return all([result.scheme, result.netloc])
    except:
        return False

def is_playlist_file(path):
    """Check if a file is a supported playlist format."""
    supported_extensions = ['.m3u8', '.m3u', '.pls', '.xspf']
    
    if is_url(path):
        # Check if URL ends with a supported extension
        return any(path.lower().endswith(ext) for ext in supported_extensions)
    else:
        return os.path.isfile(path) and any(path.lower().endswith(ext) for ext in supported_extensions)

def load_from_json(json_path):
    """Load playlist URLs from a JSON file."""
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        if isinstance(data, dict) and "Playlist URLs" in data:
            urls = data["Playlist URLs"]
            if isinstance(urls, list):
                return urls
            
        print(f"Invalid JSON format in {json_path}. Expected: {{ \"Playlist URLs\": [\"url1\", \"url2\", ...] }}")
        return []
    except Exception as e:
        print(f"Error loading JSON file {json_path}: {str(e)}")
        return []

def merge_playlists(output_path, input_paths):
    """Merge multiple playlists into a single playlist."""
    # Expand playlist sources - check for JSON files and process them
    expanded_paths = []
    for path in input_paths:
        if path.lower().endswith('.json'):
            print(f"Loading playlist URLs from JSON file: {path}")
            json_urls = load_from_json(path)
            expanded_paths.extend(json_urls)
            print(f"Added {len(json_urls)} URLs from {path}")
        else:
            expanded_paths.append(path)
    
    if not expanded_paths:
        print("No input playlists provided.")
        return False
    
    # Validate all input paths
    valid_paths = []
    for path in expanded_paths:
        if is_playlist_file(path) or (is_url(path) and not path.lower().endswith('.json')):
            valid_paths.append(path)
        else:
            print(f"Skipping invalid input: {path}")
    
    if not valid_paths:
        print("No valid playlist files found.")
        return False
    
    # Create output content with mandatory M3U header
    output_content = "#EXTM3U\n"
    
    # Process each input playlist
    for path in valid_paths:
        try:
            if is_url(path):
                import requests
                print(f"Downloading playlist from URL: {path}")
                response = requests.get(path, timeout=10)
                content = response.text
            else:
                print(f"Reading local playlist file: {path}")
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
            
            # Skip the first line if it's #EXTM3U
            lines = content.splitlines()
            start_idx = 1 if lines and lines[0].strip() == "#EXTM3U" else 0
            
            # Add all lines except the initial #EXTM3U
            playlist_content = "\n".join(lines[start_idx:])
            if playlist_content:
                output_content += playlist_content + "\n"
                
            print(f"Successfully processed: {path}")
        except Exception as e:
            print(f"Error processing {path}: {str(e)}")
    
    # Write the merged content to the output file
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(output_content)
        print(f"Successfully created merged playlist: {output_path}")
        return True
    except Exception as e:
        print(f"Error writing to output file: {str(e)}")
        return False

def main():
    """Main function to handle command line arguments."""
    if len(sys.argv) < 3:
        print("Usage: python mergeiptv.py output.m3u8 input1.m3u8 input2.m3u input3.json [input4.m3u ...]")
        print("Supported formats: .m3u8, .m3u, .pls, .xspf, and .json files containing playlist URLs")
        print("JSON format example: { \"Playlist URLs\": [\"url1\", \"url2\", ...] }")
        return
    
    output_path = sys.argv[1]
    input_paths = sys.argv[2:]
    
    print(f"Processing {len(input_paths)} source(s) to create {output_path}")
    merge_playlists(output_path, input_paths)

if __name__ == "__main__":
    main()
