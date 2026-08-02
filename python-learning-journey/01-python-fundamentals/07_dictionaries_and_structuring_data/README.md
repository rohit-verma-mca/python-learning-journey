# Dictionaries & Structuring Data

**Source:** Video tutorial + Book Ch.7 (Dictionaries and Structuring Data)

## Concepts covered
- Creating and accessing dictionaries (key-value pairs)
- `.keys()`, `.values()`, `.items()`
- `.get()` for safe access without a KeyError
- Checking membership with `in`
- Nested dictionaries and lists inside dictionaries
- Looping over a dictionary

## My Notes
Dictionaries store data as key-value pairs instead of by position like a list — so you
look things up by name instead of by index. `.get()` is safer than `dict[key]` because
it returns `None` (or a default you specify) instead of crashing if the key doesn't
exist. Nesting dictionaries and lists together lets you model more complex, real-world
data — like an inventory or a contact list — much more naturally than flat variables.

## Practice Questions
| # | Question | Status |
|---|----------|--------|
| 1 | Fantasy Game Inventory | ⬜ |
| 2 | List to Dictionary Function | ⬜ |

> Solved questions go in `exercises/` as `qXX_short_description.py`, following the format in [`EXERCISE_FORMAT.md`](../../EXERCISE_FORMAT.md).