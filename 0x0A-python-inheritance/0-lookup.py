#!/usr/bin/python3
"""Module for listing available class attributes and methods
"""


def lookup(obj):
    """gets a list of available attributes and methods of an object

    Args:
        obj (class): a class to look up its instance
    """
    attr = []
    if isinstance(obj, object):
        newobj = obj()
        attr = newobj.__dir__()
        attr.sort()
    return (attr)
