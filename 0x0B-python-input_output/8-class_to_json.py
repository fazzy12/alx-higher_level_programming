#!/usr/bin/python3
"""Defines a function that returns the dictionary description with simple data
structure (list, dictionary, string, integer and boolean)"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure (list, 
    dictionary, string, integer and boolean) for JSON serialization
    of an object"""

    if not hasattr(obj, "__dict__"):
        return {}
    return obj.__dict__

    serialized = {}
    for key, value in obj.__dict__.items():
        if type(value) in [str, int, bool, list, dict]:
            serialized[key] = value
        else:
            serialized[key] = value.__dict__
    return serialized
