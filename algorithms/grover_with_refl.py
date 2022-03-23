from .algorithm import Algorithm
import sys

import numpy as np
from gates.hadamard import Hadamard
import copy
from gates.reflection import Reflection
import time
from helpers.register import QuantumRegister as QReg
import math
import matplotlib.pyplot as plt
H = Hadamard()
R = Reflection()


class Grover_Reflection(Algorithm):
    """
    Runs Grover's algorithm
    """

    def __init__(self, n_qbits, marked_list):
        self.n_qbits = n_qbits
        self.marked_list = marked_list

    def launch(self):
        """


        Function to act grover using Qgate objects, a QReg object and a given state
            :param Reg_obj: QReg object
                register object
            :param state: string of 1&0's etc "1100"
                state for oracle
            :return:

                """

        if len(self.marked_list) >= 2**(self.n_qbits - 1):
            raise TypeError(
                "Error: The number of searching states supplied must be less than half the size of the register")

        if (max(self.marked_list) + 1) ** (1 / self.n_qbits) > 2:
            sys.exit("An index given is too large for the register")


        # Reg_obj_state is register object describing the whole statevector
        # Reg_obj_marked is register object containing the states-to-be-marked
        # Reg is Quantum_Register class function
        # define number n of qubits in register

        #pass the desired states-to-be-marked as 2d array to the register to initialise a register object that contains all states-to-be-marked
        stateentries = np.array([self.marked_list, np.ones(len(self.marked_list), dtype ='int')])
 
        Reg_obj_state = QReg(self.n_qbits)
        Reg_obj_marked = QReg(self.n_qbits, weights = stateentries)
        Reg_obj_marked.norm()
        
    
        # act hadamard on all qubits
        H.acts_on(Reg_obj_state, all=True)

        Reg_obj_Psi_0 = copy.deepcopy(Reg_obj_state)
        # store the initialized state with equal probabilities for the Grover reflection later

  
        

        # We now apply the Grover and Oracle gates in order to amplify the required state.
        # the number of Grover iterations is given by the following calculation
        n_iter = int((math.pi / 4 * np.sqrt(2 ** self.n_qbits)) / np.sqrt(len(self.marked_list)))

        #due to the approximation in the iteration number, there might be cases, where n_iter is between 0 and 1 -> int(n_iter) = 0
        #in these cases, n_iter is set to 1
        if n_iter == 0:
            n_iter = 1

 
        # now we do O and G, both with a call to the reflection operator
        # O reflects Reg around our desired states
        # don't forget *(-1): since effect is '1 - projection on s'
        # G reflects our new Reg around the initial state of equal probability
        # superpositions
        for _ in range(n_iter):
            R.acts_on(Reg_obj_state, Reg_obj_marked)
            Reg_obj_state.Reg *= (-1)
            R.acts_on(Reg_obj_state, Reg_obj_Psi_0)


        print("The resulting quantum register should have a certain state (or states) amplified:")
        if self.n_qbits <=4:
            print(Reg_obj_state.Reg)
        for i in range(len(self.marked_list)):
            print('probability of amplified state', i, 'is',Reg_obj_state.Reg[self.marked_list[i]])

        self.barchart(Reg_obj_state)






    def barchart(self, Reg_obj):

        Reals = np.real(Reg_obj.Reg) #we only work with real entries for Grover, but the register is set up more generalized
        Reals = np.abs(Reals)

        maximum = np.max(Reals)
        arg_max = np.argwhere(np.isclose(Reals, maximum))
        max_arr = Reals[arg_max]
        strings = []

        for n in range(0, len(arg_max[:, 0])):
            # append index
            strings.append(str(arg_max[n, 0]))
  
        strings.append("all others")
        minimum = np.min(Reals) #we know that all other states should have the same probability amplitude (aside from numerical accuracy errors)
        full_arr = np.append(max_arr, minimum)

        plt.title("Quantum Register after Grover's Algorithm")
        plt.xlabel("Basis states in decimal representation")
        plt.ylabel("Probability of measuring basis state")
        plt.bar(strings, np.real(full_arr ** 2), color="teal")
        plt.show()






#main to run the algorithm
def main(n, marked_list):
    grover = Grover_Reflection(n, marked_list)
    grover.launch()


if __name__ == "__main__":
    start = time.time()
    main(5, [1, 2, 8])
    end = time.time()
    diff = end - start

