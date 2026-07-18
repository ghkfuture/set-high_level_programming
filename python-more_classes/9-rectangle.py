#!/usr/bin/python3
"""Defines a structural module representing a Rectangle object."""


class Rectangle:
    """Implements factory patterns to spawn uniform square sub-instances
    easily.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes internal variables."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets width specifications."""
        return self.__width

    @width.setter
    def width(self, value):
        """Verifies integers."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets height specifications."""
        return self.__height

    @height.setter
    def height(self, value):
        """Verifies configurations."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns current mathematical areas."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns current outer measurements."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Renders string matrices."""
        if self.__width == 0 or self.__height == 0:
            return ""
        sym = str(self.print_symbol)
        return "\n".join([sym * self.__width] * self.__height)

    def __repr__(self):
        """Renders structural configurations."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Processes structural termination warnings."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Finds target properties across models."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Constructs an aligned symmetrical instance."""
        return cls(size, size)
