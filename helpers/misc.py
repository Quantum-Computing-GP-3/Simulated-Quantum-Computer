import numpy as np


def stu_kron(a, b):
    """
    kronecker product function
    ASSUMING NUMBER OF DIMENSIONS OF BOTH IS THE SAME so basically only works for 2x2
    !!!!!!!!!!!!! basically copied from numpy source code, stripped down alot !!!!!!





    [[1 2]
     [3 4]]
    [[1. 0.]
     [0. 1.]]
    results in
    [[1. 0. 2. 0.]
     [0. 1. 0. 2.]
     [3. 0. 4. 0.]
     [0. 3. 0. 4.]]


    Parameters
    ----------
    a, b : array_like
        arrays to find the kronecker product of

    Returns
    ----------
    Kron: array_like
        Kronecker product

    """
    a_dim = a.ndim
    b_dim = b.ndim

    # if one is a scalar, normal multiply
    if a_dim == 0 or b_dim == 0:
        return a * b

    #outer product
    outer = a.flatten()[:, np.newaxis] * b.flatten()[np.newaxis, :]

    #reshape and concantenate for kron product
    kron = outer.reshape(a.shape + b.shape)
    # concantenate for correct dimensions
    for i in range(a_dim):
        kron = np.concatenate(kron, axis=a_dim - 1)

    return kron


def get_state_index(ind,n):
    """
    function to find the amplitude of a certain state
    :param ind: list of 1 or 0's
        specifies the state we want to view
    :param n: int
        number of qubits
    :return: coefficient of state
    """

    # could be a magic function or something
    # very ineficient in its current form but only have to call once

    """ ie.

        get_state_index([0, 0, 0, 1])
        returns 1

        get_state_index([1, 1, 1, 1])
        returns 15

        as expected

        """


    rang = np.flip(np.arange(0, n))
    reg_route = np.zeros(len(rang))
    for count, i in enumerate(rang):
        reg_route[count] = 2 ** i

    state_2d_index = np.sum(np.array(ind) * reg_route)

    return int(state_2d_index)
    