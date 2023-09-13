#!/usr/bin/python3
"""Rectangle class, inherits from Base."""

from models.base import Base


class Rectangle(Base):
    """Rectangle class, inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position.
            Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle's position.
            Defaults to 0.
            id (int, optional): The id to assign to the instance.
            Defaults to None.
        """
        super().__init__(id)  # Call the constructor of the base class (Base)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    # Getter for width
    @property
    def width(self):
        return self.__width

    # Setter for width
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be greater than 0")
        self.__width = value

    # Getter for height
    @property
    def height(self):
        return self.__height

    # Setter for height
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be greater than 0")
        self.__height = value

    # Getter for x-coordinate
    @property
    def x(self):
        return self.__x

    # Setter for x-coordinate
    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError("X-coordinate cannot be negative")
        self.__x = value

    # Getter for y-coordinate
    @property
    def y(self):
        return self.__y

    # Setter for y-coordinate
    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError("Y-coordinate cannot be negative")
        self.__y = value
