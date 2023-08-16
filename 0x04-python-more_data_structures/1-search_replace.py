#!/usr/bin/python3
def search_replace(my_list, search, replace):
    isthenum = lambda num, search, replace: replace if num == search else num
    new_list = [isthenum(n, search, replace) for n in my_list]
    return (new_list)
