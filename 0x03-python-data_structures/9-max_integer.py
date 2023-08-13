#!/usr/bin/python3
def max_integer(my_list=[]):
    maxnum = 0
    if (len(my_list) == 0):
        return (None)
    for n in my_list:
        if (n > maxnum):
            maxnum = n
    return (maxnum)
