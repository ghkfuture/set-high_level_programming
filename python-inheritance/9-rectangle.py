#!/usr/bin/python3
"""Defines an expressive fully configured Rectangle shape."""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Implements structural evaluations and string representation layouts."""

    def __init__(self, width, height):
        """Configures dimensions matching parent parameters."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Computes internal geometric area boundaries."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a scannable structural print configuration details."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
