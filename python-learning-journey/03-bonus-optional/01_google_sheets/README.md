# Google Sheets

**Source:** Book Ch.15

## Concepts covered
- Google Cloud project setup + enabling the Sheets API
- Service account credentials (JSON key file) vs OAuth
- The `gspread` module for a simpler Python interface to Sheets
- Reading and writing cell values/ranges
- Sharing a spreadsheet with a service account's email so it can access it

## My Notes
Unlike openpyxl (which works on local files), Google Sheets needs actual API
credentials since it's talking to a live Google account over the internet. A "service
account" acts like a robot user — you create one in Google Cloud Console, download its
JSON key, and then share your specific spreadsheet with that service account's email
address (just like sharing it with a person) so it's allowed to read/write it.

## Practice Questions
| # | Question | Status |
|---|----------|--------|
| 1 | Read & Update a Google Sheet | ⬜ |

> Solved questions go in `exercises/` as `qXX_short_description.py`, following the format in [`EXERCISE_FORMAT.md`](../../EXERCISE_FORMAT.md).