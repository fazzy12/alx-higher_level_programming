#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # .pop() returns the value of the removed item
    a_dictionary.pop(key, None)
    return a_dictionary
