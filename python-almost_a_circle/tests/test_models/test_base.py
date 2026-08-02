#!/usr/bin/python3
"""
Unittests for Base class in models/base.py
"""
import unittest
import os
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test suite for Base class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_id_auto_increment(self):
        """Test Base for assigning automatically an ID."""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id_auto_increment_plus_one(self):
        """Test Base for assigning automatically an ID + 1 of previous."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_passed(self):
        """Test Base(89) saving the ID passed."""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        """Test Base.to_json_string(None)."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test Base.to_json_string([])."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_dict(self):
        """Test Base.to_json_string([{'id': 12}])."""
        d = [{'id': 12}]
        self.assertEqual(Base.to_json_string(d), '[{"id": 12}]')

    def test_to_json_string_type(self):
        """Test Base.to_json_string([{'id': 12}]) returning a string."""
        d = [{'id': 12}]
        self.assertIsInstance(Base.to_json_string(d), str)

    def test_from_json_string_none(self):
        """Test Base.from_json_string(None)."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test Base.from_json_string("[]")."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_val(self):
        """Test Base.from_json_string('[{"id": 89}]')."""
        s = '[{"id": 89}]'
        self.assertEqual(Base.from_json_string(s), [{'id': 89}])

    def test_from_json_string_type(self):
        """Test Base.from_json_string('[{"id": 89}]') returning a list."""
        s = '[{"id": 89}]'
        self.assertIsInstance(Base.from_json_string(s), list)


if __name__ == '__main__':
    unittest.main()
