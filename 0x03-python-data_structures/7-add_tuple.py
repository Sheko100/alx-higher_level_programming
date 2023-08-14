#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len1 = len(tuple_a)
    len2 = len(tuple_b)
    reslist = [0, 0]
    i = 0

    while (i < len1 and i < 2):
        reslist[i] += tuple_a[i]
        i += 1
    i = 0
    while (i < len2 and i < 2):
        reslist[i] += tuple_b[i]
        i += 1
    res = (reslist[0], reslist[1])
    return (res)
