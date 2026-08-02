"""
Question:
Given a list like ['gold coin', 'dagger', 'gold coin', 'ruby'] representing
looted items, write a function add_to_inventory(inventory, added_items) that
returns an updated inventory dictionary with the new items merged in.

"""


def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory


def display_inventory(inventory):
    print("Inventory:")
    total_items = 0
    for item, count in inventory.items():
        print(f"{count} {item}")
        total_items += count
    print(f"Total number of items: {total_items}")


if __name__ == "__main__":
    inv = {"gold coin": 42, "rope": 1}
    dragon_loot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]

    inv = add_to_inventory(inv, dragon_loot)
    display_inventory(inv)