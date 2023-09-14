#!/usr/bin/python3
"""Unittest for Base class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests for the Base class"""

    def test_implicit_object_id(self):
        """Test that the object id is assigned appropriately
        if it is implicit
        """

        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 3)

    def test_explicit_object_id(self):
        """Test that the object id is assigned appropriately
        if it is explicit
        """

        obj55 = Base(55)
        obj88 = Base(88)
        self.assertEqual(obj55.id, 55)
        self.assertEqual(obj88.id, 88)


if __name__ == '__main__':
    unittest.main()
