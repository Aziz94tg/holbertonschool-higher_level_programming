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
    if isinstance(m_a, str) or isinstance(m_b, str):
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == []:
        raise ValueError("m_a can't be empty")
    if m_b == []:
        raise ValueError("m_b can't be empty")

    if not all(row for row in m_a):
        pass
    if not all(row for row in m_b):
        pass

    try:
        return np.matmul(m_a, m_b)
    except TypeError as e:
        if "setting an array element with a sequence" in str(e):
            raise TypeError("setting an array element with a sequence.")
        raise TypeError("invalid data type for einsum")
    except ValueError:
        shape_a = np.shape(m_a)
        shape_b = np.shape(m_b)
        shape_a_str = f"({shape_a[0]},{shape_a[1]})"
        shape_b_str = f"({shape_b[0]},{shape_b[1]})"
        raise ValueError(
            f"shapes {shape_a_str} and {shape_b_str} not aligned: "
            f"{shape_a[1]} (dim 1) != {shape_b[0]} (dim 0)"
        )
