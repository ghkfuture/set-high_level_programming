#!/usr/bin/python3
"""
Unittests for Square class in models/square.py
"""
import unittest
import os
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test suite for Square class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_square_1(self):
        """Test of Square(1)."""
        s = Square(1)
        self.assertEqual(s.size, 1)

    def test_update_none(self):
        """Test of update() in Square."""
        s = Square(5)
        s.update()
        self.assertEqual(s.size, 5)

    def test_update_89(self):
        """Test of update(89) in Square."""
        s = Square(5)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_update_89_1(self):
        """Test of update(89, 1) in Square."""
        s = Square(5)
        s.update(89, 1)
        self.assertEqual(s.size, 1)

    def test_update_89_1_2(self):
        """Test of update(89, 1, 2) in Square."""
        s = Square(5)
        s.update(89, 1, 2)
        self.assertEqual(s.x, 2)

    def test_update_89_1_2_3(self):
        """Test of update(89, 1, 2, 3) in Square."""
        s = Square(5)
        s.update(89, 1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_update_kw_id(self):
        """Test of update(**{ 'id': 89 }) in Square."""
        s = Square(5)
        s.update(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_update_kw_id_size(self):
        """Test of update(**{ 'id': 89, 'size': 1 }) in Square."""
        s = Square(5)
        s.update(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)

    def test_update_kw_id_size_x(self):
        """Test of update(**{ 'id': 89, 'size': 1, 'x': 2 }) in Square."""
        s = Square(5)
        s.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)

    def test_update_kw_id_size_x_y(self):
        """Test of update(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 }) in Square."""
        s = Square(5)
        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.y, 3)

    def test_create_id(self):
        """Test of Square.create(**{ 'id': 89 })."""
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_create_id_size(self):
        """Test of Square.create(**{ 'id': 89, 'size': 1 })."""
        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)

    def test_create_id_size_x(self):
        """Test of Square.create(**{ 'id': 89, 'size': 1, 'x': 2 })."""
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)

    def test_create_id_size_x_y(self):
        """Test of Square.create(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })."""
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.y, 3)

    def test_save_to_file_none(self):
        """Test of Square.save_to_file(None) in Square."""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Square.json")

    def test_save_to_file_empty(self):
        """Test of Square.save_to_file([]) in Square."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Square.json")

    def test_save_to_file_square(self):
        """Test of Square.save_to_file([Square(1)]) in Square."""
        s = Square(1, 0, 0, 1)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()), 38)
        os.remove("Square.json")

    def test_load_from_file_no_file(self):
        """Test of Square.load_from_file() when file doesn't exist."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_exists(self):
        """Test of Square.load_from_file() when file exists."""
        s = Square(1, 0, 0, 1)
        Square.save_to_file([s])
        res = Square.load_from_file()
        self.assertEqual(res[0].size, 1)
        os.remove("Square.json")


if __name__ == '__main__':
    unittest.main()
