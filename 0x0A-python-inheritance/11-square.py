#!/usr/bin/python3
"""Module containing the `Rectangle` class inheriting
from `BaseGeometry` class."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A class representing a square, inheriting from Rectangle.

    Attributes:
        None (size is a private attribute).

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: If size is not a positive integer.

    Note:
        The Square class inherits from Rectangle and enforces
        positive integer validation for size. The square is a special case
        of a rectangle where the width and height are equal.
    """

    def __init__(self, size):
        """Initialize a Square instance with a given size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.size = size
