"""
Question:
Write a program that extracts and prints readable text from an image
file using OCR (Optical Character Recognition).

"""

import pytesseract
from PIL import Image

# Tell pytesseract where Tesseract is installed on this computer
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text


if __name__ == "__main__":
    extracted = extract_text("sample_text.png")
    print("Extracted text:")
    print(extracted)