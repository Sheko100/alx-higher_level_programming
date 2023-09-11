#!/usr/bin/python3
"""Module that presenting a class that inherits from list class
"""


class MyList(list):
    """A subclass of list class
    """
    def print_sorted(self):
        """prints a list in ascending order
        """
        sort_list = list(self)
        sort_list.sort()
        print(sort_list)
