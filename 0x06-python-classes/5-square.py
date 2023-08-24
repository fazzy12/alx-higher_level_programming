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

    # print square
    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
