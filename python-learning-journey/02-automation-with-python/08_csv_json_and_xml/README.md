# CSV, JSON & XML Files

**Source:** Book Ch.18

## Concepts covered
- The `csv` module: `csv.reader()`, `csv.writer()`, `csv.DictReader()`, `csv.DictWriter()`
- Reading and writing CSV files with headers
- The `json` module: `json.load()`, `json.dump()`, `json.loads()`, `json.dumps()`
- Converting between Python dictionaries/lists and JSON
- Basic XML parsing with `xml.etree.ElementTree`

## My Notes
CSV and JSON are both just text formats for structured data — CSV is rows and columns
(like a spreadsheet), JSON is nested key-value pairs (like a Python dict). `DictReader`
is more convenient than plain `csv.reader()` since it gives you each row as a dictionary
using the header row as keys, instead of a plain list you have to index by position.
`json.dumps()` turns a Python object into a JSON string; `json.loads()` does the
reverse — easy to mix up which direction is which.

## Notable Practice Projects (from the book)
- **Excel-to-CSV Converter** — convert every sheet of a workbook into a separate CSV file

## Practice Questions
| # | Question | Status |
|---|----------|--------|
| 1 | Excel-to-CSV Converter | ⬜ |
| 2 | JSON Contact Book | ⬜ |

> Solved questions go in `exercises/` as `qXX_short_description.py`, following the format in [`EXERCISE_FORMAT.md`](../../EXERCISE_FORMAT.md).