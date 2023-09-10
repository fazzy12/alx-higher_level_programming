#!/usr/bin/python3
""" Base class for all other classes in this project
"""


class Base:
    """ Base class for all other classes in this project

    Attributes:
        __nb_objects (int): Number of objects created
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
