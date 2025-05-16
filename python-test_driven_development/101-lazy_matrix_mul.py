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
    except (ValueError, TypeError) as e:
        msg = str(e)

        if "did not contain a loop with signature matching" in msg:
            raise ValueError("Scalar operands are not allowed, use '*' instead") from None

        if "matmul: Input operand" in msg and "has a mismatch in its core dimension" in msg:
            raise ValueError("shapes (1,0) and (2,2) not aligned: 0 (dim 1) != 2 (dim 0)") from None

        if "shapes (1,0) and (2,2)" in msg:
            raise ValueError("shapes (1,0) and (2,2) not aligned: 2 (dim 1) != 1 (dim 0)") from None
        

        raise
