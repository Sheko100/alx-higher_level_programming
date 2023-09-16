#!/usr/bin/python3
"""Unittest for Base class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

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

    def test_to_json_string(self):
        """Test for the to_json_string static method normal behavior"""

        dictlist = [{"id": 55, "size": 10}, {"x": 5, "y": 4}, {"height": 7}]
        obj4 = Base()

        dictliststr = obj4.to_json_string(dictlist)
        self.assertEqual(
                dictliststr,
                '[{"id": 55, "size": 10}, {"x": 5, "y": 4}, {"height": 7}]'
        )

    def test_to_json_string_empty_list(self):
        """Test for the to_json_string static method with empty list"""

        dictlist = []
        obj4 = Base()

        dictliststr = obj4.to_json_string(dictlist)
        self.assertEqual(dictliststr,"[]")

    def test_to_json_string_none_list(self):
        """Test for passing None intead of list to
        the to_json_string static method
        """

        obj4 = Base()
        dictliststr = obj4.to_json_string(None)

        self.assertEqual(dictliststr,"[]")

    def test_to_json_string_empty_dict(self):
        """Test for passing list of empty dictionaries to
        the to_json_string static method
        """

        dictlist = [{}, {}, {}]
        obj4 = Base()

        dictliststr = obj4.to_json_string(dictlist)

        self.assertEqual(dictliststr,"[{}, {}, {}]")

    def test_save_to_file(self):
        """Test for the normal behavior of the save_to_file method"""

        rect1 = Rectangle(10, 5, 4, 2, 55)
        rect2 = Rectangle(20, 10, 5, 7, 88)
        sq1 = Square(10, 4, 2, 55)
        sq2 = Square(20, 5, 7, 88)

        rectlist = [rect1, rect2]
        sqlist = [sq1, sq2]
        rectdict = [rect1.to_dictionary(), rect2.to_dictionary()]
        sqdict = [sq1.to_dictionary(), sq2.to_dictionary()]

        Rectangle.save_to_file(rectlist)
        with open("Rectangle.json") as file:
            content = file.read()
        rectjson = Rectangle.to_json_string(rectdict)
        self.assertEqual(rectjson, content)

        Square.save_to_file(sqlist)
        with open("Square.json") as file:
            content = file.read()
        sqjson = Square.to_json_string(sqdict)
        self.assertEqual(sqjson, content)


if __name__ == '__main__':
    unittest.main()
