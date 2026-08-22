# Graphs & Manipulating Images

**Source:** Book Ch.21

## Concepts covered
- The `matplotlib` module for basic charts/graphs
- The `Pillow` (PIL) module for opening, editing, and saving images
- Cropping, resizing, and rotating images
- Adding text or shapes onto an image
- Basic color/pixel manipulation

## My Notes
`matplotlib` is mainly for plotting data (line charts, bar charts) rather than editing
photos — good for visualizing results from other scripts, like a chart of the Coin Flip
Streaks results. `Pillow` is the actual image-editing library — `Image.open()` loads a
picture as an object you can `.resize()`, `.rotate()`, `.crop()`, or draw on top of, then
`.save()` back to a file. Both are "read a file, transform it, produce a new file" — the
same automation pattern as PDFs and spreadsheets, just for a different file type.

## Practice Questions
| # | Question | Status |
|---|----------|--------|
| 1 | Bulk Image Resizer | ⬜ |
| 2 | Chart the Coin Flip Streaks Results | ⬜ |

> Solved questions go in `exercises/` as `qXX_short_description.py`, following the format in [`EXERCISE_FORMAT.md`](../../EXERCISE_FORMAT.md).