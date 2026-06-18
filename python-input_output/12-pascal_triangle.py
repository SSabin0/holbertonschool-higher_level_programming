#!/usr/bin/python3
"""This module defines a function that generates Pascal's Triangle."""


def pascal_triangle(n):
    """Generates a list of lists of integers representing Pascal's Triangle.

    Args:
        n (int): The number of rows of the triangle to generate.

    Returns:
        list: A list of lists containing the numbers of Pascal's Triangle,
            or an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    while len(triangle) < n:
        prev_row = triangle[-1]
        next_row = [1]

        for i in range(len(prev_row) - 1):
            next_row.append(prev_row[i] + prev_row[i + 1])

        next_row.append(1)
        triangle.append(next_row)

    return triangle
