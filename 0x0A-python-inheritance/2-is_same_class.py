#!/usr/bin/python3
"""Module to check if an object is instance of specified class
"""


def is_same_class(obj, a_class):
    """checks if obj is instance of a_class

    Args:
        obj (object): an object instance
        a_class (class): a class

    Retiurn:
        bool: True if successful, False otherwise
    """
    is_same = False
    if isinstance(obj, a_class) and type(obj) == a_class:
        is_same = True

    return (is_same)
