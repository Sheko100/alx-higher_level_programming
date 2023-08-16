#!/usr/bin/python3
def best_score(a_dictionary):
    best = 0
    name = ""
    if (a_dictionary == None):
        return (None)
    for k, v in a_dictionary.items():
        if (v > best):
            name, best = k, v
    return (name)
