#!/usr/bin/python3
"""Defines a strict subclass tracking utility function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited subclass instance exclusively."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
