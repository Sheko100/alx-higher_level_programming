#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    res = 0
    i = 1
    arg = sys.argv
    arglen = len(arg)
    while (i < arglen):
        res += int(arg[i])
        i += 1
    print("{}".format(res))
