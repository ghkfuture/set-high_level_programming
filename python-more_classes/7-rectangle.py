#!/usr/bin/python3
"""Defines a structural module representing a Rectangle object."""


class Rectangle:
    """Injects completely customizable markers directly inside standard text
    representations.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Logs allocation metrics."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets width coordinates."""
        return self.__width

    @width.setter
    def width(self, value):
        """Validates width configurations."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets height configurations."""
        return self.__height

    @height.setter
    def height(self, value):
        """Validates height settings."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates internal coordinates."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates external perimeter structures."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Draws layout mapping out customizable symbols."""
        if self.__width == 0 or self.__height == 0:
            return ""
        sym = str(self.print_symbol)
        return "\n".join([sym * self.__width] * self.__height)

    def __repr__(self):
        """Formats recreation metrics."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Tracks standard decrements."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
