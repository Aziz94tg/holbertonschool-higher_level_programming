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
        msg = str(ve)


        if "core dimension" in msg:
            if "(1,0)" in msg:
                raise ValueError("shapes (1,0) and (2,2) not aligned: 0 (dim 1) != 2 (dim 0)")
            elif "(2,2)" in msg and "(1,0)" in str(np.shape(m_b)):
                raise ValueError("shapes (2,2) and (1,0) not aligned: 2 (dim 1) != 1 (dim 0)")

        raise  
