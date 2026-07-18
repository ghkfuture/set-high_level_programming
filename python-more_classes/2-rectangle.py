#!/usr/bin/python3
"""Defines a structural module representing a Rectangle object."""


class Rectangle:
    """Manages geometric metrics and tracking methods of a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes instance configurations."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets width properties."""
        return self.__width

    @width.setter
    def width(self, value):
        """Guards side bounding properties."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets height properties."""
        return self.__height

    @height.setter
    def height(self, value):
        """Guards vertical dimensions."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Computes current geometric area."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates dimensional bounding perimeters."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
