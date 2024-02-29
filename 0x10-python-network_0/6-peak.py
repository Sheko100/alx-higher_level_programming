#!/usr/bin/python3
"""Module contains a function that prints the peak of integers list
"""


def find_peak(list_of_integers):
    """Searchs and prints the peak (integer greater than its neighbors) of an
    unsorted list of integers

    Args:
        list_of_integers: list of unsorted integers integers
    """
    length = len(list_of_integers)
    i = 1

    if length > 2:
        while i < length - 1:
            left = list_of_integers[i-1]
            mid = list_of_integers[i]
            right = list_of_integers[i+1]

            if mid >= left and mid >= right:
                return mid
            i += 1
    else:
        return None
