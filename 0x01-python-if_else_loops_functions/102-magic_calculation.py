#!/usr/bin/python3

def magic_calculation(a, b, c):
    """Perform a magic calculation based on the given values.

    The function takes three arguments a, b, and c, and returns a value based
    on the following rules:
    1. If a is less than b, it returns the value of c.
    2. If c is greater than b, it returns the sum of a and b.
    3. If none of the above conditions are met, it returns the result of
       a * b - c.

    Args:
        a (int): The first integer value.
        b (int): The second integer value.
        c (int): The third integer value.

    Returns:
        int: The result of the magic calculation.

    Example:
        >>> magic_calculation(3, 5, 8)
        8
        >>> magic_calculation(5, 3, 8)
        11
        >>> magic_calculation(5, 8, 3)
        7
    """

    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return a * b - c
