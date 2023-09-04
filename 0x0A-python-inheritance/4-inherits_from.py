#!/usr/bin/python3
"""This module checks if s subclass was inherited from a class
"""


def inherits_from(obj, a_class):
    """Check if 'obj' is an instance of a class that inherits from 'a_class'.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if 'obj' is an instance of a class that inherits from 'a_class',
        otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
