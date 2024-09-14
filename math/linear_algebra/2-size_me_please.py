def matrix_shape(matrix):
    """
    Calculates the shape (dimensions) of a matrix.

    Args:
        matrix: A 2D or higher dimensional list representing a matrix.

    Returns:
        A list of integers representing the shape of the matrix.
    """

    # Get the shape of the first row (assuming all elements have the same
    # shape)
    shape = list(len(row) for row in matrix[:1])

    # Check if the matrix is a single row (1D)
    if len(matrix) == 1:
        shape = [shape[0]]  # Convert to a single-element list for consistency

    return shape
