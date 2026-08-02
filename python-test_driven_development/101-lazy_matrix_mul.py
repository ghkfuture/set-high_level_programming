#!/usr/bin/python3
"""
Module for lazy_matrix_mul function using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy module.

    Args:
        m_a: First matrix.
        m_b: Second matrix.

    Returns:
        Matrix multiplication result.
    """
    return np.matmul(m_a, m_b)
