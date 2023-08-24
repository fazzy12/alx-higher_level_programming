#!/usr/bin/python3
""" Module that defines a class Square """


class Square:
    """This class defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with optional size and position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square"""
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(val, int) for val in value) \
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#' and position"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

# def __str__(self):
#     """Convert the square to a string for printing"""
#     result = ""
#     for _ in range(self.__position[1]):
#         result += "\n"
#     for _ in range(self.__size):
#         result += " " * self.__position[0] + "#" * self.__size
#         if _ < self.__size - 1:
#             result += "\n"
#     return result


def __str__(self):
    """
    defining printing behavior of the class
    """
    if self.__size == 0:
        return ""
    new_lines = '\n' * self.__position[1]
    result = " " * self.__position[0] + "#" * self.__size
    return new_lines + '\n'.join(result + "#" for e in range(self.__size))
