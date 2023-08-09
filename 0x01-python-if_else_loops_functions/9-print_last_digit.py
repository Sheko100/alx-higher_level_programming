#!/usr/bin/python3
def print_last_digit(number):
    """prints the last digit"""
    lastdigit = -(number % -10) if (number < 0) else number % 10
    print("{}".format(lastdigit), end="")
    return (lastdigit)
