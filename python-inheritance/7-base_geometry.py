#!/usr/bin/python3
"""Defines a robust geometry management baseline validation module."""


class BaseGeometry:
    """Manages foundational matrix areas and value type validation."""

    def area(self):
        """Raises exception indicating an unimplemented calculation path."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that a named tracking value is a positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
