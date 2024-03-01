#!/usr/bin/python3
"""Module that sends a HTTP request to a specific URL using urllib
"""

import requests
from sys import argv

if __name__ == "__main__":

    url = argv[1]

    res = requests.get(url)
    if res.status_code > 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
