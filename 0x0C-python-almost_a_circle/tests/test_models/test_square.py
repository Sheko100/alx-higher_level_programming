#!/usr/bin/python3
"""Unittest for Square class"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for the Square class
    """

    def test_square_init(self):
        """Test for the initialization of a square object instance"""

        size, x, y, id = 10, 5, 3, 55

        sq1 = Square(size, x, y, id)
        self.assertEqual(sq1.width, size)
        self.assertEqual(sq1.height, size)
        self.assertEqual(sq1.x, x)
        self.assertEqual(sq1.y, y)
        self.assertEqual(sq1.id, 55)

    def test_square_str(self):
        """Test for the string represntation of an object insatnce"""

        size, x, y, id = 10, 5, 3, 55

        sq1 = Square(size, x, y, id)
        self.assertEqual(str(sq1), "[Square] (55) 5/3 - 10")
