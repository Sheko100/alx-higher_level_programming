#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    to_delete = []
    for k, v in a_dictionary.items():
        if (v == value):
            to_delete.append(k)
    for key in to_delete:
        del a_dictionary[key]
    return (a_dictionary)
