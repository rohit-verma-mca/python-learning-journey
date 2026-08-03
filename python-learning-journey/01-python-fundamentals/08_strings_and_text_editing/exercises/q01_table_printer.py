"""
Question:
Given a list of lists of strings representing table data (e.g., rows of a
spreadsheet), write a function that prints it neatly aligned in columns —
each column's width based on its longest entry in that column, with
consistent spacing between columns.

"""


def print_table(table_data):
    # find the widest entry in each column
    col_widths = [0] * len(table_data)
    for i, column in enumerate(table_data):
        col_widths[i] = max(len(str(item)) for item in column)

    num_rows = len(table_data[0])
    for row in range(num_rows):
        line = ""
        for col in range(len(table_data)):
            item = str(table_data[col][row])
            line += item.rjust(col_widths[col]) + " "
        print(line)


if __name__ == "__main__":
    table_data = [
        ["apples", "oranges", "cherries", "banana"],
        ["Alice", "Bob", "Carol", "David"],
        ["dogs", "cats", "moose", "goose"],
    ]
    print_table(table_data)