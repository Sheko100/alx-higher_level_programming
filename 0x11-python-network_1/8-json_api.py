#!/usr/bin/python3
"""sends a POST request to http://0.0.0.0:5000/search_user with
a letter as a parameter
"""
import requests
from sys import argv
q = argv[1] if len(argv) > 1 else ""
res = requests.post("http://0.0.0.0:5000/search_user", json={'q': q})
try:
    json = res.json()
    if len(json) == 0:
        print("No result")
    else:
        print("[{}] {}".format(json.get("id"), json.get("name")))
except requests.exceptions.JSONDecodeError as err:
    print("Not a valid JSON")
