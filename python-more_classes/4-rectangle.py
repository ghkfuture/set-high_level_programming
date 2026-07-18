#!/usr/bin/python3
"""Defines a structural module representing a Rectangle object."""


class Rectangle:
    """Allows clean external parsing and recreation formatting
    configurations.
    """

    def __init__(self, width=0, height=0):
        """Initializes instance state contexts."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets width properties."""
        return self.__width

    @width.setter
    def width(self, value):
        """Guards boundary definitions."""
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
        """Guards heights."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates area."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates outer metrics."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Generates standard user printable matrices."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)

    def __repr__(self):
        """Generates official executable string declarations."""
        return "Rectangle({}, {})".format(self.__width, self.__height)
