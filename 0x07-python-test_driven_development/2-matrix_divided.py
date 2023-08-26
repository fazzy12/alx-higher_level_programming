#!/usr/bin/python3
"""
This module is composed by a function that divides the numbers of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divide a matrix by a number and return a new matrix.

    Args:
        matrix (list of lists): A matrix containing integers or floats.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with each element divided by the divisor,
        rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a valid matrix of
                    integers/floats, or if div is not a number.
        TypeError: If the rows of the matrix do not have the same size.
        ZeroDivisionError: If div is equal to 0.
    """
    matrix_msg = "matrix must be a matrix (list of lists) of integers/floats"
    size_msg = "Each row of the matrix must have the same size"
    new_matrix = []

    if any(not isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError(matrix_msg)

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError(size_msg)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(num // div, 2) for num in row] for row in matrix]
    return new_matrix
