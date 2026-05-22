#!/usr/bin/python3
"""
This is the 0-add_integer module.

The module provides a single function, add_integer(a, b), which takes
two numbers, validates their types, casts them, and adds them together.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting them explicitly to integers.

    Args:
        a: The first number (integer or float).
        b: The second number (integer or float, defaults to 98).

    Returns:
        The integer sum of a and b.

    Raises:
        TypeError: If either a or b is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b) 
