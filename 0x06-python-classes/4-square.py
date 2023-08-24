#!/usr/bin/python3
""" This module defines a Square class"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        self.__size = size

    # getter
    @property
    def size(self):
        """Retrieves the size"""
        return self.__size

    # setter
    @size.setter
    def size(self, value):
        """Sets the size value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    # calculate are of square
    def area(self):
        """Returns the current square area"""
        return self.__size ** 2
