from algorithm import Algorithm
import sys
"""
sys.path.append ('C:/Users/admin/Documents/GitHub/Simulated-Quantum-Computer/gates')
sys.path.append ('C:/Users/admin/Documents/GitHub/Simulated-Quantum-Computer/helpers')
sys.path.append ('C:/Users/admin/Documents/GitHub/Simulated-Quantum-Computer/register')
"""
sys.path.append ('C:/Users/stuar/OneDrive - University of Edinburgh/Documents/GitHub/Simulated-Quantum-Computer/gates')
sys.path.append ('C:/Users/stuar/OneDrive - University of Edinburgh/Documents/GitHub/Simulated-Quantum-Computer/helpers')
sys.path.append ('C:/Users/stuar/OneDrive - University of Edinburgh/Documents/GitHub/Simulated-Quantum-Computer/register')

from hadamard import Hadamard
import copy
from reflection import Reflection
import time
from register import QuantumRegister as QReg
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
        

        a = 0
        for elm in marked_list:
            Reg_obj_marked.Reg[elm] = 1
            if elm == 0:
                a += 1 
        if a == 0:
            Reg_obj_marked.Reg[0] = 0

        Reg_obj_marked.norm
        Reg_obj_state.norm
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

        Reg_obj_Psi_0 =  copy.deepcopy(Reg_obj_state)

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
            R.acts_on(Reg_obj_state, Reg_obj_marked) 
            Reg_obj_state.Reg *= (-1)
            #print(Reg_obj_state.Reg)
            R.acts_on (Reg_obj_state, Reg_obj_Psi_0)
            
            
        print("The resulting quantum register should have a certain state (or states) amplified:")
        print(Reg_obj_state.Reg)
        for i in range(len(marked_list)):
            print(Reg_obj_state.Reg[marked_list[i]])
            







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
    main(3, [0,1,3,5,6,7])
    t2 = time.time()
    dif= t2-t1
    print(round(dif,3))