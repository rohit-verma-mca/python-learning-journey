"""
Question:
Given a dictionary like {'rope': 1, 'torch': 6, 'gold coin': 42}, write
a function display_inventory(inventory) that prints each item with its
count and a total item count at the end.

"""


def display_inventory(inventory):
    print("Inventory:")
    total_items = 0
    for item, count in inventory.items():
        print(f"{count} {item}")
        total_items += count
    print(f"Total number of items: {total_items}")


if __name__ == "__main__":
    stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}
    display_inventory(stuff)