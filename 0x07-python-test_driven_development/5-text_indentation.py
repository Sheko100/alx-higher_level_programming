#!/usr/bin/python3
"""Module to add text indentation
"""


def text_indentation(text):
    """Adds a blank line after period, qustion mark and colon

    Args:
        text (str): a string to indent

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    textlen = len(text)
    ch = 0
    while ch < textlen:
        if text[ch] in ".?:":
            print(text[ch])
            print()
            if text[ch + 1] == " ":
                ch += 1
        else:
            print(text[ch], end="")
        ch += 1
