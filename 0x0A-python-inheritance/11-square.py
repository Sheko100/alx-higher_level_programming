#!/usr/bin/python3
"""Module that presents Square class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class that defines square inherited from the rectangle class
    """

    def area(self):
        """gets the square area

        Returns:
            the square area (int)
        """
        return (self._width ** 2)

    def __init__(self, size):
        """initialize the instance

        Args:
            size (int): the square size
        """
        super().integer_validator("size", size)
        self._width = size
        self._height = size

    def __str__(self):
        name = self.__class__.__name__
        return "[{}] {}/{}".format(name, self._width, self._height)
