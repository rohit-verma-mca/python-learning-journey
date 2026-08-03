# Strings & Text Editing

**Source:** Video tutorial + Book Ch.8 (Strings and Text Editing)

## Concepts covered
- String indexing and slicing
- String methods: `.upper()`, `.lower()`, `.strip()`, `.split()`, `.join()`, `.replace()`, `.startswith()`, `.endswith()`
- f-strings and `.format()`
- Escape characters (`\n`, `\t`, `\'`, `\"`)
- Multiline strings with triple quotes
- Checking string content: `.isalpha()`, `.isdigit()`, `.isspace()`

## My Notes
Strings are immutable in Python — methods like `.upper()` or `.replace()` don't change
the original string, they return a new one, so you have to assign the result back to a
variable if you want to keep it. `.split()` and `.join()` are opposites of each other —
one breaks a string into a list, the other combines a list back into a string.

## Practice Questions
| # | Question | Status |
|---|----------|--------|
| 1 | Table Printer | ⬜ |
| 2 | Sentence Reverser | ⬜ |

> Solved questions go in `exercises/` as `qXX_short_description.py`, following the format in [`EXERCISE_FORMAT.md`](../../EXERCISE_FORMAT.md).