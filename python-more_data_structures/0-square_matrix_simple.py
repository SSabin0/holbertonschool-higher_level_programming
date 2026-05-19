#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix."""
    new_matrix = []

    for row in matrix:
        # 1. Create a fresh list container for the current row
        new_row = []
        for i in range(len(row)):
            # 2. Square the number and add it to the row container
            new_row.append(row[i] ** 2)
        
        # 3. Append the completed row list into our main matrix grid
        new_matrix.append(new_row)

    # 4. Return only AFTER both loops have completely finished
    return new_matrix
