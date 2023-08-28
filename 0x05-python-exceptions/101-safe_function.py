#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        ret = fct(*args)
    except Exception as exc:
        print("Exception: {}".format(exc.args[0]), file=sys.stderr)
        return (None)
    return (ret)
