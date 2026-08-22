"""
Question:
Write a program that takes a folder of images and resizes every one of
them to a fixed width, saving the resized versions to a new folder.

"""

import os
from PIL import Image


def resize_images(source_folder, destination_folder, target_width=800):
    os.makedirs(destination_folder, exist_ok=True)
    resized_count = 0

    valid_extensions = (".jpg", ".jpeg", ".png", ".bmp")

    for filename in os.listdir(source_folder):
        if filename.lower().endswith(valid_extensions):
            source_path = os.path.join(source_folder, filename)

            with Image.open(source_path) as img:
                width_percent = target_width / float(img.width)
                target_height = int(float(img.height) * width_percent)

                resized_img = img.resize((target_width, target_height))

                dest_path = os.path.join(destination_folder, filename)
                resized_img.save(dest_path)

            print(f"Resized: {filename} -> {target_width}x{target_height}")
            resized_count += 1

    print(f"\nDone. {resized_count} image(s) resized and saved to '{destination_folder}'.")


if __name__ == "__main__":
    resize_images(source_folder="test_images", destination_folder="resized_images", target_width=800)