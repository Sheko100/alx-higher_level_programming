#!/usr/bin/python3
"""Module that sends a HTTP request using POST with email as data
"""

from sys import argv
import urllib.request

if __name__ == "__main__":

    url = argv[1]
    email = argv[2]
    data = {"email": email}
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        content = res.read()
        print(content.decode('utf-8'))
