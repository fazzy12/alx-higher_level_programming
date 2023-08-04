#!/usr/bin/python3
"""Print the alphabet in lowercase, not followed by a new line."""
for alpahbets in range(97, 123):
    alpahbets = chr(alpahbets)
    if 'e' in alpahbets or 'q' in alpahbets:
        continue
    print("{:s}".format(alpahbets), end="")
