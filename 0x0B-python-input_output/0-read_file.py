#!/usr/bin/python3
"""Module to read a file
"""


def read_file(filename=""):
    """reads and prints a UTF8 text file to stdout

    Args:
        filename: path to the text file
    """
    with open(filename, encoding="utf-8") as file:
        data = file.read()
    print(data, end='')
