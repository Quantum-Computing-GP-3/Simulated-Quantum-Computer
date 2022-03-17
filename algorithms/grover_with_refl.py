from algorithm import Algorithm
import sys
from gates.hadamard import Hadamard
from gates.grover_gate import Grover
from gates.reflection import Reflection
from gates.oracle import Oracle
from helpers.register import QuantumRegister as QReg
import numpy as np
import math


H = Hadamard()
R = Reflection()

class Grover_Reflection(Algorithm):
    """
    Runs Grover's algorithm
    """

    def __init__(self, n_qbits, marked_list):
        self.n_qbits = n_qbits
        self.marked_list = marked_list

    def launch(self,n,marked_list):
        """
        Triggers the start of Grover's algorithm
        """

        print("WOo Grover reflection worked")
        print("Hi")

        """
                Function to act grover using Qgate objects, a QReg object and a given state
                :param Reg_obj: QReg object
                    register object
                :param state: string of 1&0's etc "1100"
                    state for oracle
                :return:
                """

        # Reg_obj is register object, Reg is Quantum_Register class function
        # define number of qubits in register

        Reg_obj_state = QReg(n)
        Reg_obj_marked = QReg(n)
        
        for elm in marked_list:
            Reg_obj_marked[elm] = 1
        Reg_obj_marked.norm
        """
        #make the state into a list of 1's and 0's
        state_list = list(state)
        for i in range(len(state_list)):
            state_list[i] = int(state_list[i])
        if len(state_list) != n:
            sys.exit("the state you have supplied is for the wrong number of qubits")
        """

        # act hadamard on all qubits
        H.acts_on(Reg_obj_state, all=True)

        Reg_obj_Psi_0 = Reg_obj_state.Reg.copy()

        if (max(marked_list) + 1) ** (1 / n) > 2:
            sys.exit("An index given is too large for the register")

        # We now apply the Grover and Oracle gates in order to amplify the required state.
        n_iter = int((math.pi / 4 * math.sqrt(2 ** n))/len(marked_list))
        if n_iter == 0:
            print("n = 0 so do once")
            n_iter = 1
        print(n_iter)
    
        #now we do O and G, both with a call to the reflection operator
        # O reflects Reg around our desired states
        #don't forget *(-1): since effect is '1 - projection on s'
        # G reflecs our new Reg around the initial state of equal probability superpositions
        for _ in range (n_iter):
            -R.acts_on(-Reg_obj_state, Reg_obj_marked) 
            R.acts_on (Reg_obj_state, Reg_obj_Psi_0)
            
            
        print("The resulting quantum register should have a certain state (or states) amplified:")
        print(Reg_obj_state.Reg)
        for i in range(len(marked_list)):
            print(Reg_obj_state.Reg[marked_list[i]])








def main(n,marked_list):

    grover = Grover(n, marked_list)
    grover.launch(n,marked_list)


if __name__ == "__main__":
    main(3,[0,3])