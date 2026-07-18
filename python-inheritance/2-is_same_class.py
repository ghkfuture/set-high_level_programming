#!/usr/bin/python3
"""Defines an exact class checking function."""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a specified class."""
    return type(obj) is a_class
