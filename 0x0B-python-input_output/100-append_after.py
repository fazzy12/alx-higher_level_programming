#!/usr/bin/python3
"""This module contains a function that inserts a line of text to a file, 
after the specified line number of text has been inserted intothe file"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after the specified line number of text
    has been inserted intothe file and returns nothing (void) otherwise returns nothing (void) 
    """
    
    if not filename or not search_string or not new_string:
        return

    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)

        for line in lines:
            file.write(line)

            if search_string in line:
                file.write(new_string + '\n')
