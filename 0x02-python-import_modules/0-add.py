#!/usr/bin/python3
from add_0 import add

def main():
    """Main function to execute the addition.

    This function imports the `add` function from the `add_0.py` module,
    performs the addition of two numbers, and prints the result.
    """
    a = 1
    b = 2

    # Call the add function to get the result
    result = add(a, b)

    # Display the result
    print("{} + {} = {}".format(a, b, result))

if __name__ == "__main__":
    main()
