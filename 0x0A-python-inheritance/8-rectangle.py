#!/usr/bin/python3
"""Module that presents the Rectangle class
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """class that defines rectangle
    """

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
