#!/usr/bin/python3
"""Module that defines a file writing function."""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns char count."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
