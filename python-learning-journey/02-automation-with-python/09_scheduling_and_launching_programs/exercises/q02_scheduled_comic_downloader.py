"""
Question:
Combine the XKCD downloader with the schedule module so it automatically
checks for and downloads the latest comic on a recurring basis, instead
of running once manually.

"""

import os
import time
import schedule
import requests
from bs4 import BeautifulSoup


def download_latest_comic(save_folder="xkcd_scheduled"):
    os.makedirs(save_folder, exist_ok=True)

    response = requests.get("https://xkcd.com")
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    comic_img = soup.select_one("#comic img")
    if comic_img is None:
        print("Could not find today's comic.")
        return

    image_url = "https:" + comic_img["src"]
    image_response = requests.get(image_url)
    filename = os.path.join(save_folder, os.path.basename(image_url))

    with open(filename, "wb") as f:
        f.write(image_response.content)

    print(f"[{time.strftime('%H:%M:%S')}] Downloaded latest comic: {filename}")


def solve():
    # For real use: schedule.every().day.at("09:00").do(download_latest_comic)
    # Using a short interval here just to demonstrate it working while testing:
    schedule.every(10).seconds.do(download_latest_comic)

    print("Scheduler started. Checking every 10 seconds (for testing). Press Ctrl+C to stop.")
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    solve()