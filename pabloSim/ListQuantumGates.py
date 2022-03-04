# -*- coding: utf-8 -*-
"""
Uses the QuantumGate class to create all the quantum gates that the quantum
computer will need.
"""
from .QuantumGate import QuantumGate
import numpy as np 
import sys

#---------------------------- HADAMARD -------------------------------------
Hadamard = QuantumGate(1/np.sqrt(2)*np.array([[1,1],
                                              [1,-1]]))
#---------------------------------------------------------------------------



#------------------------------ CNOT ---------------------------------------
CNOT = QuantumGate(np.array([[1,0,0,0],
                             [0,1,0,0],
                             [0,0,0,1],
                             [0,0,1,0]]))
#---------------------------------------------------------------------------



# The Oracle and Grover gates act on the n qubit register. Thus, in order to define
# these gates we need to know how many qubits the register has.
n = 4
N = 2**n



#------------------------------ GROVER -------------------------------------
matrix_G = np.ones((N, N)) * 2/N

for i in range(N):
    matrix_G[i,i] -= 1

G = QuantumGate(matrix_G)
#---------------------------------------------------------------------------




#------------------------------ ORACLE -------------------------------------
matrix_O = np.eye(N)

# Here we define what state the oracle picks out. 
# "1100" refers to the basis state |1,1,0,0>
state = "1100"

# We check that "state" has the same length as the number of qubits in the register. 
if len(state) != n:
    sys.exit("The state the oracle should single out is not a valid basis state of the quantum register.")

# "state" is then converted to decimal in order to modify the correct diagonal entry
# of the Oracle matrix representation.
matrix_O[int(state,2), int(state,2)] = -1

O = QuantumGate(matrix_O)
#---------------------------------------------------------------------------




    
    
    

    

