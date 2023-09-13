#!/usr/bin/python3
"""Module to append string to a file
"""


def append_write(filename="", text=""):
    """appends string to an UTF8 text file

    Args:
        filename (str): file path
        text (str): text to write

    Returns: number of characters written
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        written = file.write(text)

    return (written)
