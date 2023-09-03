#!/usr/bin/python3
"""The list module contains the class list"""


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



    def __init__(self):
        return super().__init__()


def print_sorted(self):
    """
    Print the list elements in ascending sorted order.

    Usage:
        my_list = MyList([4, 2, 7, 1, 5])
        my_list.print_sorted()  # Output: [1, 2, 4, 5, 7]
    """
    sorted_list = sorted(self)
    print(sorted_list)
