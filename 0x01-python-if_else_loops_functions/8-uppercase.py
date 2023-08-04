#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase followed by a new line."""
    for custom_str in str():
        if ord(custom_str) >= 97 and ord(custom_str) <= 122:
            uppercase_char = chr(ord(custom_str) - 32)
        print("{}".format(uppercase_char), end="")
    print("")
