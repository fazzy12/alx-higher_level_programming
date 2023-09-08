#!/usr/bin/python3
"""This module contains a function that inserts a line of text to a file,
after the specified line number of text has been inserted intothe file"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after the specified line number
    of text has been inserted intothe file and returns nothing (void)
    otherwise returns nothing (void)
    """

    with open(filename, 'r+') as f:
        lines = f.readlines()
        new_lines = []
        for line in lines:
            new_lines.append(line)
            if search_string in line:
                new_lines.append(new_string)
        f.seek(0)
        f.writelines(new_lines)
