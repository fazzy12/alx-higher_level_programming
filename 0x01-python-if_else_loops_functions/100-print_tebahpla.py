#!/usr/bin/python3

for ascii_value in range(ord('Z'), ord('a') - 1, -1):
    character = chr(ascii_value)
    if (ord('Z') - ascii_value) % 2 == 0:
        character = character.lower()
    print("{}".format(character), end="")
