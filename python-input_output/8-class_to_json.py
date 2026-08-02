#!/usr/bin/python3
"""Module that returns dictionary description for JSON serialization of object."""


def class_to_json(obj):
    """Returns the dictionary description of simple data structures of an object."""
    return obj.__dict__
