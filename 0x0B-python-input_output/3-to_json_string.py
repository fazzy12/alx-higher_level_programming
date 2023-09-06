#!/usr/bin/python3
"""Module for to_json_string method that returns the JSON
representation of an object (string)
"""


import json


def to_json_string(my_obj):
    return json.dumps(my_obj)
