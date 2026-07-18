#!/usr/bin/python3
"""Defines a highly customized standalone Square subclass component."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Extends rectangle mechanics with customized print mapping strings."""

    def __init__(self, size):
        """Validates metrics while passing downstream constructors."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns custom structural square formatting data string."""
        return "[Square] {}/{}".format(self.__size, self.__size)
