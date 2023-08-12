def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix"""
    return [[elem ** 2 for elem in row] for row in matrix]
    
