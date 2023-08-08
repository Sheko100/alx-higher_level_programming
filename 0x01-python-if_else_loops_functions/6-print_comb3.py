#!/usr/bin/python3
for t in range(0, 10):
    for s in range(1, 10):
        if (t >= s):
            continue
        elif (t == 8):
            print("{}{}".format(t, s))
        else:
            print("{}{}, ".format(t, s), end="")
