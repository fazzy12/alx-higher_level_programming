#!/usr/bin/python3
"""This module contains a function that returns a list of lists of integers
representing the Pascal's Triangle of a given number of rows"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal's Triangle
    of a given number of rows
    
    Args:
        n (int): the number of rows of Pascal's Triangle to generate
        
    Returns:
        list: a list of lists of integers representing the Pascal's Triangle
            of a given number of rows
    """

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[-1]

        for j in range(1, i):
            value = prev_row[j - 1] + prev_row[j]
            row.append(value)

        row.append(1)
        triangle.append(row)

    return triangle
