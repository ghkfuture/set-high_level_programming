#!/usr/bin/python3
"""Module that inserts line of text after lines containing specific string."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file after each line containing search_string."""
    modified_lines = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            modified_lines.append(line)
            if search_string in line:
                modified_lines.append(new_string)

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(modified_lines)
