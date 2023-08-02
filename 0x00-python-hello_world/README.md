# 0x00. Python - Hello, World
This repository contains a series of Python scripts that cover various topics related to the basics of Python programming.
Each script is designed to demonstrate a specific concept or solve a particular problem.

1. [Run Python file]()
* A Shell script (0-run) that runs a Python script specified in the environment variable $PYFILE. The Python script prints "Best School" when executed.

2. [Run inline]()
* A Shell script (1-run_inline) that runs Python code specified in the environment variable $PYCODE. The Python code prints "Best School: 98" when executed.

3. [Hello, print]()
* A Python script (2-print.py) that uses the print function to display the message "Programming is like building a multilingual puzzle" followed by a new line.

4. [Print integer]()
* A Python script (3-print_number.py) that prints the integer stored in the variable number followed by the string 
  "Battery street" and a new line. The variable number is not cast into a string, and f-strings are used.

5. [Print float]()
* A Python script (4-print_float.py) that prints the float stored in the variable number with a precision of 2 digits. F-strings are used, and the variable number is not cast into a string.

6. [Print string]()
* A Python script (5-print_string.py) that prints the value of the variable str three times, followed by a new line, 
  and then prints the first 9 characters of the variable str, followed by a new line. No loops or conditional statements are used.

7. [Play with strings]()
* A Python script (7-edges.py) that manipulates the variable word to extract substrings word_first_3, word_last_2, and middle_word based on specific conditions.

8. [Create a new sentence]()
* A Python script (8-concat_edges.py) that prints "object-oriented programming with Python" followed by a new line, using the variables str1, str2, and the slicing technique.

9. [Easter Egg]()
* A Python script (9-easter_egg.py) that prints "The Zen of Python" by Tim Peters, which is a collection of guiding principles for writing computer programs in Python.

10. [Linked list cycle]()
* A C function (10-check_cycle.c) that checks if a singly linked list has a cycle. The function returns 1 if there
  is a cycle and 0 if there is no cycle. The function uses pointers and does not require loops or conditional statements.

11. [Hello, write]()
* A Python script (100-write.py) that prints "and that piece of art is useful - Dora Korpar, 2015-10-19" to the standard error output (stderr) and exits with a status code of 1.

12. [Compile]()
* A Shell script (101-compile) that compiles a Python script specified in the environment variable $PYFILE. The compiled output is saved with a ".pyc" extension (e.g., if $PYFILE is "main.py," then "main.pyc" is created).

13. [ByteCode -> Python #1]()
* A Python function (102-magic_calculation.py) that performs the same operations as the given Python bytecode. 
The bytecode calculates 98 raised to the power of a, adds b to the result, and returns the final value.




Please refer to each script's file for more detailed explanations and code implementation. Happy learning and coding!


## Usage

Follow these steps to run the "Hello, World" Python script:

1. Clone this repository to your local machine.

```
git clone https://github.com/your-username/0x00-Python-Hello-World.git
```

2. Change into the project directory.

```
cd 0x00-Python-Hello-World
```
3. Set the environment variable $PYFILE to the name of the Python script you want to execute.
```
export PYFILE=hello_world.py
```
 Replace hello_world.py with the name of your Python script.

4. Run the Shell script to execute the Python script.
```
./run_python_script.sh
```
The `"Hello, World"` message should be displayed in the terminal.

## Support
If you encounter any issues or have questions regarding this project, please open an issue on the repository.

## Contributing
We welcome contributions to improve this project and help others learn Python. To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch with your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request to this repository.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
