#!/usr/bin/python3
"""Module to add attribute to an object if allowed
"""

def add_attribute(obj, name, value):
    """adds attribute to object if allowed

    Args:
        obj (object): object instance to add the attribute to
        name (str): attribute name
        value (str): attribute value
    """
    obj.__setattr__(name, value)
    obj.__setattr__("hello", "world")
    print(dir(obj))
