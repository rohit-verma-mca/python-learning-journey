"""
Question:
Walk through a folder and find files above a certain size (or matching
a certain extension, like .tmp or .log) and delete them - print what
was deleted as you go.

"""

import os

TEST_MODE = True  # keep True while testing - only prints, never actually deletes


def delete_unneeded_files(folder, extension=".tmp", min_size_bytes=0):
    deleted_files = []

    for folder_path, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            file_path = os.path.join(folder_path, filename)
            matches_extension = filename.lower().endswith(extension.lower())
            file_size = os.path.getsize(file_path)

            if matches_extension and file_size >= min_size_bytes:
                if TEST_MODE:
                    print(f"[TEST MODE] Would delete: {file_path} ({file_size} bytes)")
                else:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                deleted_files.append(file_path)

    print(f"\n{len(deleted_files)} file(s) matched and processed.")
    return deleted_files


if __name__ == "__main__":
    # Test on a throwaway folder first, not a real one
    delete_unneeded_files(folder="test_folder", extension=".tmp", min_size_bytes=0)