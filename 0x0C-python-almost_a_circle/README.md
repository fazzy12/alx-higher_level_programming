<div style="width: 100%; height: 0; padding-bottom: 100%; position: relative;">
    <img src="circle.mp4" alt="OOP Image" style="position: absolute; width: 100%; height: 100%; object-fit: cover;">
</div>

# Python - Almost a Circle

In this project, I have demonstrated my skills in Python object-oriented programming by implementing three interconnected classes to represent rectangles and squares. I have also created a comprehensive test suite using the `unittest` module to thoroughly evaluate the functionality of each class.

The project leverages various Python tools and concepts, including:

- Importing modules
- Handling exceptions
- Utilizing private attributes
- Implementing getter and setter methods
- Working with class and static methods
- Utilizing inheritance
- Performing file input/output operations
- Using `*args` and `**kwargs` in functions
- Serializing and deserializing data in JSON and CSV formats
- Conducting unit testing with the `unittest` framework

## Tests :heavy_check_mark:

The project includes a test suite located in the [tests/test_models](./tests/test_models) directory. This suite consists of independently-developed test files for each class:

- [test_base.py](./tests/test_models/test_base.py) - Tests for the base class.
- [test_rectangle.py](./tests/test_models/test_rectangle.py) - Tests for the rectangle class.
- [test_square.py](./tests/test_models/test_square.py) - Tests for the square class.

## Classes :cl:

### Base

The `Base` class serves as the foundation for all other classes in the project. It encompasses the following features:

- Private class attribute `__nb_objects = 0` to track the number of objects created.
- Public instance attribute `id` to store the unique identifier of each object.
- Class constructor `def __init__(self, id=None)`:
  - If `id` is `None`, increments `__nb_objects` and assigns its value to the public instance attribute `id`.
  - Otherwise, sets the public instance attribute `id` to the provided `id`.
- Static method `def to_json_string(list_dictionaries)`:
  - Returns the JSON string serialization of a list of dictionaries.
  - If `list_dictionaries` is `None` or empty, returns the string `"[]"`.
- Class method `def save_to_file(cls, list_objs)`:
  - Writes the JSON serialization of a list of objects to a file.
  - The parameter `list_objs` is expected to be a list of instances inherited from the `Base` class.
  - If `list_objs` is `None`, the function saves an empty list.
  - The file is saved with the name `<cls name>.json` (e.g., `Rectangle.json`) and overwrites it if it already exists.
- Static method `def from_json_string(json_string)`:
  - Returns a list of objects deserialized from a JSON string.
  - The parameter `json_string` is expected to be a string representing a list of dictionaries.
  - If `json_string` is `None` or empty, the function returns an empty list.
- Class method `def create(cls, **dictionary)`:
  - Instantiates an object with the attributes given in `**dictionary`.
- Class method `def load_from_file(cls)`:
  - Returns a list of objects instantiated from a JSON file.
  - Reads from the JSON file `<cls name>.json` (e.g., `Rectangle.json`).
  - If the file does not exist, the function returns an empty list.
- Class method `def save_to_file_csv(cls, list_objs)`:
  - Writes the CSV serialization of a list of objects to a file.
  - The parameter `list_objs` is expected to be a list of instances inherited from the `Base` class.
  - If `list_objs` is `None`, the function saves an empty list.
  - The file is saved with the name `<cls name>.csv` (e.g., `Rectangle.csv`).
- Class method `def load_from_file_csv(cls)`:
  - Returns a list of objects instantiated from a CSV file.
  - Reads from the CSV file `<cls name>.csv` (e.g., `Rectangle.csv`).
  - If the file does not exist, the function returns an empty list.
- Static method `def draw(list_rectangles, list_squares)`:
  - Draws instances of `Rectangle` and `Square` in a graphical user interface (GUI) window using the `turtle` module.
  - The parameter `list_rectangles` is expected to be a list of `Rectangle` objects to be drawn.
  - The parameter `list_squares` is expected to be a list of `Square` objects to be drawn.

### Rectangle

The `Rectangle` class represents a rectangle and inherits from the `Base` class. It includes the following features:

- Private instance attributes `__width`, `__height`, `__x`, and `__y`, each with its own getter and setter methods.
- Class constructor `def __init__(self, width, height, x=0, y=0, id=None)`:
  - Validates the input parameters for `width`, `height`, `x`, and `y`.
- Public method `def area(self)`:
  - Returns the area of the `Rectangle` instance.
- Public method `def display(self)`:
  - Prints the `Rectangle` instance to the standard output using the `#` character.
  - Adjusts the display position based on the `x` and `y` coordinates.
- Overridden `__str__` method to print a `Rectangle` instance in the format `[Rectangle] (<id>) <x>/<y>`.
- Public method `def update(self, *args, **kwargs)`:
  - Updates the attributes of a `Rectangle` instance.
  - Accepts `*args` in the order of `id`, `width`, `height`, `x`, and `y`.
  - Alternatively, accepts `**kwargs` to update attributes with a dictionary.
  - `**kwargs` is ignored if `*args` is provided.
- Public method `def to_dictionary(self)`:
  - Returns a dictionary representation of a `Rectangle` instance.

### Square

The `Square` class represents a square and inherits from the `Rectangle` class. It includes the following features:

- Class constructor `def __init__(self, size, x=0, y=0, id=None)`:
  - Assigns the `width` and `height` of the `Rectangle` superclass using the `size` parameter.
- Overridden `__str__` method to print a `Square` instance in the format `[Square] (<id>) <x>/<y>`.
- Public method `def update(self, *args, **kwargs)`:
  - Updates the attributes of a `Square` instance.
  - Accepts `*args` in the order of `id`, `size`, `x`, and `y`.
  - Alternatively, accepts `**kwargs` to update attributes with a dictionary.
  - `**kwargs` is ignored if `*args` is provided.
- Public method `def to_dictionary(self)`:
  - Returns a dictionary representation of a `Square` instance.

This project showcases the principles of object-oriented programming and encapsulation in Python, along with comprehensive testing and documentation practices.

