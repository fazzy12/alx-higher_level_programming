#!/usr/bin/python3
""" Base class for all other classes in this project
"""


class Base:
    """ Base class for all other classes in this project

    Attributes:
        __nb_objects (int): Number of objects created
    """
    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
