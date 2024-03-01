#!/usr/bin/python3
"""Module that sends a HTTP request to a specific URL using requests
"""

import requests
from sys import argv

if __name__ == "__main__":

    url = argv[1]

    res = requests.get(url)
    print(res.headers['X-Request-Id'])
