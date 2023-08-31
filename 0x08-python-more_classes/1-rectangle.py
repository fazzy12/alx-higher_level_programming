#!/usr/bin/python3
"""
This module defines the Rectangle class, which represents
a geometric rectangle.

Classes:
    Rectangle: A geometric shape with width and height properties.

Attributes:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.

Methods:
    __init__(width=0, height=0): Initializes a Rectangle instance with given
    width and height.
    width(): Getter method to retrieve the width of the rectangle.
    width(value): Setter method to set the width of the rectangle.
    height(): Getter method to retrieve the height of the rectangle.
    height(value): Setter method to set the height of the rectangle.

Raises:
    TypeError: If width or height is not an integer.
    ValueError: If width or height is less than 0.
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method to retrieve the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method to set the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Getter method to retrieve the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method to set the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
