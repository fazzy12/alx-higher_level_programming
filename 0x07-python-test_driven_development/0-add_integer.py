#!/usr/bin/python3
"""This module adds two integers or floats together"""

def add_integer(a, b=98):
    """
    This function adds two integers or floats together.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Returns:
        int: The sum of the two numbers.

    Raises:
        TypeError: If either a or b is not an integer or a float.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
