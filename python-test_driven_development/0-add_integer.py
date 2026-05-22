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
        TypeError: If either a or b is not an integer, float, or is NaN.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # A completely bulletproof way to catch NaN without math module:
    # Converting float('nan') to a string always results in 'nan'
    if str(a) == "nan":
        raise TypeError("a must be an integer")
    if str(b) == "nan":
        raise TypeError("b must be an integer")

    # Catch float infinity edge cases before casting causes an OverflowError
    if a == float('inf') or a == float('-inf'):
        raise OverflowError("cannot convert float infinity to integer")
    if b == float('inf') or b == float('-inf'):
        raise OverflowError("cannot convert float infinity to integer")

    return int(a) + int(b)
