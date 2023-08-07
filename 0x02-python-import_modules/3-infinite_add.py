#!/usr/bin/python3
import sys

if __name__ == "__main__":

    args = sys.argv[1:]  # Get command-line arguments excluding the script name
    result = sum(int(arg) for arg in args)  # Sum all the integer arguments

print("{}".format(result))
