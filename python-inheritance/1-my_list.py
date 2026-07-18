#!/usr/bin/python3
"""Defines a subclassed list class."""


class MyList(list):
    """Implements custom printed list behaviors extending list."""

    def print_sorted(self):
        """Prints the internal numerical list sorted in ascending order."""
        print(sorted(self))
