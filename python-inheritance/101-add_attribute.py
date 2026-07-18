#!/usr/bin/python3
"""Defines a dynamic attribute tracking validation engine."""


def add_attribute(obj, name, value):
    """Adds a new parameter property if structural slots allow it."""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
