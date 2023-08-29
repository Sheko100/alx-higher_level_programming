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
