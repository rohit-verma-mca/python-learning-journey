"""
Question:
Given a URL, download the page, find every link on it, and check each
one to report which links are broken (return an error status) vs
working.

Topic     : Web Scraping
Source    : Automate the Boring Stuff with Python - Ch.13 ("Broken Link Checker")
Difficulty: Medium
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def check_links(page_url, max_links=20):
    response = requests.get(page_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all("a", href=True)

    working = []
    broken = []

    for link in links[:max_links]:
        full_url = urljoin(page_url, link["href"])
        try:
            link_response = requests.head(full_url, timeout=5, allow_redirects=True)
            if link_response.status_code < 400:
                working.append(full_url)
            else:
                broken.append((full_url, link_response.status_code))
        except requests.RequestException as e:
            broken.append((full_url, str(e)))

    print(f"Checked {len(working) + len(broken)} link(s) on {page_url}\n")

    print(f"Working links: {len(working)}")
    print(f"Broken links: {len(broken)}")
    for url, reason in broken:
        print(f"  BROKEN: {url}  ({reason})")

    return working, broken


if __name__ == "__main__":
    check_links("https://xkcd.com", max_links=15)