#!/usr/bin/python3
"""Module to check if an object instance of a class that is inherited from
a specified class
"""


def inherits_from(obj, a_class):
    """checks if obj is direct instance of a class that inherited from a_class

    Args:
        obj (object): an object instance
        a_class (class): a class

    Returns:
        bool: True if successful, False otherwise
    """
    is_inherited = False
    if issubclass(obj.__class__, a_class) and type(obj) != a_class:
        is_inherited = True

    return (is_inherited)
