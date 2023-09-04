#!/usr/bin/python3
"""
This module defines a base class for geometry-related operations.
"""


class BaseGeometry:
    """
    A base class for geometry-related operations.

    This class defines an 'area' method that raises an exception with
    the message 'area() is not implemented.' Subclasses are expected
    to override this method with their own implementations.

    Attributes:
        None.

    Methods:
        area(): An abstract method that raises an Exception
        with the message 'area() is not implemented.'
    """

    def area(self):
        """Raise an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer value.

        Args:
            name (str): The name of the value being validated.
            value: The value to be validated.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
