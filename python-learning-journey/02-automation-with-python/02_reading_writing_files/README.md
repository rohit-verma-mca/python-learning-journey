# Reading & Writing Files

**Source:** Book Ch.10

## Concepts covered
- `open()`, file modes (`'r'`, `'w'`, `'a'`, `'r+'`)
- Reading files: `.read()`, `.readline()`, `.readlines()`
- Writing/appending to files
- Using `with open(...) as f:` (context managers) so files close automatically
- File paths: absolute vs relative, `os.path` basics
- Working with plain text files vs the `shelve` module for saving Python data

## My Notes
Always use `with open(...) as f:` instead of manually calling `.close()` — it
automatically closes the file even if an error happens partway through, so you never
leak open file handles. `'w'` mode wipes the file clean before writing, while `'a'`
appends to the end without deleting existing content — easy to mix these up and lose
data, so it's worth double-checking the mode before running anything.

## Practice Questions
| # | Question | Status |
|---|----------|--------|
| 1 | Extending the Multi-Clipboard | ⬜ |
| 2 | Simple To-Do List File Manager | ⬜ |

> Solved questions go in `exercises/` as `qXX_short_description.py`, following the format in [`EXERCISE_FORMAT.md`](../../EXERCISE_FORMAT.md).