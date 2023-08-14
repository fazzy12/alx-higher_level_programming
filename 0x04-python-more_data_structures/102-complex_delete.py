#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_remove = []

    for key, val in a_dictionary.items():
        if val == value:
            keys_to_remove.append(key)

    for key in keys_to_remove:
        del a_dictionary[key]

    return a_dictionary
