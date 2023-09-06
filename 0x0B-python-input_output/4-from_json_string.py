#!/usr/bin/python3
"""This module implements a function that returns an object
(Python data structure) represented by a JSON string"
"""


import json


def to_json_string(my_str):
    """Returns an object (Python data structure)
    represented by a JSON string"""

    return json.load(my_str)
