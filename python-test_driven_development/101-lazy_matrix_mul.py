#!/usr/bin/python3
"""Module that defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy.

    Args:
        m_a: First matrix.
        m_b: Second matrix.

    Returns:
        Resulting matrix product.
    """
    return np.matmul(m_a, m_b)
