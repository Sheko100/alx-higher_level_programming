#!/usr/bin/python3
def uppercase(str):
    """Converts srting to uppercase"""
    upperstr = ""
    for c in str:
        uni = ord(c)
        upperstr += chr(ord(c) - 32) if (uni > 96 and uni < 123) else c
    print("{}".format(upperstr))
