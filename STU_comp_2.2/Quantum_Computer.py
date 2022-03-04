"""
Access to the simulated quantum computer
"""
import time
import random
import numpy as np
from Quantum_Gate import Quantum_Gate as QGate
from Quantum_Algorithm import Quantum_Algorithm as QAlg
from Quantum_Register import Quantum_Register as QReg
from ListQuantumGates import H, CNOT, O, G
from ListQuantumAlgorithms import Grover
import matplotlib.pyplot as plt

def main():
    """
    A quick intro:



    Register:

        To initialise a register object, we call for example Reg_1 = QReg(n) where n is required number of qubits in register
    multiple registers can be called if required

    To access the state vector (2**n long array) we call Reg_1.Reg

    To access a particular state we call Reg_obj.Reg[get_state_index([1,0,0,1,0)]) where 1,0,0,1,0 is the state we want
    to view the amplitude of




    Gates and algorithms:

    Gate objects H, CNOT, O, G should all be imported from ListQuantumGates.py
    aswell as the algorithm object, Grover, from ListQuantumAlgorithms.py

    To act a gate or algorithm on a register, we do H.act() (for hadamard for example or Grovers.act() with
    parameters: Reg_obj, q=None, all=False, state=None (see documentation)

    "Reg_obj" is the register object to act the gate or algorithm on
    "q" is the qubits to act on
    "all" is whether or not the gate should act on all qubits, only applicable to 1 qubit gates and not applicable at all to algorithms
    state is the state required for the oracle in Grovers (or when calling oracle directly)

    This will act the gate or algorithm on the supplied register, Reg_obj





    A note on how the Quantum_Gate class works:

    QGate.act is class variable. If a certain gate has an algorithmic method of acting then  self.act = Gate_act
    for example, when CNOT gate is initialised, we say in initialisation: self.act = self.act_CNOT
    This means that the function self.act_CNOT() is called when we call "CNOT.act in main"


    If there is no algorithmic method for a gate, we say: self.act = self.act_choose
    where self.act_choose is a function that will choose between the original "act_on" function, the new "Stu_act_on" or
     "act_on_all" depending on gate type and parameters of act

     So no matter how we compute a certain gate, all the user has to do is Gate.act() and the rest will be sorted


     This layout does have some drawbacks, but hopefully it is easier to use, and more computationally efficient than
    previous iterations of our quantum computer



    """





    #test grover
    #can do up to about 10 or 11 qubits almost instantaneously, any more takes longer
    Reg_1 = QReg(6)
    Grover.act(Reg_1, state = "110000")
    """
    
    #test CNOT
    Reg_1 = QReg(3, increasing_integers = True)
    print(Reg_1.Reg)
    CNOT.act(Reg_1, [0,1])
    print(Reg_1.Reg)
    """


    """
    TEST GROVER EFFICIENCY WITH QUBITS
    
    
    Function to create random binary string for oracle
    #wee function just copied from web
    def rand_key(p):

        # Variable to store the
        # string
        key1 = ""

        # Loop to find the string
        # of desired length
        for i in range(p):
            # randint function to generate
            # 0, 1 randomly and converting
            # the result into str
            temp = str(random.randint(0, 1))

            # Concatenation the random 0, 1
            # to the final result
            key1 += temp

        return (key1)

    

    start = time.time()
    print("hello")
    end = time.time()
    print(end - start)

    #test grover efficiency
    time_elapsed =[]
    nrange = np.arange(3,14)
    print(nrange)
    for i in nrange:
        state = rand_key(i)

        #start timer
        start = time.time()

        #enact grovers
        Reg_1 = QReg(i)
        Grover.act(Reg_1, state=state)

        #end timer
        end = time.time()

        elapsed = end-start
        time_elapsed.append(elapsed)
    print("finished!")
    plt.title("Time taken to act grover's algorithm for any number of qubits")
    plt.xlabel("Number of qubits")
    plt.ylabel("Time taken (s)")
    plt.plot(nrange, time_elapsed)
    plt.show()
    """









# Execute main method, but only when directly invoked
if __name__ == "__main__":
    main()

