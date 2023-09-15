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
        self.size = size

    @property
    def size(self):
        """int: the size of the rectangle

        Raises:
            TypeError: if the value is not int
            ValueError: if the value equals or less than zero
        """
        return self.__width

    @size.setter
    def size(self, value):

        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value
        self.__height = value

    def __str__(self):
        name = self.__class__.__name__
        id, size, x, y = self.id, self.size, self.x, self.y

        return "[{}] ({}) {}/{} - {}".format(name, id, x, y, size)
