#!/usr/bin/python3
"""Module to print a square with #
"""


def print_square(size):
    """prints a square with #

    Args:
        size (int): the size length of the square

    Raises:
        TypeError: if size is not integer
        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for n in range(0, size):
        print(size * "#")
