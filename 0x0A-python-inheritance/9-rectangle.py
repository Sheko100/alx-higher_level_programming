#!/usr/bin/python3
"""Module that presents the Rectangle class
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """class that defines rectangle
    """

    def area(self):
        """gets the rectangle area

        Returns:
            rectangle area (int)
        """
        width = self._width
        height = self._height
        return (width * height)

    def __init__(self, width, height):
        """initializes width and height to the new instance

        Args:
            width (int): rectangle width
            height (int): rectangle height
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self._width = width
        self._height = height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self._width, self._height)
