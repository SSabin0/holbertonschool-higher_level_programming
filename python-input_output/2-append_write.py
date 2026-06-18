#!/usr/bin/python3
"""
This module contains a function that appends a string to a text file (UTF8)
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file and returns characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text string to append.

    Returns:
        int: The number of characters added.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
