#!/usr/bin/python3
"""Module for converting Roman numerals to integers."""


def roman_to_int(roman_string):
    """Convert a roman string to an integer."""
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0
    length = len(roman_string)

    for i in range(length):
        current_val = roman_dict.get(roman_string[i], 0)

        if i + 1 < length and current_val < roman_dict.get(roman_string[i + 1], 0):
            total -= current_val
        else:
            total += current_val

    return total
