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

        # Reg_obj_state is register object describing the whole statevector
        # Reg_obj_marked is register object containing the states-to-be-marked
        # Reg is Quantum_Register class function
        # define number n of qubits in register
        Reg_obj_state = QReg(n)
        Reg_obj_marked = QReg(n)
        
        Reg_obj_marked.Reg[0] = 0 
        #our register initialization: not as (0 0 0 0 0) but (1 0 0 0 0)^t - the state needs one nonzero entry to be normalized and a proper quantum state)
        # due to this initializtaon, one needs to manually set the first entry to zero here
        for elm in marked_list:
            Reg_obj_marked.Reg[elm] = 1

        Reg_obj_marked.norm()

        # act hadamard on all qubits
        H.acts_on(Reg_obj_state, all=True)

        Reg_obj_Psi_0 =  copy.deepcopy(Reg_obj_state)
        #store the initialized state with equal probabilities for the Grover reflection later


        #possible error: IS THIS RIGHT?????*******
        if (max(marked_list) + 1) ** (1 / n) > 2:
            sys.exit("An index given is too large for the register")
        #*****************************************


        # We now apply the Grover and Oracle gates in order to amplify the required state.
        #the number of Grover iterations is given by the following calculation
        n_iter = int((math.pi / 4 * np.sqrt(2 ** n))/len(marked_list))


        #IS THIS RIGHT``````````
        if n_iter == 0:
            print("n = 0 so do once")
            n_iter = 1
    
        #now we do O and G, both with a call to the reflection operator
        # O reflects Reg around our desired states
        #don't forget *(-1): since effect is '1 - projection on s'
        # G reflects our new Reg around the initial state of equal probability superpositions
        for _ in range (n_iter):
            R.acts_on(Reg_obj_state, Reg_obj_marked) 
            Reg_obj_state.Reg *= (-1)
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
    main(6, [3])
    t2 = time.time()
    dif= t2-t1
    print(round(dif,3))