#!/usr/bin/python3
"""
Module for add_integer method.
"""


def add_integer(a, b=98):
    """Adds two integers or floats and casts them to integers.

    Args:
        a: First number (int or float)
        b: Second number (int or float, default 98)

    Returns:
        The integer addition of a and b.

    Raises:
        TypeError: If a or b is not an int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
