#!/usr/bin/python3
"""
This module provides utility functions for working with text
formatting and printing.
"""


def text_indentation(text):
    """Format a given text by adding two new lines after each '.', '?', or ':'.

        Args:
            text (str): The input text to be formatted.

        Returns:
            None. The formatted text is printed.

        Raises:
            TypeError: If the input text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_chars = ".?:"
    lines = []
    line = ""

    for char in text:
        line += char
        if char in punctuation_chars:
            lines.append(line.strip())
            line = ""

    lines.append(line.strip())

    formatted_text = "\n\n".join(lines)
    print(formatted_text)
