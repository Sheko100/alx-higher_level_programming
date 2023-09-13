#!/usr/bin/python3
"""Module for adding all arguments to a list and save them in a file
"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

argv = sys.argv
args = []
for arg in argv[1:]:
    args.append(arg)

with open("add_item.json", mode="w", encoding="utf-8") as file:
    jsons = json.dumps(args)
    wrtten = file.write(jsons)
