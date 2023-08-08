# CPython #0: Python Lists
`CPython` is the reference implementation of the `Python` programming language, written in `C`. This task involves creating a `C` function that provides some basic information about `Python lists`. By examining the underlying `C` implementation of `Python`, we can gain insights into how `lists` work in the language.

## Task Details
Create a `C` function called `print_python_list_info` that prints information about a `Python list`. The details to be printed include:

- Size of the Python List (number of elements)
- Allocated memory (number of slots)
- Type of elements in the list

The provided Python version for this task is `3.4``. The shared library containing the `C` function will be compiled using the following command:

```
gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c
```
The `Python` `script` `100-test_lists.py` demonstrates the usage of the `C` `function`. It creates and manipulates `Python lists`, calling the `print_python_list_info` function to display relevant information about the `lists`.


## Files

[0-print_list_integer.py]()
- Description: Python script to print a list of integers, one per line.
- Usage: `./0-main.py`

[1-element_at.py]()
- Description: Python script to retrieve an element from a list at a specific index.
- Usage: `./1-main.py`

[2-replace_in_list.py]()
- Description: Python script to replace an element in a list at a specific position.
- Usage: `./2-main.py`

[3-print_reversed_list_integer.py]()
- Description: Python script to print a list of integers in reverse order.
- Usage: `./3-main.py`

[4-new_in_list.py]()
- Description: Python script to replace an element in a list at a specific position without modifying the original list.
- Usage: `./4-main.py`

[5-no_c.py]()
- Description: Python script to remove all occurrences of characters 'c' and 'C' from a string.
- Usage: `./5-main.py`

[6-print_matrix_integer.py]()
- Description: Python script to print a matrix of integers.
- Usage: `./6-main.py`

[7-add_tuple.py]()
- Description: Python script to add two tuples element-wise.
- Usage: `./7-main.py`

[8-multiple_returns.py]()
- Description: Python script to return the length of a string and its first character.
-Usage: `./8-main.py`

[9-max_integer.py]()
- Description: Python script to find the maximum integer in a list.
- Usage: `./9-main.py`

[10-divisible_by_2.py]()
- Description: Python script to determine if elements in a list are divisible by 2.
- Usage: `./10-main.py`

[11-delete_at.py]()
- Description: Python script to delete an element at a specific index in a list.
- Usage: `./11-main.py`

[12-switch.py]()
- Description: Python script to switch the values of two variables.
- Usage: `./12-switch.py`

[13-is_palindrome.c]()
- Description: C function to check if a singly linked list is a palindrome.
- Usage: Compile and run the provided test script.

[100-print_python_list_info.c]()
- Description: C function to print basic information about Python lists.
- Usage: Compile the shared library and run the provided Python test script.

#### Additional Files

[lists.h]()
Description: Header file containing structure definitions and function prototypes for the linked list tasks.


## How to Run

Compile the shared library:
````
gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c
````
Run the Python script:

``````
python3 100-test_lists.py
``````
The output of the script will display information about the Python `lists` created and manipulated using the `C` function.

## Requirements

- `C` compiler `(gcc)`
- `Python 3.4`
- `ctypes` library (used for interfacing with shared `C` libraries in `Python`)

## Additional Information
This task offers insights into the inner workings of Python lists by examining their C-level implementation. By understanding how lists are structured and allocated in memory, we can appreciate the efficiency and versatility of this fundamental data structure in Python.

## Author
[ifeanyi kalu](http://github.com/fazzy12)

Copyright © 2023 ALX