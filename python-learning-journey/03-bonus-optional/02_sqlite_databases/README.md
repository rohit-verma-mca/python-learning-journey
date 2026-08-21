# SQLite Databases

**Source:** Book Ch.16

## Concepts covered
- The `sqlite3` module (built into Python, no install needed)
- Creating a database file and connecting to it
- Creating tables with SQL (`CREATE TABLE`)
- Inserting, reading, updating, and deleting rows (`INSERT`, `SELECT`, `UPDATE`, `DELETE`)
- Using `?` placeholders to safely insert values (avoiding SQL injection)
- Committing changes with `.commit()`

## My Notes
SQLite stores an entire database as a single file on disk — no server setup needed,
which makes it perfect for small scripts and learning SQL basics. You write real SQL
strings and pass them to `.execute()`, using `?` placeholders instead of directly
inserting Python variables into the SQL string — this matters for security, since
building SQL strings by hand with f-strings is how SQL injection vulnerabilities happen.
Changes aren't saved to the file until you call `.commit()`.

## Practice Questions
| # | Question | Status |
|---|----------|--------|
| 1 | Student Records Database | ⬜ |
| 2 | Simple Task Tracker with SQLite | ⬜ |

> Solved questions go in `exercises/` as `qXX_short_description.py`, following the format in [`EXERCISE_FORMAT.md`](../../EXERCISE_FORMAT.md).