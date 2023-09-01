#!/usr/bin/python3
"""Module to add two numbers
"""


def add_integer(a, b=98):
    """Adds two numbers

        Args:
            a (int/float): first number
            b (int/float): second number

        Returns:
            int: the result of the addition
    """
    res = 0
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        res = int(a) + int(b)
    return (res)
