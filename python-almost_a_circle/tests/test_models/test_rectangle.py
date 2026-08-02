#!/usr/bin/python3
"""Unittests for Rectangle class."""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test suite for Rectangle class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_rect_1_2(self):
        """Test of Rectangle(1, 2)."""
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_rect_1_2_3(self):
        """Test of Rectangle(1, 2, 3)."""
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_rect_1_2_3_4(self):
        """Test of Rectangle(1, 2, 3, 4)."""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_rect_str_width(self):
        """Test of Rectangle("1", 2)."""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_rect_str_height(self):
        """Test of Rectangle(1, "2")."""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_rect_str_x(self):
        """Test of Rectangle(1, 2, "3")."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_rect_str_y(self):
        """Test of Rectangle(1, 2, 3, "4")."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_rect_1_2_3_4_5(self):
        """Test of Rectangle(1, 2, 3, 4, 5)."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)

    def test_rect_neg_width(self):
        """Test of Rectangle(-1, 2)."""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_rect_neg_height(self):
        """Test of Rectangle(1, -2)."""
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_rect_zero_width(self):
        """Test of Rectangle(0, 2)."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_rect_zero_height(self):
        """Test of Rectangle(1, 0)."""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_rect_neg_x(self):
        """Test of Rectangle(1, 2, -3)."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_rect_neg_y(self):
        """Test of Rectangle(1, 2, 3, -4)."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        """Test of area()."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        """Test of __str__() for Rectangle."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_89_1_2_3(self):
        """Test of update(89, 1, 2, 3) in Rectangle."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 3/10 - 1/2")

    def test_update_89_1_2_3_4(self):
        """Test of update(89, 1, 2, 3, 4) in Rectangle."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")

    def test_update_kw_id(self):
        """Test of update(**{ 'id': 89 }) in Rectangle."""
        r = Rectangle(10, 10)
        r.update(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_update_kw_id_width(self):
        """Test of update(**{ 'id': 89, 'width': 1 }) in Rectangle."""
        r = Rectangle(10, 10)
        r.update(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)

    def test_update_kw_id_width_height(self):
        """Test of update(**{ 'id': 89, 'width': 1, 'height': 2 }) in Rectangle."""
        r = Rectangle(10, 10)
        r.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)

    def test_update_kw_id_width_height_x(self):
        """Test of update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 }) in Rectangle."""
        r = Rectangle(10, 10)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)

    def test_update_kw_id_width_height_x_y(self):
        """Test of update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 }) in Rectangle."""
        r = Rectangle(10, 10)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.y, 4)

    def test_create_id(self):
        """Test of Rectangle.create(**{ 'id': 89 })."""
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_create_id_width(self):
        """Test of Rectangle.create(**{ 'id': 89, 'width': 1 })."""
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)

    def test_create_id_width_height(self):
        """Test of Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2 })."""
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)

    def test_create_id_width_height_x(self):
        """Test of Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 })."""
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)

    def test_create_id_width_height_x_y(self):
        """Test of Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })."""
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.y, 4)

    def test_save_to_file_none(self):
        """Test of Rectangle.save_to_file(None)."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Rectangle.json")

    def test_save_to_file_empty(self):
        """Test of Rectangle.save_to_file([])."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Rectangle.json")

    def test_save_to_file_list(self):
        """Test of Rectangle.save_to_file([Rectangle(1, 2)])."""
        r = Rectangle(1, 2, 0, 0, 1)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), 53)
        os.remove("Rectangle.json")

    def test_load_from_file_no_file(self):
        """Test of Rectangle.load_from_file() when file doesn't exist."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_exists(self):
        """Test of Rectangle.load_from_file() when file exists."""
        r = Rectangle(1, 2, 0, 0, 1)
        Rectangle.save_to_file([r])
        res = Rectangle.load_from_file()
        self.assertEqual(res[0].width, 1)
        os.remove("Rectangle.json")


if __name__ == '__main__':
    unittest.main()
