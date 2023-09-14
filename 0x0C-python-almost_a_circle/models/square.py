#!/usr/bin/python3
""" Square class, inherits from Rectangle. """

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square (both width and height).
            x (int, optional): The x-coordinate of the square's position.
            Defaults to 0.
            y (int, optional): The y-coordinate of the square's position.
            Defaults to 0.
            id (int, optional): The id to assign to the instance.
            Defaults to None.
        """

        # Call the constructor of the base class (Rectangle)
        super().__init__(size, size, x, y, id)

    # Override the __str__ method to return a custom string representation
    def __str__(self):
        """Return a custom string representation of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    # Override the setter for size to ensure both width and height are updated
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        # if not isinstance(value, int):
        #     raise TypeError("width must be an integer")
        # if value <= 0:
        #     raise ValueError("size must be > 0")
        self.width = value
        self.height = value
