#!/usr/bin/python3
"""Square class defined by size and position"""


class Square:
    def __init__(self, size=0):
        """Initialize a square instance
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

    def __eq__(self, other):
        """Compare if two squares have equal areas"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare if two squares have different areas"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Compare if the area of the first square
                is greater than the second"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare if the area of the first square is
                greater than or equal to the second"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Compare if the area of the first square is less than the second"""
        return self.area() < other.area()

    def __le__(self, other):
        """Compare if the area of the first square is
                less than or equal to the second"""
        return self.area() <= other.area()
