#!/usr/bin/python3
"""
Module defines a function that checks if an object is an instance of a
"""


def is_same_class(obj, a_class):
    """Check if 'obj' is exactly an instance of 'a_class'.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if 'obj' is an instance of 'a_class', otherwise False.
    """
    if type(obj) == a_class:
        return True
    return False
