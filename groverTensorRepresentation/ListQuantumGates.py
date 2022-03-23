# -*- coding: utf-8 -*-
"""
Uses the QuantumGate class to create all the quantum gates that the quantum
computer will need.
"""
from .QuantumGate import QuantumGate
import numpy as np 


#---------------------------- HADAMARD -------------------------------------
def get_Hadamard():
    """
    Returns the Hadamard gate.

    Returns
    -------
    Hadamard : QuantumGate type
        Represents the Hadamard gate.

    """

    Hadamard = QuantumGate(1/np.sqrt(2)*np.array([[1,1],
                                                  [1,-1]]))
    
    return Hadamard
#---------------------------------------------------------------------------



#------------------------------ CNOT ---------------------------------------
def get_CNOT():
    """
    Returns the CNOT gate.

    Returns
    -------
    CNOT : QuantumGate type
        Represents the CNOT gate.

    """
    CNOT = QuantumGate(np.array([[1,0,0,0],
                                 [0,1,0,0],
                                 [0,0,0,1],
                                 [0,0,1,0,]]))
    
    return CNOT
#---------------------------------------------------------------------------




# The Oracle and Grover gates act on the n qubit register. Thus, in order to define
# these gates we need to know how many qubits the register has.

#------------------------------ GROVER -------------------------------------
def get_Grover(n):
    """
    Returns the Grover gate.

    Parameters
    ----------
    n : Integer
        Number of qubits in the system.

    Returns
    -------
    G : QuantumGate type
        Represents the Grover gate.

    """
    N = 2**n

    matrix_G = np.ones((N, N)) * 2/N
    
    for i in range(N):
        matrix_G[i,i] -= 1
    
    G = QuantumGate(matrix_G)
    
    return G
#---------------------------------------------------------------------------


#------------------------------ ORACLE -------------------------------------
def get_Oracle(n, marked_state):
    """
    Returns the Oracle gate, which will amplify the marked_state.

    Parameters
    ----------
    n : Integer
        Number of qubits in the system.
    marked_state : Tuple
        Represents the state that needs to be amplified..


    Returns
    -------
    O : QuantumGate type
        Represents the Oracle gate..

    """
    N = 2**n
    
    matrix_O = np.eye(N)
    
    # Here we define what state the oracle picks out.
    # "1100" refers to the basis state |1,1,0,0>
    state = "".join(map(str,marked_state))
    
    # We check that "state" has the same length as the number of qubits in the register. 
    if len(state) != n:
        raise ValueError("The state the oracle should single out is not a valid basis state of the quantum register.")
    
    # "state" is then converted to decimal in order to modify the correct diagonal entry
    # of the Oracle matrix representation.
    matrix_O[int(state,2), int(state,2)] = -1
    
    O = QuantumGate(matrix_O)
    
    return O
#---------------------------------------------------------------------------

    

