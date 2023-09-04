#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """Check if 'obj' is an instance of, or inherits from, 'a_class'.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if 'obj' is an instance of 'a_class' or inherits from it,
        otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    return False
