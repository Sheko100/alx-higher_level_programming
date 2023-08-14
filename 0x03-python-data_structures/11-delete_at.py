#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    listlen = len(my_list)
    if (idx < 0 or idx >= listlen):
        return (my_list)
    del my_list[idx]
    return (my_list)
