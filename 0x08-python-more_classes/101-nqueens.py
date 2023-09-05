#!/usr/bin/python3
"""Module that solving N queens puzzle
"""
import sys


argv = sys.argv
if len(argv) != 2:
    print("Usage: nqueens N", file=sys.stderr)
    sys.exit(1)
try:
    n = int(argv[1])
except ValueError:
    print("N must be a number", file=sys.stderr)
    sys.exit(1)

if n < 4:
    print("N must be at least 4", file=sys.stderr)
    sys.exit(1)

base = [0, 1]
delta = base[1] + 1
col, row = base[0], base[1]
squares = [base]
tempcol = base[0]
temprow = base[1]

while True:
    col = col + 1
    row = row + delta
    print(row)
    if col >= n:
        col = 0
    if row >= n:
        row = 0
    if col == base[0]:
        col += 1
    if row == base[1]:
        row += 1
    square = [col, row]
    squares.append(square)
    if (len(squares) == n):
        print(squares)
        base[1] += 1
        delta = base[1] + 1
        squares = [base]
        col = base[0]
        row = base[1]
    if base[1] == (n - 1):
        break
