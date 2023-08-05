#!/usr/bin/python3

for ascii_value in range(ord('z'), ord('a') - 1, -1):
    character = chr(ascii_value)
    if ascii_value % 3 - 1 == 0:
        character = character.upper()
    print("{}".format(character), end="")
