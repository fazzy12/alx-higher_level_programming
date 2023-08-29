#!/usr/bin/python3
"""
Module for matrix multiplication using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        numpy.ndarray: The resulting matrix after multiplication.

    Raises:
        ValueError: If m_a or m_b is empty,
            or if the matrices cannot be multiplied.
    """

    result = np.matmul(m_a, m_b)
    return result
