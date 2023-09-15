#!/usr/bin/python3
"""Unittest for Rectangle class"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for the Rectangle class"""

    def test_normal_width(self):
        """Test for the normal behavior of passing integer width"""

        rect1 = Rectangle(10, 5, 5, 2)
        self.assertEqual(rect1.width, 10)

    def test_negative_or_zero_width(self):
        """Test for handling the nagative and zero values"""

        with self.assertRaises(ValueError):
            rect3 = Rectangle(0, 2, 3, 1)

        with self.assertRaises(ValueError):
            rect3 = Rectangle(-1, 2, 3, 1)

    def test_not_int_width(self):
        """Test for the cases when the passing value of width is not int"""

        with self.assertRaises(TypeError):
            rect3 = Rectangle("5", 2, 3, 1)

        with self.assertRaises(TypeError):
            rect3 = Rectangle(2.5, 2, 3, 1)

        with self.assertRaises(TypeError):
            rect3 = Rectangle((5, 5), 2, 3, 1)

        with self.assertRaises(TypeError):
            rect3 = Rectangle([], 2, 3, 1)

        with self.assertRaises(TypeError):
            rect3 = Rectangle({"width: 5"}, 2, 3, 1)

        with self.assertRaises(TypeError):
            rect3 = Rectangle({2, 5}, 2, 3, 1)

        with self.assertRaises(TypeError):
            rect3 = Rectangle(None, 2, 3, 1)

    def test_normal_height(self):
        """Test for the normal behavior of passing integer height"""

        rect1 = Rectangle(10, 5, 5, 2)
        self.assertEqual(rect1.height, 5)

    def test_negative_or_zero_height(self):
        """Test for handling the nagative and zero values"""

        with self.assertRaises(ValueError):
            rect3 = Rectangle(5, 0, 3, 1)

        with self.assertRaises(ValueError):
            rect3 = Rectangle(5, -1, 3, 1)

    def test_not_int_height(self):
        """Test for the cases when the passing value of height is not int"""

        with self.assertRaises(TypeError):
            rect3 = Rectangle(5, "2", 3, 1)

        with self.assertRaises(TypeError):
            rect3 = Rectangle(5, 2.5 , 3, 1)

        with self.assertRaises(TypeError):
            rect3 = Rectangle(5, (2, 2), 3, 1)

        with self.assertRaises(TypeError):
            rect3 = Rectangle(5, [], 3, 1)

        with self.assertRaises(TypeError):
            rect3 = Rectangle(5, {"height: 2"}, 3, 1)

        with self.assertRaises(TypeError):
            rect3 = Rectangle(5, {2, 5}, 3, 1)

        with self.assertRaises(TypeError):
            rect3 = Rectangle(5, None, 3, 1)

    def test_normal_x_axis(self):
        """Test for the normal behavior of passing integer x"""

        rect1 = Rectangle(10, 5, 5, 2)
        self.assertEqual(rect1.x, 5)

    def test_negative_x_axis(self):
        """Test for handling the nagative value"""

        with self.assertRaises(ValueError):
            rect3 = Rectangle(5, 2, -1, 1)

    def test_not_int_x_axis(self):
        """Test for the cases when the passing value of x is not int"""

        with self.assertRaises(TypeError):
            rect3 = Rectangle(5, 2, "3", 1)

        with self.assertRaises(TypeError):
            rect3 = Rectangle(5, 2 , 3.5, 1)

        with self.assertRaises(TypeError):
            rect3 = Rectangle(5, 2, (3, 3), 1)

        with self.assertRaises(TypeError):
            rect3 = Rectangle(5, 2, [], 1)

        with self.assertRaises(TypeError):
            rect3 = Rectangle(5, 2, {"x": 3}, 1)

        with self.assertRaises(TypeError):
            rect3 = Rectangle(5, 2, {3, 5}, 1)

        with self.assertRaises(TypeError):
            rect3 = Rectangle(5, 2, None, 1)

    def test_normal_y_axis(self):
        """Test for the normal behavior of passing integer y"""

        rect1 = Rectangle(10, 5, 5, 2)
        self.assertEqual(rect1.y, 2)

    def test_negative_y_axis(self):
        """Test for handling the nagative value"""

        with self.assertRaises(ValueError):
            rect3 = Rectangle(5, 2, 3, -1)

    def test_not_int_y_axis(self):
        """Test for the cases when the passing value of y is not int"""

        with self.assertRaises(TypeError):
            rect3 = Rectangle(5, 2, 3, "1")

        with self.assertRaises(TypeError):
            rect3 = Rectangle(5, 2 , 3, 1.5)

        with self.assertRaises(TypeError):
            rect3 = Rectangle(5, 2, 3, (1, 1))

        with self.assertRaises(TypeError):
            rect3 = Rectangle(5, 2, 3, [])

        with self.assertRaises(TypeError):
            rect3 = Rectangle(5, 2, 3, {"y": 1})

        with self.assertRaises(TypeError):
            rect3 = Rectangle(5, 2, 3, {1, 5})

        with self.assertRaises(TypeError):
            rect3 = Rectangle(5, 2, 3, None)

    def test_area(self):
        """Test for the area output"""

        rect3 = Rectangle(5, 2, 3, 1)
        self.assertEqual(rect3.area(), 10)

    def test_rect_str(self):
        """Test for the rect str representation"""

        rect3 = Rectangle(5, 2, 3, 1, 55)
        self.assertEqual(str(rect3), "[Rectangle] (55) 3/1 - 5/2")

