# PDF & Word Documents

**Source:** Book Ch.17

## Concepts covered
- The `PyPDF2` (or `pypdf`) module for reading/writing PDFs
- Extracting text from PDF pages
- Merging and encrypting/decrypting PDFs
- The `python-docx` module for reading/writing Word documents
- Adding paragraphs, headings, and basic formatting to a `.docx` file

## My Notes
`PyPDF2` treats a PDF as a list of pages you can loop through — `.extract_text()` pulls
readable text out of each page, though formatting/tables often come out messy since
PDFs aren't really structured text. Encrypting a PDF with `PdfWriter.encrypt(password)`
locks it so it can't be opened without that password, useful for batch-protecting
sensitive files. `python-docx` works similarly to openpyxl — build up a `Document()`
object with paragraphs/headings, then `.save()` it as a real `.docx` file.

## Practice Questions
| # | Question | Status |
|---|----------|--------|
| 1 | PDF Paranoia | ⬜ |
| 2 | Custom Invitations as Word Documents | ⬜ |

> Solved questions go in `exercises/` as `qXX_short_description.py`, following the format in [`EXERCISE_FORMAT.md`](../../EXERCISE_FORMAT.md).