#!/usr/bin/python3
def common_elements(set_1, set_2):
    """Finds all common elements between two sets."""
    new_set = set()  # Initializes an empty set
    for element in set_1:
        if element in set_2:
            new_set.add(element)
    return new_set
