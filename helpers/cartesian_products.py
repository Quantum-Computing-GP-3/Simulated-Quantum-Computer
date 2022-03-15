def cartesian_product_n_qubits(n):
    """
    Given an n qubit system generates all the possible index combinations.
    
    For example, for a four qubit system it would yield the following values:
        (0,0,0,0), (0,0,0,1), (0,0,1,0),(0,0,1,1), [...], (1,1,1,1)

    Equivalent to n-nested for loops. We use yield instead of return because there
    is no need to remember the list of all index combinations. Saves memory.

    Parameters
    ----------
    n : integer
        Number of qubits in the system.

    Yields
    ------
    tuple
        Cartesian product of n indices.

    """
    pools = [(0,1)] * n
    
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for product in result:
        yield tuple(product)


def stu_cartesian_product_n_qubits(n):
    """
    Stu needed the full return not yield so added this function

    Given an n qubit system generates all the possible index combinations.

    For example, for a four qubit system it would yield the following values:
        (0,0,0,0), (0,0,0,1), (0,0,1,0),(0,0,1,1), [...], (1,1,1,1)

    Equivalent to n-nested for loops. We use yield instead of return because there
    is no need to remember the list of all index combinations. Saves memory.

    Parameters
    ----------
    n : integer
        Number of qubits in the system.

    Yields
    ------
    tuple
        Cartesian product of n indices.

    """
    pools = [(0, 1)] * n

    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    return result
    