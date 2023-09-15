#!/usr/bin/python3
"""Module for defining the Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """Class that defines a rectangle inherited from Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new object instance of the Rectangle class

        Args:
            width (int): rectangle width
            height (int): rectangle height
            x (int): rectangle x axis
            y (int): rectangle y axis
            
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """int: the width of the rectangle

        Raises:
            TypeError: if the value is not int
            ValueError: if the value equals or less than zero
        """
        return self.__width

    @width.setter
    def width(self, value):

        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """int: the height of the rectangle

        Raises:
            TypeError: if the value is not int
            ValueError: if the value equals or less than zero
        """
        return self.__height

    @height.setter
    def height(self, value):

        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """int: the x axis of the rectangle

        Raises:
            TypeError: if the value is not int
            ValueError: if the value is less than zero
        """
        return self.__x

    @x.setter
    def x(self, value):

        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """int: the y axis of the rectangle

        Raises:
            TypeError: if the value is not int
            ValueError: if the value is less than zero
        """
        return self.__y

    @y.setter
    def y(self, value):

        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Gets the area of the rectangle

        Returns: the area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """Displays the rectangle with # on the standard output
        """

        cols = self.width
        rows = self.height
        for row in range(rows):
            print(cols * "#")

    def __str__(self):
        name = self.__class__.__name__
        id = self.id
        width, height, x, y = self.width, self.height, self.x, self.y
        return ("[{}] ({}) {}/{} - {}/{}".format(name, id, x, y, width, height))
