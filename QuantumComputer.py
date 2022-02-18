# -*- coding: utf-8 -*-
from QuantumGate import QuantumGate
import numpy as np

def main():

    #----------------------------- EXAMPLE 1 ---------------------------------
    print("This example is of a Hadamard gate acting on the first qubit of a four",
            "qubit quantum register.\n")
    n=4

    reg = np.zeros((2,)*n, dtype = complex) 
    reg[1,0,0,0] = 1j/np.sqrt(5)
    reg[0,1,0,0] = 2/np.sqrt(5)
    
    print("This is the initial quantum register:")
    print(reg)
    
    # We define the hadamard as a QuantumGate by writing down its matrix representation.
    hadamard = QuantumGate(1/np.sqrt(2)*np.array([[1,1],
                                                  [1,-1]]))
    
    # We then act on the qth qubit of our quantum register.
    # Numbering of the qubits starts at zero.
    q = [0]
    reg_new = hadamard.acts_on(q, reg)
    
    print(f"This is the result of applying Hadamard to the {q}th qubit on the register:")
    print(reg_new)
    
    # One can check reg_new is correct by checking the coefficients of each basis state.
    print(reg_new[1,0,0,0])
    # This checks the coefficient of the basis state |1000>, which should be -i / sqrt(10) 
    # in this case




    #----------------------------- EXAMPLE 2 ---------------------------------
    print("\nThis example corresponds to the action of a CNOT gate on the second and",
          "third qubit of a three qubit quantum register.\n")
    n = 3

    reg = np.zeros((2,)*n, dtype = complex) 
    reg[0,0,1] = 1/np.sqrt(7)
    reg[0,1,0] = -2j/np.sqrt(7)
    reg[1,0,0] = 1/np.sqrt(7)
    reg[1,1,0] = 1/np.sqrt(7)
    
    print("This is the initial quantum register:")
    print(reg)
    
    # We define the CNOT as a QuantumGate by writing down its matrix representation.
    cnot = QuantumGate(np.array([[1,0,0,0],
                                 [0,1,0,0],
                                 [0,0,0,1],
                                 [0,0,1,0]]))
    
    # We then act on the qth qubit(s) of our quantum register.
    q = [1,2]
    reg_new = cnot.acts_on(q, reg)
    
    print(f"\nThis is the result of applying CNOT to the {q} qubit on the register:")
    print(reg_new)


    
# Execute main method, but only when directly invoked
if __name__ == "__main__":
    main()