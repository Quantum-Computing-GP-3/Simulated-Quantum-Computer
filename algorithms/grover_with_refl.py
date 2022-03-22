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

        if len(self.marked_list)>=2**(self.n_qbits-1):
            raise TypeError("Error: The number of searching states supplied must be less than half the size of the register")


        # Reg_obj_state is register object describing the whole statevector
        # Reg_obj_marked is register object containing the states-to-be-marked
        # Reg is Quantum_Register class function
        # define number n of qubits in register
        Reg_obj_state = QReg(self.n_qbits)
        Reg_obj_marked = QReg(self.n_qbits)
        
        Reg_obj_marked.Reg[0] = 0 
        #our register initialization: not as (0 0 0 0 0) but (1 0 0 0 0)^t - the state needs one nonzero entry to be normalized and a proper quantum state)
        # due to this initializtaon, one needs to manually set the first entry to zero here
        for elm in self.marked_list:
            Reg_obj_marked.Reg[elm] = 1

        Reg_obj_marked.norm()

        # act hadamard on all qubits
        H.acts_on(Reg_obj_state, all=True)

        Reg_obj_Psi_0 =  copy.deepcopy(Reg_obj_state)
        #store the initialized state with equal probabilities for the Grover reflection later


        #possible error: IS THIS RIGHT?????*******
        if (max(self.marked_list) + 1) ** (1 / self.n_qbits) > 2:
            sys.exit("An index given is too large for the register")



        # We now apply the Grover and Oracle gates in order to amplify the required state.
        #the number of Grover iterations is given by the following calculation
        n_iter = int((math.pi / 4 * np.sqrt(2 ** self.n_qbits))/len(self.marked_list))*2


        #IS THIS RIGHT``````````
        if n_iter == 0:
            print("n = 0 so do once")
            n_iter = 1
    
        print(n_iter)
        #print('beide regs',Reg_obj_state.Reg, Reg_obj_marked.Reg)
        #now we do O and G, both with a call to the reflection operator
        # O reflects Reg around our desired states
        #don't forget *(-1): since effect is '1 - projection on s'
        # G reflects our new Reg around the initial state of equal probability superpositions
        for _ in range (n_iter):
            R.acts_on(Reg_obj_state, Reg_obj_marked) 
           # print(Reg_obj_state.Reg)
            Reg_obj_state.Reg *= (-1)
            R.acts_on (Reg_obj_state, Reg_obj_Psi_0)
            print('after',Reg_obj_state.Reg)
            
            
        print("The resulting quantum register should have a certain state (or states) amplified:")
        #print(Reg_obj_state.Reg)
        for i in range(len(self.marked_list)):
            print(Reg_obj_state.Reg[self.marked_list[i]])

        self.barchart(Reg_obj_state)



    def barchart(self,Reg_obj):


        Reals = np.real(Reg_obj.Reg)
        Reals = np.abs(Reals)

        maximum = np.max(Reals)
        arg_max = np.argwhere(np.isclose(Reals, maximum))
        max_arr = Reals[arg_max]
        strings = []

        for n in range(0,len(arg_max[:,0])):
            strings.append(str(bin(arg_max[n,0])))


        #find binary string values
        for s in range(len(strings)):
            string = strings[s].lstrip("0")
            string = string.lstrip("b")
            strings[s] = string

        strings.append("all others")
        minimum = np.min(Reals)
        full_arr = np.append(max_arr, minimum)


        plt.title("Amplified states")
        plt.xlabel("Binary state")
        plt.ylabel("Probability")
        plt.bar(strings, np.real(full_arr**2), color = "teal")
        plt.show()




def main(n,marked_list):

    grover = Grover_Reflection(n, marked_list)
    grover.launch(n,marked_list)


if __name__ == "__main__":
   # print('5,    [0,3] refl \n')
    #main(5,[0,3])
    #print('6,    [2] refl \n')
    #main(6,[2])
    #print('4,    [1,2,3] refl \n')
    #main(4,[1,2,3])
    #print('5,    [0,30] refl \n')
    #main(5,[0, 30])
    #print('5,    [10] refl \n')
    #main(5,[10])
    t1 = time.time()

    #main(5, [0,1,3])
    #main(3, [1,2,3])
    main(10, [1])
    t2 = time.time()
    dif= t2-t1
    print(round(dif,3))