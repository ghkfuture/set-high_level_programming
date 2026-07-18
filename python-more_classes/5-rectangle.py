#!/usr/bin/python3
"""Defines a structural module representing a Rectangle object."""


class Rectangle:
    """Triggers specific alert patterns upon engine reference collection
    cycles.
    """

    def __init__(self, width=0, height=0):
        """Initializes object metrics."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Enforces limits."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Enforces constraints."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates area coverage."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates perimeters."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Formats hash layout."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)

    def __repr__(self):
        """Formats instantiation strings."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Intercepts garbage deletion events to notify status."""
        print("Bye rectangle...")
