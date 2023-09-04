#!/usr/bin/python3
"""
The list module contains the class MyList.
"""


class MyList(list):
    """
    A custom list class that inherits from the built-in 'list' class.

    This class adds a 'print_sorted' method to print the list in
    ascending sorted order.

    Attributes:
        No additional attributes.

    Methods:
        print_sorted(): Print the list elements in ascending sorted order.
    """


def print_sorted(self):
    """
    Print the list elements in ascending sorted order.

    """

    print(sorted(self))
