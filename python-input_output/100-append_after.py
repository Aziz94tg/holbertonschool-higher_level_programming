#!/usr/bin/python3
"""Inserts a line of text after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """Appends `new_string` after each line in `filename`
    that contains `search_string`.

    Args:
        filename: Name of the file to modify.
        search_string: The string to search for in each line.
        new_string: The string to insert after matched lines.
    """
    with open(filename, "r") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        new_lines.append(line)
        if search_string in line:
            new_lines.append(new_string)

    with open(filename, "w") as f:
        f.writelines(new_lines)
