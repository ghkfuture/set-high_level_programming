#!/usr/bin/python3
"""Defines a subclassed Square structural blueprint component."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Manages dimension rules of a uniform Square shape object."""

    def __init__(self, size):
        """Initializes size metrics using structural validator steps."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
