#!/usr/bin/python3
# 1-number_of_lines.py
# ifeanyi kalu
"""Defines a text file line-counting function."""


def number_of_lines(filename=""):
    """Return the number of lines in a text file."""
    lines = 0
    with open(filename) as f:
        for lines in f:
            lines += 1
    return lines
