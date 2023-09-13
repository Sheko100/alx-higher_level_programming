#!/usr/bin/python3
"""Module to write to a file
"""

def write_file(filename="", text=""):
    """writes a string to an UTF8 text file

    Args:
        filename (str): file path
        text (str): text to write

    Returns: number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        written = file.write(text)

    return (written)
