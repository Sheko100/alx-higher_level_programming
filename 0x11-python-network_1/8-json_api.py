#!/usr/bin/python3
"""Module that sends a HTTP request to a specific URL using urllib
"""

import requests
from sys import argv

if __name__ == "__main__":

    url = "http://0.0.0.0:5000/search_user"
    data = {"q": ""}

    if len(argv) > 1:
        data['q'] = argv[1]

    res = requests.post(url, data)
    if res.status_code == 200:
        try:
            json = res.json()
            if len(json) == 0:
                print("No result")
            elif "id" in json and "name" in json:
                print("[{}], {}".format(json["id"], json["name"]))
        except requests.exceptions.JSONDecodeError:
            print("Not a valid JSON")
