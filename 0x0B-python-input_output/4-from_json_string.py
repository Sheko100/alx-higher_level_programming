#!/usr/bin/python3
"""Module to deserialize JSON to a python object
"""
import json


def from_json_string(my_str):
    """deserialzes JSON string to a python object

    Args:
        my_str (str): JSON string

    Returns: python object
    """
    obj = json.loads(my_str)
    return (obj)
