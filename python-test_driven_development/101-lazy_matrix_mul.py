#!/usr/bin/python3
"""
This module uses NumPy to perform matrix multiplication.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a: First matrix.
        m_b: Second matrix.

    Returns:
        The result of the matrix multiplication.

    Raises:
        TypeError: If m_a or m_b is not a valid list of lists of numbers.
        ValueError: If the matrices can't be multiplied.
    """
    try:
        return np.matmul(m_a, m_b)
    except ValueError as ve:
        raise ValueError("shapes not aligned for matrix multiplication") from ve
    except TypeError as te:
        raise TypeError("invalid input types for matrix multiplication") from te

