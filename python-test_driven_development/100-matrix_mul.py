#!/usr/bin/python3
"""Module that defines a matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices.

    Args:
        m_a: First matrix (list of lists of ints/floats).
        m_b: Second matrix (list of lists of ints/floats).

    Returns:
        New matrix resulting from multiplication.

    Raises:
        TypeError: For non-lists, non-list of lists, non-numeric elements,
                   or non-rectangular matrices.
        ValueError: For empty matrices or non-multipliable dimensions.
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

    for row in m_a:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    len_a = len(m_a[0])
    if not all(len(row) == len_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    len_b = len(m_b[0])
    if not all(len(row) == len_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            elem_sum = 0
            for k in range(len(m_b)):
                elem_sum += m_a[i][k] * m_b[k][j]
            row.append(elem_sum)
        new_matrix.append(row)

    return new_matrix
