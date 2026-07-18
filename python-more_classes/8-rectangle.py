#!/usr/bin/python3
"""Defines a structural module representing a Rectangle object."""


class Rectangle:
    """Utilizes specialized logical sorting comparison methods to evaluate
    rect instances.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Configures instances dynamically."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets width metrics."""
        return self.__width

    @width.setter
    def width(self, value):
        """Verifies horizontal parameters."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets height metrics."""
        return self.__height

    @height.setter
    def height(self, value):
        """Verifies vertical boundaries."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates internal spacing."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates tracking values."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Outputs custom layouts."""
        if self.__width == 0 or self.__height == 0:
            return ""
        sym = str(self.print_symbol)
        return "\n".join([sym * self.__width] * self.__height)

    def __repr__(self):
        """Recreates initialization codes."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Monitors deletion actions."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Evaluates and shifts major surface area allocations."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
