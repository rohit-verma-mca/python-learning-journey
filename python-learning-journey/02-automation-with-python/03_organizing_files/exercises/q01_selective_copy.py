"""
Question:
Walk through a folder (and its subfolders) and copy only files matching
a certain pattern (e.g., all .pdf or .jpg files) into a new destination
folder, preserving filenames.

"""

import os
import shutil


def selective_copy(source_folder, destination_folder, extension=".pdf"):
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
    # Test on a throwaway folder first, not a real one
    selective_copy(source_folder="test_folder", destination_folder="test_folder_pdfs", extension=".pdf")