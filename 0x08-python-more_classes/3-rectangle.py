#!/usr/bin/python3
"""Module of a rectangle class.

    This module contains a class called rectangle
"""


class Rectangle:
    """defines a rectangle
    """

    def __init__(self, width=0, height=0):
        """initializes the rectangle instance

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """int: the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """gets the rectangle area

        Returns:
            the rectangle area
        """
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """returns rectangle shape with #
        """
        rect = ""
        if self.width > 0 and self.height > 0:
            rect = ((self.width * "#" + "\n") * self.height)[:-1]
        return rect
