#!/usr/bin/python3
"""Module that connects with github API
"""

import requests
from sys import argv

if __name__ == "__main__":

    uname = argv[1]
    url = "https://api.github.com/user"
    pwd = argv[2]
    auth = "Bearer {}".format(pwd)
    headers = {"Authorization": auth}

    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        try:
            json = res.json()
            if len(json) == 0:
                print("No result")
            elif "id" in json:
                print("{}".format(json["id"]))
        except ValueError:
            print("Not a valid JSON")
