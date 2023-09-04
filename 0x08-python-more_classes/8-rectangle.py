#!/usr/bin/python3
"""Module of a rectangle class.

    This module contains a class called rectangle
"""


class Rectangle:
    """defines a rectangle

    Attributes:
        number_of_instances (int): The count of rectangle instances
        print_symbol (str): symbol to print the rectangle shape with
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes the rectangle instance

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """returns rectangle shape with symbol
        """
        rect = ""
        symbol = str(self.print_symbol)
        if self.width > 0 and self.height > 0:
            rect = ((self.width * symbol + "\n") * self.height)[:-1]
        return rect

    def __repr__(self):
        """returns new instance representation
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """prints a message after deleting
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compares two rectangles areas

        Args:
            rect_1 (Rectangle): first rectangle
            rect_2 (Rectangle): second rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1
