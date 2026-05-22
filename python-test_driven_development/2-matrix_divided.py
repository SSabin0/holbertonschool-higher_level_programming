#!/usr/bin/python3
"""
This is the 2-matrix_divided module.

The module provides a single function, matrix_divided(matrix, div), which
validates a matrix and a divisor, then returns a newly divided matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix: A list of lists containing integers or floats.
        div: The number (integer or float) to divide by.

    Returns:
        A brand new matrix with the results rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix structure or elements are invalid,
                   if rows have different sizes, or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    # 1. Validate that matrix is a non-empty list
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    # 2. Validate row sizes and element types dynamically
    row_size = None
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)

        if row_size is None:
            row_size = len(row)
        elif len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg)

    # 3. Validate divisor type and value
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 4. Generate the new matrix, handling rounding and the -0.0 infinity edge case
    new_matrix = []
    for row in matrix:
        new_row = []
        for item in row:
            val = round(item / div, 2)
            # Standardize -0.0 to 0.0 if divided by negative infinity
            if val == 0.0:
                val = 0.0
            new_row.append(val)
        new_matrix.append(new_row)

    return new_matrix
