#!/usr/bin/python3
"""
This module contains a function that writes a string to a text file (UTF8) and returns the number of characters written:
"""


def write_file(filename="", text=""):
    """Writes a UTF8 text file and return its content to stdout."""
    with open(filename, "w", encoding="utf-8") as f:
        print(f.write(), end="")
