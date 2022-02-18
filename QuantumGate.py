# -*- coding: utf-8 -*-

"""
QuantumGate is a class whose instances can represent the action of any quantum
gate.

"""
import numpy as np
import sys

class QuantumGate(object):
    def __init__(self, matrix):
        """
        The matrix and tensor representation of the quantum gate has to be established.

        Parameters
        ----------
        matrix : Complex numpy array
            Stores the matrix representation of the quantum gate.

        Returns
        -------
        None.
        """
        self.matrix = matrix
        
        # self.size is the number of qubits the gate is designed to act on.
        # Can be obtained by looking at the number of rows in its matrix representation.
        self.size = int(matrix.shape[0] / 2)
        
        # self.tensor is the tensor representation of the quantum gate, which is needed
        # for the tensor calculations of its action on the quantum register.
        self.tensor = np.reshape(matrix, (2,)*matrix.shape[0])
        
        
    def acts_on(self, q, reg):
        """
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
        reg_new = np.zeros_like(reg)
        
        # Checks we are acting on the amount of qubits the quantum gate is designed for.
        if len(q) != self.size:
            sys.exit("This quantum gate does not act on the number of qubits specified")
        
        # Checks we are not acting on more qubits than exist in the register.
        if len(q) > np.ndim(reg):
            sys.exit("You cannot act on more qubits than exist in the register.")
        
        # The first cartesian product is for iterating over the unprimed indices.
        for xs in cartesian_product_n_qubits(np.ndim(reg)):   
            
            # The second cartesian product is for iterating over the primed indices.
            # Equivalent to Einstein summation. The number of primed indices the Einstein
            # summation is done over is specified by len(q).
            for ys in cartesian_product_n_qubits(len(q)):
                
                # We now set the indices of each tensor according to tensor notation.
                indices = np.asarray(xs)
                indices_prime = indices
                indices_gate = np.zeros(len(q)*2, dtype = int)
    
                for i,y in enumerate(ys):
                    indices_prime[q[i]] = y
                    
                    indices_gate[i]         = xs[q[i]]
                    indices_gate[i+len(q)]  = y
     
                xs_prime = tuple(indices_prime)
                xs_gate = tuple(indices_gate)
            
                # We are now able to do the tensor product with the correct indices.
                reg_new[xs] += self.tensor[xs_gate] * reg[xs_prime]
                
        return reg_new
    

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



    
    
    
            
 