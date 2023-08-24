#!/usr/bin/python3
""" Module that defines a class Node """


class Node:
    """ Class that defines a node """
    def __init__(self, data, next_node=None):
        """ Class constructor """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Getter method for data attribute """
        return self.__data

    @data.setter
    def data(self, value):
        """ Setter method for data attribute """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """ Getter method for next_node attribute """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Setter method for next_node attribute """
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """This class defines a singly linked list"""

    def __init__(self):
        """Initialize an empty singly linked list"""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position"""
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Convert the linked list to a string for printing"""
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
