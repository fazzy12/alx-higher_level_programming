#!/usr/bin/python3
"""
    This module provides a function to print a square made of '#' characters.
"""


def print_square(size):
    """
    Print a square made of '#' characters.

    This function takes an integer `size` as input and prints a square pattern
    made of '#' characters. The square has `size` rows and `size` columns.

    Args:
        size (int): The size of the square to be printed.

    Raises:
        TypeError: If `size` is not an integer.
        ValueError: If `size` is less than 0.
        TypeError: If `size` is a negative float.

    Note:
        - The function raises appropriate exceptions to handle invalid input.
        - The square is printed using '#' characters.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for _ in range(size):
            print("#" * size)
