#!/usr/bin/python3
"""Module that sends a HTTP request to a specific URL using urllib
"""

from sys import argv
import urllib.request
import urllib.error

if __name__ == "__main__":

    url = argv[1]

    try:
        with urllib.request.urlopen(url) as res:
            headers = res.headers
            data = res.read()
            print(data.decode('utf-8'))
    except urllib.erro.HTTPError as err:
        print("Error code: {}".format(err.code))
