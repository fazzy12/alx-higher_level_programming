#!usr/bin/python3
"""Module for read_file method that reads a file"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
