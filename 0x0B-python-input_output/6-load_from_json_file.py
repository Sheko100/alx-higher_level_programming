#!/usr/bin/python3
"""Module for creating an object from JSON in text file
"""
import json


def load_from_json_file(filename):
    """creates an object from JSON in a text file

    Args:
        filename: file path
    """
    with open(filename, encoding="utf-8") as jsonfile:
        jsons = jsonfile.read()
        obj = json.loads(jsons)

    return obj
