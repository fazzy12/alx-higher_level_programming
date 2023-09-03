<div style="width: 100%; height: 0; padding-bottom: 100%; position: relative;">
    <img src="Inheritance.png" alt="OOP Image" style="position: absolute; width: 100%; height: 100%; object-fit: cover;">
</div>

# Python - Inheritance

In this project, I explored Python class inheritance, including superclass and subclass relationships, multiple base classes, and method/attribute overrides.

## Tests :heavy_check_mark:

* [tests](./tests): This folder contains both Holberton-provided tests and additional independently-developed tests:
    * [1-my_list.txt](./1-my_list.txt)
    * [7-base_geometry.txt](./7-base_geometry.txt)

## Function Prototypes :floppy_disk:

Function prototypes for this project:

| File                    | Prototype                             |
| ----------------------- | ------------------------------------- |
| [0-lookup.py](./0-lookup.py)           | `def lookup(obj):`                    |
| [1-my_list.py](./1-my_list.py)    | `class MyList(list):`                 |
| [2-is_same_class.py](./2-is_same_class.py) | `def is_same_class(obj, a_class):`    |
| [3-is_kind_of_class.py](./3-is_kind_of_class.py) | `def is_kind_of_class(obj, a_class):` |
| [4-inherits_from.py](./4-inherits_from.py)    | `def inherits_from(obj, a_class):`    |
| [5-base_geometry.py](./5-base_geometry.py) | `class BaseGeometry:`                 |
| [6-base_geometry.py](./6-base_geometry.py) | `class BaseGeometry:`                 |
| [7-base_geometry.py](./7-base_geometry.py) | `class BaseGeometry:`                 |
| [8-rectangle.py](./8-rectangle.py) | `class Rectangle(BaseGeometry):`      |
| [9-rectangle.py](./9-rectangle.py) | `class Rectangle(BaseGeometry):`      |
| [10-square.py](./10-square.py)    | `class Square(Rectangle):`            |
| [11-square.py](./11-square.py)    | `class Square(Rectangle):`            |
| [100-my_int.py](./100-my_int.py)  | `class MyInt(int):`                   |
| [101-add_attribute.py](./101-add_attribute.py) | `def add_attribute(obj, att, value):` |

## Tasks :page_with_curl:

### 0. Lookup

- [0-lookup.py](./0-lookup.py)
- Python function that returns a list of available attributes and methods of an object.

### 1. My List

- [1-my_list.py](./1-my_list.py)
- Python class `MyList` that inherits from `list`. Includes:
  * Public instance method `def print_sorted(self):` that prints the list in ascending sorted order (assumes all list elements are integers).

### 2. Exact same object

- [2-is_same_class.py](./2-is_same_class.py)
- Python function that returns `True` if an object is exactly an instance of a specified class; otherwise `False`.

### 3. Same class or inherit from

- [3-is_kind_of_class.py](./3-is_kind_of_class.py)
- Python function that returns `True` if an object is an instance or inherited instance of a specified class; otherwise `False`.

### 4. Only sub class of

- [4-inherits_from.py](./4-inherits_from.py)
- Python function that returns `True` if an object is an inherited instance (either directly or indirectly) from a specified class; otherwise `False`.

### 5. Geometry module

- [5-base_geometry.py](./5-base_geometry.py)
- An empty Python class `BaseGeometry`.

### 6. Improve Geometry

- [6-base_geometry.py](./6-base_geometry.py)
- Python class `BaseGeometry`. Builds on [5-base_geometry.py](./5-base_geometry.py) with:
  * Public instance method `def area(self):` that raises an `Exception` with the message `area() is not implemented`.

### 7. Integer validator

- [7-base_geometry.py](./7-base_geometry.py)
- Python class `BaseGeometry`. Builds on [6-base_geometry.py](./6-base_geometry.py) with:
  * Public instance method `def integer_validator(self, name, value):` that validates the parameter `value`.
  * Assumes the parameter `name` is always a string.
  * The parameter `value` must be an `int`, otherwise, a `TypeError` exception is raised with the message `<name> must be an integer`.
  * The parameter `value` must be greater than `0`, otherwise, a `ValueError` exception is raised with the message `<value> must be greater than 0`.

### 8. Rectangle

- [8-rectangle.py](./8-rectangle.py)
- Python class `Rectangle` that inherits from `BaseGeometry` ([7-base_geometry.py](./7-base_geometry.py)). Includes:
  * Private attributes `width` and `height` - validated with `integer_validator`.
  * Instantiation with `width` and `height`: `def __init__(self, width, height):`

### 9. Full rectangle

- [9-rectangle.py](./9-rectangle.py)
- Python class `Rectangle` that inherits from `BaseGeometry` ([7-base_geometry.py](./7-base_geometry.py)). Builds on [8-rectangle.py](./8-rectangle.py) with:
  * Implementation of the method `area()`.
  * Special method `__str__` to print `Rectangle`s in the format `[Rectangle] <width>/<height>`.

### 10. Square #1

- [10-square.py](./10-square.py)
- Python class `Square` that inherits from `Rectangle` ([9-rectangle.py](./9-rectangle.py)). Includes:
  * Private attribute `size` - validated with `integer_validator`.
  * Instantiation with `size`: `def __init__(self, size):`.
  * Implementation of the `area()` method.

### 11. Square #2

- [11-square.py](./11-square.py)
- Python class `Square` that inherits from `Rectangle` ([9-rectangle.py](./9-rectangle.py)). Builds on [10-square.py](./10-square.py) with:
  * Special method `__str__` to print squares in the format `[Square] <width>/<height>`.

### 100. Can I? 

- [100-my_int.py](./100-my_int.py)
- Python class `MyInt` that inherits from `int`. Swaps the behavior of the `==` and `!=` operators. When comparing two instances of `MyInt`, the result should be based on the opposite behavior of the standard `int` comparison.

### 101. Add attribute

- [101-add_attribute.py](./101-add_attribute.py)
- Python function `add_attribute(obj, att, value)` that adds a new attribute to an object if it's possible.

## Usage

These Python scripts can be executed as standalone programs or imported as modules into other Python scripts for use. To run a script, you can use the following command in your terminal:

```
python script_name.py
```

For example, to run the 0-lookup.py script, you can use the following command:

```
python 0-lookup.py
```

## Author
[Ifeanyi kalu](https://github.com/fazzy12) - [LinkedIn](htttps://linkedin.com/in/ifeanyi-kalu)
