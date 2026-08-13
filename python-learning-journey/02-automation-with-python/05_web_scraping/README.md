# Web Scraping

**Source:** Book Ch.13

## Concepts covered
- The `requests` module for downloading web pages
- The `beautifulsoup4` module for parsing HTML
- Finding elements with `.select()` (CSS selectors) or `.find()` / `.find_all()`
- Following links across multiple pages
- Downloading files (images, etc.) from URLs
- Basic scraping etiquette — checking `robots.txt`, not hammering a server with requests

## My Notes
`requests.get(url)` downloads the raw HTML of a page; BeautifulSoup then turns that
raw text into a structure you can search through, like `soup.select('.comic img')` to
grab elements matching a CSS selector. A lot of scraping is really just "download page
→ find the piece I need → follow a link → repeat," which is why the XKCD downloader
project works as a loop rather than one-off code. Always add a small delay between
requests when scraping many pages, so you're not hitting the server too fast.

## Notable Practice Projects (from the book)
- **Project: Run a Program with the `webbrowser` Module** — open a map from a clipboard address
- **Project: Open All Search Results** — open the top PyPI search results in new tabs
- **Project: Download XKCD Comics** — follow "Prev" links to bulk-download a comic archive

## Practice Questions
| # | Question | Status |
|---|----------|--------|
| 1 | Download XKCD Comics | ⬜ |
| 2 | Broken Link Checker | ⬜ |

> Solved questions go in `exercises/` as `qXX_short_description.py`, following the format in [`EXERCISE_FORMAT.md`](../../EXERCISE_FORMAT.md).