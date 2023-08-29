#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Class Square

    This module creates a class called Square
"""


class Square:
    """a class defines a Square with size

    Args:
        size (int): The size of the square
        position (int, int): a position in the square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """int: gets and sets the size of the square

        Raises a TypeError if the size is not integer and
        raises a ValueError if the size less than 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Gets the square area

        Returns: the square area
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with # in a specific position"""
        size = self.__size
        pos = self.__position
        if size > 0:
            for d in range(0, pos[1]):
                print()
            for r in range(0, size):
                for p in range(0, pos[0]):
                    print(" ", end="")
                print("#" * size)
        else:
            print()
