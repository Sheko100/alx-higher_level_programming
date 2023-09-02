#!/usr/bin/python3
"""Module to print a full name
"""


def say_my_name(first_name, last_name=""):
    """ prints "My name is <first name> <last name>"

    Args:
        first_name (str): first name
        last_name (str): last name

    Raises:
        TypeError: if first_name or last_name is not a string
            if firs_name is empty
            
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif len(first_name) < 1:
        raise TypeError("first_name can't be empty")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
