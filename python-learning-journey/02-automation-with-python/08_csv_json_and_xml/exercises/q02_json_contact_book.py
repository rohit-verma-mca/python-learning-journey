"""
Question:
Write a program that lets you add a contact (name, phone, email) to a
JSON file, and look up a contact by name.

"""

import json
import os

DATA_FILE = "contacts.json"


def load_contacts():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def add_contact(name, phone, email):
    contacts = load_contacts()
    contacts[name] = {"phone": phone, "email": email}
    with open(DATA_FILE, "w") as f:
        json.dump(contacts, f, indent=2)
    print(f"Added contact: {name}")


def find_contact(name):
    contacts = load_contacts()
    contact = contacts.get(name)
    if contact:
        print(f"{name} -> Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print(f"No contact found for '{name}'.")
    return contact


if __name__ == "__main__":
    add_contact("Rahul Sharma", "9876543210", "rahul@example.com")
    add_contact("Priya Verma", "9123456789", "priya@example.com")

    find_contact("Rahul Sharma")
    find_contact("Someone Else")