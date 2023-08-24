#!/usr/bin/python3
"""Square class defined by size and position"""


class Square:
    def __init__(self, size=0):
        """initializes
        Args:
            size (int): size
        Returns: None
        """
        self.size = size

    @property
    def size(self):
        """
        getter of size
        Return:
            Size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter of size
        Args:
            value (int): size
        Raises
            TypeError: if size is not int
            ValueError: size less than 0
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculate area of square
        Returns:
            Area of square
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Compare two squares
        Args:
            other (Square): square to compare
        Returns:
            True if equal, False otherwise
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compare two squares
        Args:
            other (Square): square to compare
        Returns:
            True if not equal, False otherwise
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Compare two squares
        Args:
            other (Square): square to compare
        Returns:
            True if less, False otherwise
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compare two squares
        Args:
            other (Square): square to compare
        Returns:
            True if less or equal, False otherwise
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Compare two squares
        Args:
            other (Square): square to compare
        Returns:
            True if greater, False otherwise
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compare two squares
        Args:
            other (Square): square to compare
        Returns:
            True if greater or equal, False otherwise
        """
        return self.area() >= other.area()
