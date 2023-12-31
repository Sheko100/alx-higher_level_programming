#!/usr/bin/python3
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
        return self.width

    @size.setter
    def size(self, value):

        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def __str__(self):
        name = self.__class__.__name__
        id, size, x, y = self.id, self.size, self.x, self.y

        return "[{}] ({}) {}/{} - {}".format(name, id, x, y, size)

    def update(self, *args, **kwargs):
        """Updates the square attributes

        Args:
            *args (tuple): argument list of attributes
            **kwargs (dictionary): keyword argument list of attributes
        """
        if len(args) > 0:
            argn = 0
            for arg in args:
                if argn == 0:
                    self.id = arg
                elif argn == 1:
                    self.size = arg
                elif argn == 2:
                    self.x = arg
                elif argn == 3:
                    self.y = arg
                argn += 1
        else:
            for key in kwargs:
                value = kwargs[key]
                setattr(self, key, value)

    def to_dictionary(self):
        """Gets the dictionary representation of an object instance

        Returns: the dictionary representation of a
        Square object instance
        """
        keys = ["id", "size", "x", "y"]
        dct = {}

        for key in keys:
            dct[key] = getattr(self, key)

        return dct
