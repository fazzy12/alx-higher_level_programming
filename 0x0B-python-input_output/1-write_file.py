#!/usr/bin/python3
"""Module for write_file method that writes a string to a text file"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of"""
    with open(filename, "w", encoding="utf=8") as file:
        return file.write(text)
