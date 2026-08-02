#!/usr/bin/python3
"""Unittests for models/square.py."""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test suite for Square class."""

    def test_instantiation(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.area(), 25)

    def test_size_setter(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_invalid_size(self):
        with self.assertRaises(TypeError):
            Square("5")
        with self.assertRaises(ValueError):
            Square(-5)

    def test_str(self):
        s = Square(5, 1, 2, 3)
        self.assertEqual(str(s), "[Square] (3) 1/2 - 5")


if __name__ == '__main__':
    unittest.main()
