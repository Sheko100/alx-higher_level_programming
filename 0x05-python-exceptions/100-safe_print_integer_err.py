#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as exc:
        print("Exception: {}".format(exc.args[0]), file=sys.stderr)
        return (False)
    return (True)
