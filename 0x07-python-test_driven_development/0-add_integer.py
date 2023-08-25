#!/usr/bin/python3
"""This module adds two integers or floats together"""

def add_integer(a, b=98):
    """This function adds two integers or floats together"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
