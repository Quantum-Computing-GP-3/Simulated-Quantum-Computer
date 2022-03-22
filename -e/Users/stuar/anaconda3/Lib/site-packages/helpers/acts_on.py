import sys
import numpy as np

from .misc import stu_kron
from .cartesian_products import cartesian_product_n_qubits


def acts_on(Reg_obj, q, tensor, size):
    """

    NOW TAKES A 2D INPUT AND CONVERTS TO TENSOR

    Given a quantum register, the quantum gate will act on the quantum qubits
    specified in the list q. 
    
    For example, if q = [0,1], the quantum gate will act on the first and second
    qubit of the register.   

    Parameters
    ----------
    q : List
        Specifies on which qubit(s) of the quantum register the quantum gate 
        will act on. Numbering of the qubits starts at zero. 
    reg : Complex Numpy Array
        Specifies the quantum register the quantum gate will act on.

    Returns
    -------
    reg_new : Complex Numpy Array
        Resulting quantum register.

    """
    # Complex array to store the resulting quantum register after the quantum
    # gate has been applied.

    # Reg_obj is register object, Reg is Quantum_Register class function, reg is what I will call the tensor register in this function
    Reg_obj.tensor_notation()
    reg = Reg_obj.Reg


    reg_new = np.zeros_like(reg)
    
    # Checks we are acting on the amount of qubits the quantum gate is designed for.
    if len(q) != size:
        sys.exit("This quantum gate does not act on the number of qubits specified")
    
    # Checks we are not acting on more qubits than exist in the register.
    if len(q) > np.ndim(reg):
        sys.exit("You cannot act on more qubits than exist in the register.")
    
    # The first cartesian product is for iterating over the unprimed indices.
    for xs in cartesian_product_n_qubits(np.ndim(reg)):   
        
        # The second cartesian product is for iterating over the primed indices.
        # Equivalent to Einstein summation. The number of primed indices the Einstein
        # Summation is done over is specified by len(q).
        for ys in cartesian_product_n_qubits(len(q)):
            
            # We now set the indices of each tensor according to tensor notation.
            indices = np.asarray(xs)
            indices_prime = indices
            indices_gate = np.zeros(len(q)*2, dtype = int)

            for i,y in enumerate(ys):
                indices_prime[q[i]] = y
                
                indices_gate[i] = xs[q[i]]
                indices_gate[i+len(q)]= y
    
            xs_prime = tuple(indices_prime)
            xs_gate = tuple(indices_gate)
        
            # We are now able to do the tensor product with the correct indices.
            reg_new[xs] += tensor[xs_gate] * reg[xs_prime]
        Reg_obj.Reg = reg_new
        Reg_obj.tensor_notation()
    return Reg_obj


def Stu_acts_on(Reg_obj, q, matrix, size):
    """
    Given a quantum register, the quantum gate will act on the quantum qubits
    specified in the list q.

    For example, if q = [0,1], the quantum gate will act on the first and second
    qubit of the register.

    :param Reg_obj: obj
        Register object
    :param q: list
        qubit(s) to act on


    """
    # Reg_obj is register object, Reg is Quantum_Register class function, reg is what I will call the tensor register in this function
    reg = Reg_obj.Reg
    n = Reg_obj.n

    # Checks we are acting on the amount of qubits the quantum gate is designed for.
    numq = len(q)
    if numq != size:
        sys.exit("This quantum gate does not act on the number of qubits specified")

    # Checks we are not acting on more qubits than exist in the register.
    if numq > n:
        sys.exit("You cannot act on more qubits than exist in the register.")

    # If number of qubits to act on is 1
    if numq == 1:
        q = q[0]


        # Set start matrix (ie if its the first qubit then the first matrix is the gate, else, it is the identiy
        if q == 0:
            M = matrix
        else:
            M = np.eye(2, dtype=complex)



        # Act the identity matrix if its not the qubit that the gate is acting on, if it is the correct qubit then act self.matrix
        for i in range(1,n):
            if q == i:
                A = matrix
            else:
                A = np.eye(2, dtype=complex)
            M = stu_kron(M, A)

        reg_new = np.matmul(M, reg)
        Reg_obj.Reg = reg_new
        Reg_obj.tensor_notation()
        return Reg_obj
        

    # If number of qubits to act on is 2
    elif numq >1:
        print("This will have to be passed to pablo's original act_on ")
        # Havent done yet, shouldnt be hard atall


def acts_on_all(Reg_obj, matrix):
    """
    function to act a 1 qubit gate on all qubits
    :param Reg_obj: obj
        Register object
    :return:
    """
    # Reg_obj is register object, Reg is Quantum_Register class function, reg is what I will call the tensor register in this function
    reg = Reg_obj.Reg
    n = Reg_obj.n

    # If the gate isn't 2x2, this wont work
    if matrix.shape != (2,2):
        sys.exit("You cannot act anything other than a 1 qubit gate using this function")

    # Iterate through kron products untill we have a full matrix
    M = matrix
    for i in range(n-1):
        M = stu_kron(M, matrix)

    # Matrix multiply the matrix we have built, and the state vector for new reg
    reg_new = np.matmul(M, reg)
    Reg_obj.Reg = reg_new
    Reg_obj.tensor_notation()
    return Reg_obj