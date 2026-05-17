#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds two tuples based on their first two elements.

    Missing elements are treated as 0, and extra elements are ignored.
    """
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    return (a[0] + b[0], a[1] + b[1])
