#!/usr/bin/python3
"""Defines a structural module representing a Rectangle object."""


class Rectangle:
    """Monitors live active counts of overall initialized class
    representations.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Tracks construction offsets."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets width details."""
        return self.__width

    @width.setter
    def width(self, value):
        """Limits inputs."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets height details."""
        return self.__height

    @height.setter
    def height(self, value):
        """Limits variables."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates metrics."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates paths."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Formats matrix representations."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)

    def __repr__(self):
        """Formats string recreation paths."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Tracks destructor reduction patterns."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
