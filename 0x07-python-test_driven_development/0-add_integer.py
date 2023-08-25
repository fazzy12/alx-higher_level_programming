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

    Examples:
        >>> add_integer(3, 5)
        8

        >>> add_integer(2.5, 3.5)
        6

        >>> add_integer(5, 3.5)
        8

        >>> add_integer(-5, -10)
        -15

        >>> add_integer(-2.5, -3.5)
        -6

        >>> add_integer(5, -10)
        -5

        >>> add_integer(-2.5, 3.5)
        1

        >>> add_integer(7)
        105

        >>> add_integer("5", 3)
        Traceback (most recent call last):
            ...
        TypeError: a must be an integer

        >>> add_integer(5, "3")
        Traceback (most recent call last):
            ...
        TypeError: b must be an integer

        >>> add_integer("5", "3")
        Traceback (most recent call last):
            ...
        TypeError: a must be an integer
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
