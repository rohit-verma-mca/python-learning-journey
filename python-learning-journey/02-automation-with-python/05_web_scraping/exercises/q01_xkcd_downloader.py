"""
Question:
Starting from the homepage of a webcomic site (xkcd.com), download the
comic image, then follow the "Prev" link repeatedly to keep downloading
every past comic until you reach the first one (or a set limit).

Topic     : Web Scraping
Source    : Automate the Boring Stuff with Python - Ch.13 Project ("Download XKCD Comics")
Difficulty: Medium
"""

import os
import requests
from bs4 import BeautifulSoup


def download_xkcd_comics(start_url="https://xkcd.com", max_comics=10, save_folder="xkcd_comics"):
    os.makedirs(save_folder, exist_ok=True)

    url = start_url
    downloaded = 0

    while url and downloaded < max_comics:
        print(f"Fetching page: {url}")
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        comic_img = soup.select_one("#comic img")
        if comic_img is None:
            print("Could not find comic image, stopping.")
            break

        image_url = "https:" + comic_img["src"]
        image_response = requests.get(image_url)
        image_response.raise_for_status()

        filename = os.path.join(save_folder, os.path.basename(image_url))
        with open(filename, "wb") as f:
            f.write(image_response.content)

        print(f"Downloaded: {filename}")
        downloaded += 1

        prev_link = soup.select_one("a[rel='prev']")
        if prev_link is None:
            print("Reached the first comic.")
            break
        url = "https://xkcd.com" + prev_link["href"]

    print(f"\nDone. {downloaded} comic(s) downloaded to '{save_folder}'.")


if __name__ == "__main__":
    download_xkcd_comics(max_comics=5)  # keep it small while testing