#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    res = requests.get(url)
    if res.status_code > 200:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
