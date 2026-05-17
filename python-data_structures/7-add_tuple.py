#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least 2 elements by padding them with zeros
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    
    # Return a new tuple adding the first two elements of each padded tuple
    return (a[0] + b[0], a[1] + b[1])
