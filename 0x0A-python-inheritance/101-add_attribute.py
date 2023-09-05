#!/usr/bin/python3
"""This module contains functions for adding attributes to objects."""


def add_attribute(obj, attr_name, attr_value):
    """Add a new attribute to an object if possible, otherwise raise TypeError.

    Args:
        obj: The object to which the attribute will be added.
        attr_name (str): The name of the new attribute.
        attr_value: The value of the new attribute.

    Raises:
        TypeError: If the object cannot have new attributes.
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
