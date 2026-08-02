#!/usr/bin/python3
"""Module that defines an integer addition function."""


def add_integer(a, b=98):
    """Adds 2 integers or floats casted to integers.

    Args:
        a: first integer or float
        b: second integer or float (default 98)

    Returns:
        The addition of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
