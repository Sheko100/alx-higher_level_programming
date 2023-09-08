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

    def test_max_first(self):
        """Testing passing list with the max int at the first
        """
        numbers = [150, 1, 2, 3, 4, 5, 100]
        self.assertEqual(max_integer(numbers), 150)

    def test_max_middle(self):
        """Testing passing list with the max int in the middle
        """
        numbers = [1, 2, 3, 150, 4, 5, 100]
        self.assertEqual(max_integer(numbers), 150)

    def test_one_negative(self):
        """Testing passing list with one negatve numbers
        """
        numbers = [1, 2, 3, 4, -5, 100, 150]
        self.assertEqual(max_integer(numbers), 150)

    def test_negative_list(self):
        """Testing passing list with all negative
        """
        numbers = [-1, -2, -3, -4, -5, -100, -150]
        self.assertEqual(max_integer(numbers), -1)

    def test_one_element_list(self):
        """Testing passing list with one element
        """
        numbers = [1]
        self.assertEqual(max_integer(numbers), 1)

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


if __name__ == '__main__':
    unittest.main()
