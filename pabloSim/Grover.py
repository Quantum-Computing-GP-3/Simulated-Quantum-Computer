# -*- coding: utf-8 -*-
"""
Given the appropriate quantum gates, it applies Grover's algorithm to a quantum
register.

"""
# From ListQuantumGates we import the number of qubits of the quantum register (n)
# and the needed quantum gates.
from .ListQuantumGates import n, Hadamard, O, G
import numpy as np

def main():
    # First step is to initialise a quantum register of n qubits to the 0th state.
    reg = np.zeros((2,)*n, dtype = complex) 
    reg[0,0,0,0] = 1
    
    
    # We then use Hadamard gates to get the quantum register into an equal superposition
    # of all states.
    for i in range(n):
       reg = Hadamard.acts_on([i], reg)

    # We now apply the Grover and Oracle gates in order to amplify the needed state.
    number_iterations = int( np.pi / 4 * np.sqrt(2**n) )
    
    for i in range(number_iterations):
        reg = O.acts_on([j for j in range(n)], reg)
        reg = G.acts_on([j for j in range(n)], reg)
        
        
    print("The resulting quantum register should have a certain state amplified:")
    print(reg)
    
    print("\nIn this case the amplified state is reg[1,1,0,0]:")
    print(reg[1,1,0,0])

    
# Execute main method, but only when directly invoked
if __name__ == "__main__":
    main()