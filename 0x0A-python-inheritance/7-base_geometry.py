#!/usr/bin/python3
"""Module that presents BaseGeometry class
"""


class BaseGeometry:
    """Class that defines a base geometry
    """
    def area(self):
        """raises exception with a message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name="value", value=""):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
