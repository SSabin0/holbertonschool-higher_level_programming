#!/usr/bin/python3
"""This module defines a function that converts an object to a JSON string."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object as a string.

    Args:
        my_obj: The Python object to convert to JSON format.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
