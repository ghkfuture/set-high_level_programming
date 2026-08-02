#!/usr/bin/python3
"""
Module for matrix_mul function.
"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices.

    Args:
        m_a: First matrix.
        m_b: Second matrix.

    Returns:
        New matrix result.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all(isinstance(elem, (int, float)) for row in m_a for elem in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(elem, (int, float)) for row in m_b for elem in row):
        raise TypeError("m_b should contain only integers or floats")

    len_a = len(m_a[0])
    if not all(len(row) == len_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    len_b = len(m_b[0])
    if not all(len(row) == len_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    res = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            elem_sum = 0
            for k in range(len(m_b)):
                elem_sum += m_a[i][k] * m_b[k][j]
            row.append(elem_sum)
        res.append(row)
    return res
