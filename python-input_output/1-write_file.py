#!/usr/bin/python3
"""
This module contains a function that writes a string to a text file (UTF8)
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """Writes a string to a UTF8 text file and returns the character count.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write into the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
