#!/usr/bin/python3

if __name__ == "__main__":
    # import all the calc functions fom calculator_1.py
    from calculator_1 import add, sub, mul, div

    # the value 10 to a variable a
    a = 10
    # the value 5 to a variable b
    b = 5

    # print the result of the addition of a and b
    print("{} + {} = {}".format(a, b, add(a, b)))
    # print the result of the subtraction of a and b
    print("{} - {} = {}".format(a, b, sub(a, b)))
    # print the result of the multiplication of a and b
    print("{} * {} = {}".format(a, b, mul(a, b)))
    # print the result of the division of a and b
    print("{} / {} = {}".format(a, b, div(a, b)))
