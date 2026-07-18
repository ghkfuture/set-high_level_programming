#!/usr/bin/python3
"""Defines a basic Rectangle component inheriting from BaseGeometry."""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Implements basic bounded private metrics of a Rectangle shape."""

    def __init__(self, width, height):
        """Initializes dimensions after type checking verification."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
