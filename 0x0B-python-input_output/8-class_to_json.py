#!/usr/bin/python3
"""Module for getting the dictionary description for
    JSON serialization of an object
"""
import json


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    for JSON serialization of an object

    Args:
        obj (object): an instance of a Class

    Returns: class dictionary descritiption
    """
    dct = obj.__dict__
    jsons = json.dumps(dct)
    return (jsons)
