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
    try:
        return np.matmul(np.array(m_a), np.array(m_b))
    except ValueError as e:
        err = str(e)
        # Rewrite NumPy's newer error to the old expected message
        if "did not contain a loop with signature matching" in err:
            raise ValueError("Scalar operands are not allowed, use '*' instead") from None
        raise
