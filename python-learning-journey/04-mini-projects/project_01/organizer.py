"""
Project: Automated File Organizer & Report Generator
Day 1 — Core Logic

Scans a source folder and sorts files into subfolders by file type
(Documents, Images, Spreadsheets, Others), based on file extension.
"""
import logging
from report_generator import generate_report
import os
import shutil
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("organizer.log"),
        logging.StreamHandler()
    ]
)
FILE_CATEGORIES = {
    "Documents": [".pdf", ".docx", ".txt"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Spreadsheets": [".xlsx", ".csv"],
}


def get_category(filename):
    ext = os.path.splitext(filename)[1].lower()
    for category, extensions in FILE_CATEGORIES.items():
        if ext in extensions:
            return category
    return "Others"


def organize_folder(source_folder):
    if not os.path.exists(source_folder):
        logging.error(f"Source folder '{source_folder}' does not exist.")
        return {}

    moved_summary = {}

    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        if os.path.isfile(source_path):
            category = get_category(filename)
            category_folder = os.path.join(source_folder, category)
            os.makedirs(category_folder, exist_ok=True)

            dest_path = os.path.join(category_folder, filename)
            shutil.move(source_path, dest_path)

            moved_summary[category] = moved_summary.get(category, 0) + 1
            logging.info(f"Moved '{filename}' -> {category}/")

    logging.info("\nSummary:")
    for category, count in moved_summary.items():
        print(f"  {category}: {count} file(s)")

    return moved_summary


if __name__ == "__main__":
    summary = organize_folder("test_source_folder")
    if summary:
        generate_report(summary, output_folder="test_source_folder")