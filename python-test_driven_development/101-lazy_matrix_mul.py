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
    if isinstance(m_a, str) or isinstance(m_b, str):
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    
    try:
        return np.matmul(m_a, m_b)
    except ValueError as ve:
        try:
            shape_a = np.shape(m_a)
            shape_b = np.shape(m_b)
            raise ValueError(
                f"shapes {shape_a} and {shape_b} not aligned: "
                f"{shape_a[1]} (dim 1) != {shape_b[0]} (dim 0)"
            )
        except Exception:
            raise ve
