#!/usr/bin/python3
"""This module contains a class Student that defines a student"""


class Student:
    """Defines a student with a first name, last name, and age"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new student

        Args:
            first_name (str): the student's first name
            last_name (str): the student's last name
            age (int): the student's age

        Returns:
            None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance

        Args:
            attrs (list, optional): List of attribute names to retrieve.
                If provided, only these attributes will be included
                    in the dictionary.
                If None, all attributes will be included.

        Returns:
            dict: The dictionary representation of a Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {
                attr: getattr(self, attr)
                for attr in attrs
                if hasattr(self, attr)
            }

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance with ones in json

        Args:
            json (dict): dictionary of attributes to replace in the instance

        Returns:
            None
        """
        for attr, value in json.items():
            setattr(self, attr, value)
