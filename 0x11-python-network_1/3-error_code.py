#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response
"""
import urllib.request
import urllib.error
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    try:
        with urllib.request.urlopen(argv[1]) as res:
            html = res.read()
            print(html.decode("ascii"))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
