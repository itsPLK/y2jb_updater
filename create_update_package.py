#!/usr/bin/env python3

import sys
import os
import zipfile

def get_file_size(filepath):
    try:
        # os.stat() returns a stat_result object, and st_size is the size in bytes
        return os.path.getsize(filepath)
    except OSError as e:
        print(f"Error accessing file {filepath}: {e}")
        return None

def create_package(source_dir):

    # Normalize the source directory path
    source_dir = os.path.normpath(source_dir)
    
    # Check if the directory exists
    if not os.path.isdir(source_dir):
        print(f"Error: Directory not found: {source_dir}")
        sys.exit(1)

    zip_name = f"y2jb_update.zip"

    file_list_for_zip = []  # Stores (full_path, relative_path)
    size_lines = []         # Stores "relative_path|file_size_bytes"

    print(f"Scanning directory: {source_dir} ...")

    for root, dirs, files in os.walk(source_dir, topdown=True):
        
        # EXCLUDE HIDDEN DIRECTORIES
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            # EXCLUDE HIDDEN FILES
            if file.startswith('.'):
                continue

            full_path = os.path.join(root, file)
            
            # This is the path as it should appear in the zip/info file
            relative_path = os.path.relpath(full_path, source_dir)
            
            relative_path_unix = relative_path.replace(os.sep, '/')

            file_size = get_file_size(full_path)
            
            if file_size is not None:
                file_list_for_zip.append((full_path, relative_path_unix))
                # Format: relative_path|size_in_bytes
                size_lines.append(f"{relative_path_unix}|{file_size}")

    size_lines.sort()
    info_content = "\n".join(size_lines)
    info_file_name = "update-info.txt"

    print(f"Found {len(file_list_for_zip)} files. Creating {zip_name}...")

    # --- Create the zip file ---
    try:
        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Add all the files from the directory
            for full_path, arcname in file_list_for_zip:
                zipf.write(full_path, arcname)
                
            # Add the generated update-info.txt
            zipf.writestr(info_file_name, info_content)

        print(f"\nSuccessfully created {zip_name}")
        print(f"Archive contains {len(file_list_for_zip)} files + {info_file_name}.")

    except IOError as e:
        print(f"Error writing zip file: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# --- Main execution ---
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <directory_to_zip>")
        print(f"- <directory_to_zip> is the path to the directory containing splash.html and other Y2JB files.")
        sys.exit(1)
        
    directory_to_zip = sys.argv[1]
    create_package(directory_to_zip)