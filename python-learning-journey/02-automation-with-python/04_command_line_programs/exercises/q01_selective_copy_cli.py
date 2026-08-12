"""
Question:
Take the Selective Copy script from Organizing Files and rewrite it to
accept the source folder, destination folder, and file extension as
command-line arguments using argparse, instead of hardcoding them.

"""

import os
import shutil
import argparse


def selective_copy(source_folder, destination_folder, extension):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    copied_files = []
    for folder_path, subfolders, filenames in os.walk(source_folder):
        for filename in filenames:
            if filename.lower().endswith(extension.lower()):
                source_path = os.path.join(folder_path, filename)
                dest_path = os.path.join(destination_folder, filename)
                shutil.copy(source_path, dest_path)
                copied_files.append(filename)
                print(f"Copied: {filename}")

    print(f"\nDone. {len(copied_files)} file(s) copied to '{destination_folder}'.")
    return copied_files


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copy files with a given extension from one folder to another.")
    parser.add_argument("source", help="Source folder to search")
    parser.add_argument("destination", help="Destination folder to copy into")
    parser.add_argument("--ext", default=".pdf", help="File extension to match (default: .pdf)")

    args = parser.parse_args()
    selective_copy(args.source, args.destination, args.ext)

# Run like this from the terminal:
# python q01_selective_copy_cli.py test_folder test_folder_pdfs --ext .pdf