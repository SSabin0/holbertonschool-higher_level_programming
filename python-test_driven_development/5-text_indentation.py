#!/usr/bin/python3
"""
This module contains a function that indents text based on specific characters.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ?, and :

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    flag = 0
    for char in text:
        if flag == 0:
            if char == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if char in ".?:":
                print(char)
                print()
                flag = 0
            else:
                print(char, end="")
