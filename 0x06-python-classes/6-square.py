#!/usr/bin/python3
""" This module defines a Square class"""


class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    # getter
    @property
    def position(self):
        """Return the position"""
        return self.__position

    # setter
    @position.setter
    def position(self, value):
        """Sets the position value"""
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    # print square with position
    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

