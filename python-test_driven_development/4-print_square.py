#!/usr/bin/python3
"""
This module defines a function that 
prints a square with the character #.
"""

def print_square(size):
    """
    prints a square with the character #.

    Args:
        size: The size length of the square.

    Returns:
        square with the character #.

    Raises:
        TypeError: If size is not a integer.
        ValueError: If size is less than zero.
        TypeError: If size is a float and is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
