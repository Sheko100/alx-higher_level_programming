#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for max_integer function
    """

    def test_normal_list(self):
        """Testing normal behavior by passing populated ordred numbers array
        """
        numbers = [1, 2, 3, 4, 5, 100, 150]
        self.assertEqual(max_integer(numbers), 150)

    def test_empty_list(self):
        """Testing passing empty list
        """
        numbers = []
        self.assertEqual(max_integer(numbers), None)

    def test_none(self):
        """Testing passing None
        """
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_string(self):
        """Testing passing string
        """
        with self.assertRaises(TypeError):
            max_integer("list")

    def test_num(self):
        """Testing passing number
        """
        with self.assertRaises(TypeError):
            max_integer(1)

    def test_tuble(self):
        """Testing passing tuble
        """
        with self.assertRaises(TypeError):
            max_integer((1, 2))

    def test_float(self):
        """Testing passing float
        """
        with self.assertRaises(TypeError):
            max_integer(5.5)


if __name__ == '__main__':
    unittest.main()
