#!/usr/bin/python3
"""
    This module provides a function to print a formatted
    message with names.
"""


def say_my_name(first_name, last_name=""):
    """
    Print a formatted message with the provided first and last names.

    This function takes the first name and an optional last name as arguments,
    and prints a message in the format "My name is <first_name> <last_name>".

    Args:
        first_name (str): The first name to be included in the message.
        last_name (str, optional): The last name to be included in the message.
            Defaults to an empty string.

    Raises:
        TypeError: If either `first_name` or `last_name` is not a string.

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
