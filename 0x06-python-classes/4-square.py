#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Class Square

    This module creates a class called Square
"""


class Square:
    """a class defines a Square with size

    Args:
        size (int): The size of the square
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """int: gets and sets the size of the square

        Raises a TypeError if the size is not integer and
        raises a ValueError if the size less than 0
        """
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Gets the square area

        Returns: the square area
        """
        return self.__size ** 2
