#!/usr/bin/python3
"""
Module for print_square function.
"""


def print_square(size):
    """Prints a square with the character #.

    Args:
        size: Size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size < 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
