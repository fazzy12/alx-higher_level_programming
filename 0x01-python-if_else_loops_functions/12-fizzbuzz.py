#!/usr/bin/python3
def fizzbuzz():
    """Print numbers from 1 to 100 separated by a space."""
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("{}".format("FizzBuzz"), end=" ")
        elif i % 3 == 0:
            print("{}".format("Fizz"), end=" ")
        elif i % 5 == 0:
            print("{}".format("Buzz"), end=" ")
        else:
            print("{}".format(i), end=" ")
