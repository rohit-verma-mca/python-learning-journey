# Organizing Files

**Source:** Book Ch.11

## Concepts covered
- The `os` and `shutil` modules
- Walking a folder tree with `os.walk()`
- Copying, moving, and renaming files: `shutil.copy()`, `shutil.move()`
- Creating/deleting folders: `os.makedirs()`, `os.remove()`, `shutil.rmtree()`
- Matching filenames with `glob` or plain string checks (e.g., `.endswith()`)
- Zipping and unzipping folders with the `zipfile` module

## My Notes
`os.walk()` is the key tool here — it goes through a folder and every subfolder inside
it automatically, giving you the current folder path, subfolders, and files at each
level, so you don't have to write your own recursive function. `shutil` handles the
higher-level file operations (copy/move/delete) that `os` alone doesn't cover directly.
Deleting with `shutil.rmtree()` is permanent — no recycle bin — so it's worth testing
scripts like this on a throwaway test folder first.

## Practice Questions
| # | Question | Status |
|---|----------|--------|
| 1 | Selective Copy | ⬜ |
| 2 | Deleting Unneeded Files | ⬜ |

> Solved questions go in `exercises/` as `qXX_short_description.py`, following the format in [`EXERCISE_FORMAT.md`](../../EXERCISE_FORMAT.md).