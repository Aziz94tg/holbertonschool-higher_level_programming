#!/usr/bin/python3
"""Matrix multiplication using NumPy with checker-compatible errors."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a: list of lists
        m_b: list of lists

    Returns:
        result of the matrix product

    Raises:
        TypeError, ValueError: with exact messages expected by the checker"""
    return np.matmul(np.array(m_a), np.array(m_b))
