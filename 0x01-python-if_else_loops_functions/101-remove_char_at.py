#!/usr/bin/python3
def remove_char_at(str, n):
    strcpy = ""
    i = 0
    for c in str:
        if (n == i):
            i += 1
            continue
        strcpy += c
        i += 1
    return (strcpy)
