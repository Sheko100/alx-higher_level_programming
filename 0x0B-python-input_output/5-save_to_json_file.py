#!/usr/bin/python3
"""Module for writing an object to a text file in JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """writes object as JSON to a text file

    Args:
        my_obj: object to write
        filename: file path
    """
    jsons = json.dumps(my_obj)
    with open(filename, mode="w", encoding="utf-8") as file:
        written = file.write(jsons)
