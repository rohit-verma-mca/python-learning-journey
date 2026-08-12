# Designing & Deploying Command Line Programs

**Source:** Book Ch.12

## Concepts covered
- `sys.argv` for reading command-line arguments
- The `argparse` module for proper flags/options
- Exit codes with `sys.exit()`
- Printing usage/help messages
- Making a script runnable from anywhere (basics of shebang lines / running via `python script.py`)

## My Notes
`sys.argv` is a plain list of whatever was typed after `python script.py` on the command
line — `argv[0]` is always the script name itself. `argparse` is a big step up from
manually parsing `sys.argv`, since it automatically handles things like `--help`,
required vs optional arguments, and gives clear error messages if something's missing,
without me writing that logic by hand.

## Practice Questions
| # | Question | Status |
|---|----------|--------|
| 1 | Selective Copy as a CLI Tool | ⬜ |
| 2 | Word Counter CLI | ⬜ |

> Solved questions go in `exercises/` as `qXX_short_description.py`, following the format in [`EXERCISE_FORMAT.md`](../../EXERCISE_FORMAT.md).