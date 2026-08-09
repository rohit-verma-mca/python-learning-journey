# Regular Expressions

**Source:** Book Ch.9

## Concepts covered
- The `re` module: `re.compile()`, `.search()`, `.findall()`
- Basic regex syntax: `\d`, `\w`, `\s`, `+`, `*`, `?`, `{}`
- Groups with `()`
- `|` for matching alternatives
- Greedy vs non-greedy matching
- `re.sub()` for find-and-replace

## My Notes
Regex lets you search for *patterns* in text instead of exact strings — `\d+` matches
one or more digits anywhere, without knowing the exact number in advance. Wrapping part
of a pattern in `()` creates a "group," which lets you pull out just that piece of the
match instead of the whole thing. `.findall()` returns every match in the text as a
list, while `.search()` just returns the first one.

## Notable Practice Projects (from the book)
- **Project: Extract Contact Information from Large Documents** — regex-scan clipboard text for phone numbers and emails using `pyperclip`
- **Practice: Strong Password Detection** — validate length, case mix, and digits with regex
- **Practice: Regex version of `strip()`** — reimplement the string method using pattern matching

## Practice Questions
| # | Question | Status |
|---|----------|--------|
| 1 | Strong Password Detection | ✅ |
| 2 | Extract Contact Information | ⬜ |

> Solved questions go in `exercises/` as `qXX_short_description.py`, following the format in [`EXERCISE_FORMAT.md`](../../EXERCISE_FORMAT.md).