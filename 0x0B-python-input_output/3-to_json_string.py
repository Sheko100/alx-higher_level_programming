#!/usr/bin/python3
"""Module to serialize an object to JSON
"""
import json


def to_json_string(my_obj):
    """serializes an object to JSON

        Args:
            my_obj: object to serialize

        Returns: JSON string
    """
    jsons = json.dumps(my_obj)
    return (jsons)
