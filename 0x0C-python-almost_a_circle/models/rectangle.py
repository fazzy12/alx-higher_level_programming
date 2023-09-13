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
            x (int, optional): The x-coordinate of the rectangle's
            position. Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle's
            position. Defaults to 0.
            id (int, optional): The id to assign to the instance.
            Defaults to None.
        """
        super().__init__(id)  # Call the constructor of the base class (Base)

        self.width = width  # Use the setter method to validate width
        self.height = height  # Use the setter method to validate height
        self.x = x  # Use the setter method to validate x
        self.y = y  # Use the setter method to validate y

    # Getter for width
    @property
    def width(self):
        return self.__width

    # Setter for width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # Getter for height
    @property
    def height(self):
        return self.__height

    # Setter for height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # Getter for x-coordinate
    @property
    def x(self):
        return self.__x

    # Setter for x-coordinate
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # Getter for y-coordinate
    @property
    def y(self):
        return self.__y

    # Setter for y-coordinate
    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
