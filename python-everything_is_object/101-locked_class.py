#!/usr/bin/python3
"""Module that defines a low-memory cost locked class constraint."""


class LockedClass:
    """Prevents dynamic attributes creation except for first_name."""
    __slots__ = ["first_name"]
