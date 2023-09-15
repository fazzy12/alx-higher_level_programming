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

    # Static method to return JSON string representation of list_dictionaries
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

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of a list of instances file.

        Args:
            list_objs (list): A list of instances to be saved to a JSON file.
        """
        if list_objs is None:
            list_objs = []

        file_name = cls.__name__ + ".json"
        with open(file_name, mode="w", encoding="utf-8") as file:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(list_dicts)
            file.write(json_string)

    # Static method to return list of instances from JSON string representation
    @staticmethod
    def from_json_string(json_string):
        """Parse a JSON string representation into a list of dictionaries.

        Args:
            json_string (str): A JSON string representing a list of
            dictionaries.

        Returns:
            list: The list of dictionaries parsed from the JSON string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes set from a dictionary.

        Args:
            **dictionary: A dictionary with attribute names and values.

        Returns:
            Base: An instance of the class with attributes set from
            the dictionary.
        """
        if cls.__name__ == "Rectangle":
            # Create a dummy Rectangle with mandatory attributes
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)  # Create a dummy Square with mandatory attributes
        else:
            raise ValueError("Unsupported class")

        # Use the update method to assign attributes from the dictionary
        dummy.update(**dictionary)
        return dummy
