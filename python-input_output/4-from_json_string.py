#!/usr/bin/python3
"""This module defines a function converting a JSON string to an object."""
import json


def from_json_string(my_str):
    """Returns a Python data structure represented by a JSON string.

    Args:
        my_str (str): The JSON string representation to decode.

    Returns:
        any: The corresponding Python object (list, dict, str, etc.).
    """
    return json.loads(my_str)
