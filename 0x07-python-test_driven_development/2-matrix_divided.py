#!/usr/bin/python3
"""Module to divide a matrix.
"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix

    Args:
        matrix (2D list): list that contains lists of integers or floats
        div (int/float): a number to divide by

    Returns:
            a matrix contains the result values

    Raises:
        TypeError: if matrix is not a list of lists.
            if matrix lists are not equal in length.
            if div is neither an int nor float.
        ZeroDivisionError: if div is zero
    """
    err = "matrix must be a matrix (list of lists) of integers/floats"
    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list):
        raise TypeError(err)
    elif len(matrix) > 0 and isinstance(matrix[0], list):
        rowsize = len(matrix[0])
        if (rowsize < 1):
            raise TypeError(err)
    else:
        raise TypeError(err)

    newmatrix = []
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(err)
        elif len(row) < 1 or len(row) != rowsize:
            raise TypeError(err)
        newlist = []
        for col in row:
            if not isinstance(col, int) and not isinstance(col, float):
                raise TypeError(err)
            newlist.append(round(col / div, 2))
        newmatrix.append(newlist)
    return (newmatrix)
