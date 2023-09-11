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


class Rectangle(Base):
    """ Class Rectangle that inherits from Base class

    Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle
        x (int): x coordinate of the rectangle
        y (int): y coordinate of the rectangle
        id (int): id of the rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor method for Rectangle class

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): x coordinate of the rectangle
            y (int): y coordinate of the rectangle
            id (int): id of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
