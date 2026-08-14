# Excel Spreadsheets

**Source:** Book Ch.14

## Concepts covered
- The `openpyxl` module: `load_workbook()`, `Workbook()`
- Reading cell values, rows, and columns
- Writing/updating cells and saving a workbook
- Working with multiple sheets
- Cell styling basics (fonts, formulas are read as text unless recalculated by Excel)

## My Notes
`openpyxl` treats a workbook like a Python object — `wb['Sheet1']['A1'].value` gets you
a specific cell's contents, and setting `.value =` on a cell then calling `wb.save()`
writes it back to the file. Rows and columns can be accessed by number (`cell(row=1,
column=1)`) or by letter/label (`['A1']`) — both point to the same cell, just different
ways of addressing it. This is one of the most directly useful automation skills, since
so much real business data still lives in spreadsheets.

## Notable Practice Projects (from the book)
- **Multiplication Table Maker** — generate an N×N multiplication table as a new spreadsheet
- **Text Files to Spreadsheet** — read data from multiple text files into one sheet

## Practice Questions
| # | Question | Status |
|---|----------|--------|
| 1 | Multiplication Table Maker | ⬜ |
| 2 | Update Spreadsheet Cells | ⬜ |

> Solved questions go in `exercises/` as `qXX_short_description.py`, following the format in [`EXERCISE_FORMAT.md`](../../EXERCISE_FORMAT.md).