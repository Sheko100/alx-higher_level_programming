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


class TestSquareSize(unittest.TestCase):
    """Tests for the size attribute of the Square class"""

    def test_normal_size(self):
        """Test for the normal behavior of passing integer size"""

        sq1 = Square(10, 5, 3)
        self.assertEqual(sq1.size, 10)

    def test_negative_or_zero_size(self):
        """Test for handling the nagative and zero values"""

        with self.assertRaises(ValueError):
            sq1 = Square(0, 2, 3)

        with self.assertRaises(ValueError):
            sq1 = Square(-1, 2, 3)

    def test_not_int_size(self):
        """Test for the cases when the passing value of size is not int"""

        with self.assertRaises(TypeError):
            sq1 = Square("5", 2, 3)

        with self.assertRaises(TypeError):
            sq1 = Square(2.5, 2, 1)

        with self.assertRaises(TypeError):
            sq1 = Square((5, 5), 2, 3)

        with self.assertRaises(TypeError):
            sq1 = Square([], 2, 3)

        with self.assertRaises(TypeError):
            sq1 = Square({"width: 5"}, 2, 3)

        with self.assertRaises(TypeError):
            sq1 = Square({2, 5}, 2, 3)

        with self.assertRaises(TypeError):
            sq1 = Square(None, 2, 3)
