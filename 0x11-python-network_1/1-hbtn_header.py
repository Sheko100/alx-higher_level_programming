#!/usr/bin/python3
"""Module that sends a HTTP request to a specific URL using urllib
"""

from sys import argv
import urllib.request

if __name__ == "__main__":

    url = argv[1]

    with urllib.request.urlopen(url) as res:
        print(res.headers['X-Request-Id'])
