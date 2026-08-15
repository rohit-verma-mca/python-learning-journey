"""
Question:
Write a program that takes a folder of PDF files and a password, then
encrypts every PDF in that folder with that password, saving the
encrypted versions to a new folder.

"""

import os
from pypdf import PdfReader, PdfWriter


def encrypt_pdfs(source_folder, destination_folder, password):
    os.makedirs(destination_folder, exist_ok=True)
    encrypted_count = 0

    for filename in os.listdir(source_folder):
        if filename.lower().endswith(".pdf"):
            source_path = os.path.join(source_folder, filename)

            reader = PdfReader(source_path)
            writer = PdfWriter()

            for page in reader.pages:
                writer.add_page(page)

            writer.encrypt(password)

            dest_path = os.path.join(destination_folder, filename)
            with open(dest_path, "wb") as f:
                writer.write(f)

            print(f"Encrypted: {filename}")
            encrypted_count += 1

    print(f"\nDone. {encrypted_count} PDF(s) encrypted and saved to '{destination_folder}'.")


if __name__ == "__main__":
    encrypt_pdfs(source_folder="pdf_test_folder", destination_folder="pdf_encrypted", password="secret123")