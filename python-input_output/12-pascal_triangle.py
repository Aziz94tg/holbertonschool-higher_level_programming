#!/usr/bin/python3
"""Generates Pascal's Triangle up to n rows.
"""


def pascal_triangle(n):
    """Returns a list of lists representing Pascal Triangle of n.

    Args:
        n: Number of rows in the triangle

    Returns:
        list: pascals triangle as a list of lists
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1]

        for j in range(1, len(prev_row)):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
