#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        rowlen = len(row)
        i = 0
        while (i < rowlen):
            print("{:d}".format(row[i]), end="")
            if (i != (rowlen - 1)):
                print(" ", end="")
            i += 1
        print()
