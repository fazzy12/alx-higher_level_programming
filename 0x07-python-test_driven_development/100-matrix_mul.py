#!/usr/bin/python3
"""Module composed by a function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        list of lists: The resulting matrix after multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list,
            or if m_a or m_b is not a list of lists,
            or if one element of the matrices is not an integer or float.
        ValueError: If m_a or m_b is empty,
            or if the matrices cannot be multiplied.

    Note:
        The matrices must meet certain requirements:
        - Both m_a and m_b must be lists of lists.
        - All elements of the matrices must be integers or floats.
        - Each row of m_a must have the same size,
        and each row of m_b must have the same size.
        - The number of columns in m_a must be equal
        to the number of rows in m_b for multiplication
    """

    be_list = "m_a must be a list or m_b must be a list"
    listOfList = "m_a must be a list of lists or m_b must be a list of lists"
    notEmpty = "m_a can't be empty or m_b can't be empty"
    varTypes1 = "m_a should contain only integers or"
    varTypes2 = "floats or m_b should contain only integers or floats"
    sameSize1 = "each row of m_a must be of the same"
    sameSize2 = "size or each row of m_b must be of the same size"
    cantMul = "m_a and m_b can't be multiplied"

    # both must be a list
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError(be_list)

    # both m_a and m_b must be a list of a list
    if not all(isinstance(row, list) for row in m_a) or\
            not all(isinstance(row, list) for row in m_b):
        raise TypeError(listOfList)

    # both m_a and m_b cant be empty
    if len(m_a) == 0 or len(m_b) == 0:
        raise ValueError(notEmpty)

    # both m_a and m_b be ints or floats
    a = any(not isinstance(num, (int, float)) for row in m_a for num in row)
    b = any(not isinstance(num, (int, float)) for row in m_b for num in row)

    if a or b:
        raise TypeError(varTypes1 + " " + varTypes2)

    # get length of both lists
    num_columns_m_a = len(m_a[0])
    num_columns_m_b = len(m_b[0])

    # rows must be of the same size
    if not all(len(row) == num_columns_m_a for row in m_a) or\
            not all(len(row) == num_columns_m_b for row in m_b):
        raise ValueError(sameSize1 + " " + sameSize2)

    # check if rows can  be multiplied
    if num_columns_m_a != len(m_b):
        raise ValueError(cantMul)

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            element = 0
            for k in range(len(m_b)):
                element += m_a[i][k] * m_b[k][j]
            row.append(element)
        result.append(row)

    return result
