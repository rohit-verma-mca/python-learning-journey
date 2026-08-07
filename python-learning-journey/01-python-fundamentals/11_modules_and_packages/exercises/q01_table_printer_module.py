"""
Question:
Take the Table Printer function from the Strings topic, move it into
its own file (table_printer.py), then import and use it from this
separate script - practicing real module structure.

"""

from table_printer import print_table


if __name__ == "__main__":
    table_data = [
        ["apples", "oranges", "cherries", "banana"],
        ["Alice", "Bob", "Carol", "David"],
        ["dogs", "cats", "moose", "goose"],
    ]
    print_table(table_data)