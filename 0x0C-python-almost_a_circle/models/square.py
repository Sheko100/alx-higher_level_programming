#!/usr/bin/pyhton3
"""Module for defining a Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that defines a square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes an object instance

        Args:
            size (int): the square size
            x (int): the square x axis
            y (int): the square y axis
            id (int): the square id
        """
        super().__init__(size, size, x, y, id)
