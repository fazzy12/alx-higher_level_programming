#!/usr/bin/python3
"""This module contains a class Student that defines a student"""


class Student():
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

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance

        Args:
            None

        Returns:
            dict: the dictionary representation of a Student instance
        """

        return self.__dict__
