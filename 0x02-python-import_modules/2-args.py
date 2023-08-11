#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argstr = ""
    argv = sys.argv
    arglen = len(argv) - 1
    i = 1
    if (arglen == 1):
        argstr = "argument:"
    elif (arglen == 0):
        argstr = "arguments."
    else:
        argstr = "arguments:"
    print("{} {}".format(arglen, argstr))
    while (i <= arglen):
        print("{}: {}".format(i, argv[i]))
        i += 1
