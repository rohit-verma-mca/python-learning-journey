"""
Question:
Connect to a Google Sheet using a service account, read all values from
it, then update one specific cell and confirm the change reflects in
the actual sheet.

"""

import gspread

KEY_FILE = "../../../secrets/google_sheets_key.json"  # adjust path if needed
SHEET_NAME = "Test Sheet"


def connect_to_sheet():
    gc = gspread.service_account(filename=KEY_FILE)
    sheet = gc.open(SHEET_NAME).sheet1
    return sheet


def read_all_data(sheet):
    data = sheet.get_all_records()
    print("Current data in sheet:")
    for row in data:
        print(row)
    return data


def update_cell(sheet, cell, new_value):
    sheet.update_acell(cell, new_value)
    print(f"Updated cell {cell} to '{new_value}'")


if __name__ == "__main__":
    sheet = connect_to_sheet()

    read_all_data(sheet)

    update_cell(sheet, "B2", 95)

    print("\nAfter update:")
    read_all_data(sheet)