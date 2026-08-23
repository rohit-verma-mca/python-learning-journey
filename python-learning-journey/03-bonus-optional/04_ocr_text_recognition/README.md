# Recognizing Text in Images (OCR)

**Source:** Book Ch.22

## Concepts covered
- OCR (Optical Character Recognition) — what it is and its limitations
- The `pytesseract` module (a Python wrapper around Google's Tesseract OCR engine)
- Installing Tesseract itself (separate from the Python package)
- Extracting text from an image file
- Image preprocessing (grayscale, thresholding) to improve OCR accuracy

## My Notes
OCR reads text out of an image the way a human would visually read it — useful for
scanned documents, screenshots, or photos of printed text where you don't have the
underlying text data. `pytesseract` is just a Python wrapper — the actual OCR engine
(Tesseract) is a separate program that has to be installed on the computer itself, not
just `pip install`ed. OCR accuracy depends heavily on image quality — clean, high-contrast
text works well; blurry or handwritten text often doesn't.

## Practice Questions
| # | Question | Status |
|---|----------|--------|
| 1 | Extract Text from a Screenshot | ⬜ |

> Solved questions go in `exercises/` as `qXX_short_description.py`, following the format in [`EXERCISE_FORMAT.md`](../../EXERCISE_FORMAT.md).