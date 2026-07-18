#!/usr/bin/python3
"""Defines a structural module representing a Rectangle object."""


class Rectangle:
    """Manages structural dimensions defining side measurements
    of a rectangle.
    """

    def __init__(self, width=0, height=0):
        """Initializes internal dimensional properties cleanly."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves internal coordinate width parameters."""
        return self.__width

    @width.setter
    def width(self, value):
        """Validates structural bounding type metrics."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves internal vertical height settings."""
        return self.__height

    @height.setter
    def height(self, value):
        """Validates incoming structural height definitions."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
