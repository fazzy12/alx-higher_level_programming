#!/usr/bin/python3
i = 0
for c in range(ord('z'), ord('a') - 1, -1):
    ascii_value = c - 32 if (ord('z') - c) % 2 == 0 else c
    print("{}".format(chr(ascii_value)), end="")
