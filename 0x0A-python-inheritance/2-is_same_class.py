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
    if isinstance(obj, a_class):
        return True
    else:
        return False


a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))
