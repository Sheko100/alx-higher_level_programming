#!/usr/bin/python3
"""Module for adding all arguments to a list and save them in a file
"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
args = []
argv = sys.argv
if len(argv) > 1:
    obj = load_from_json_file(filename)
    for ele in obj:
        args.append(ele)
    for arg in argv[1:]:
        args.append(arg)
    save_to_json_file(args, filename)
else:
    save_to_json_file([], filename)
"""jsons = file.readline()
    print(len(jsons))
    if len(jsons) > 0:
        print(args)
        obj = json.loads(jsons)
        for ele in obj:
            args.append(ele)
    for arg in sys.argv[1:]:
        args.append(arg)
    jsons = json.dumps(args)
    wrtten = file.write(jsons)
"""
