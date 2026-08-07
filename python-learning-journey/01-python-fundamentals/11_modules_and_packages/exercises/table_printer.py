def print_table(table_data):
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