#!/usr/bin/python3
"""
Module: 0-pascal_triangle
"""

def pascal_triangle(n):
    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Generate each row
    for i in range(1, n):
        # Start each row with a 1
        row = [1]

        # Calculate the inner elements (sum of two elements above)
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])

        # End each row with a 1
        row.append(1)

        # Append the row to the triangle
        triangle.append(row)

    return triangle
