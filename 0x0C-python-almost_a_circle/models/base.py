#!/usr/bin/python3
""" Base class for all other classes in this project
"""
import json


class Base:
    """Base class for managing id attribute."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance.

        Args:
            id (int, optional): The id to assign to the instance.
            Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # Static method to return the JSON string representation of list_dictionaries
    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries
            to be converted to JSON.

        Returns:
            str: The JSON string representation of the input
            list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
