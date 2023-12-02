#!/usr/bin/python3
"""sends a POST request to the passed URL with the email and
displays the body of the response
"""
import urllib.parse
import urllib.request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    with urllib.request.urlopen(argv[1], data) as res:
        html = res.read()
        print(html.decode("ascii"))
