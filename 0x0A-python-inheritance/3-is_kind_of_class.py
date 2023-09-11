#!/usr/bin/python3
"""Module to check if an object is instance of a class or one of
its subclasses
"""


def is_kind_of_class(obj, a_class):
    """checks if obj is direct instance of a_class or one of its subclasses

    Args:
        obj (object): an object instance
        a_class (class): a class

    Returns:
        bool: True if successful, False otherwise
    """
    is_kind_of = False
    if isinstance(obj, a_class) or issubclass(obj.__class__, a_class):
        is_kind_of = True

    return (is_kind_of)
