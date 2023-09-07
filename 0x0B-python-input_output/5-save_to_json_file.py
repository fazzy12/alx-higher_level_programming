#!/usr/bin/python3
"""This module implements a function that writes an Object to a text file,
using the standard encoding and decoding functions for encoding
and decoding respectively
"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation"""

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
