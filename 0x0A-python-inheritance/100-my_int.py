#!/usr/bin/python3
"""Module containing the `MyInt` class inheriting from `int` class."""


class MyInt(int):
    """A custom integer class with inverted equality and inequality operators.

    This class inherits from the built-in `int` class but changes the behavior
    of the equality (==) and inequality (!=) operators. When comparing
    instances of `MyInt`, these operators return inverted results compared
    to standard integers.

    Attributes:
        None

    Methods:
        __eq__(self, other): Override the equality operator (==) to return the
        inverted result.
        __ne__(self, other): Override the inequality operator (!=) to return
        the inverted result.
    """

    def __eq__(self, other):
        """Override the equality operator (==) to return the inverted result.

        Args:
            other (int or MyInt): The object to compare with.

        Returns:
            bool: True if the objects are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the inequality operator (!=) to return the inverted result.

        Args:
            other (int or MyInt): The object to compare with.

        Returns:
            bool: True if the objects are equal, False otherwise.
        """
        return super().__eq__(other)
