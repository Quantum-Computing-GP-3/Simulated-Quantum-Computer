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
from grover_gate import Grover
from oracle import Oracle
from register import QuantumRegister as QReg
import numpy as np
import math
H = Hadamard()
G = Grover()
O = Oracle()

class Grover(Algorithm):
    """
    Runs Grover's algorithm
    """

    def __init__(self, n_qbits, marked_list):
        self.n_qbits = n_qbits
        self.marked_list = marked_list

    def launch(self,n,marked_list):
        """
        Triggers the start of Grover's algorithm
        Function to act grover using Qgate objects, a QReg object and a given state
            :param Reg_obj: QReg object
                register object
            :param state: string of 1&0's etc "1100"
                state for oracle
            :return:
        """

        if len(marked_list)>=2**(self.n_qbits-1):
            raise TypeError("Error: The number of searchg states supplied must be less than half the size of the register")


        # Reg_obj is register object, Reg is Quantum_Register class function
        # define number n of qubits in register
        Reg_obj = QReg(n)

        # act hadamard on all qubits
        H.acts_on(Reg_obj, all=True)

        #errors: IS THIS RIGHT????????
        if (max(marked_list) + 1) ** (1 / n) > 2:
            sys.exit("An index given is too large for the register")

        # We now apply the Grover and Oracle gates in order to amplify the required state.
        #the number of Grover iterations is given by the following calculation
        n_iter = int((math.pi / 4 * math.sqrt(2 ** n))/len(marked_list))
        
        if n_iter == 0:
            print("n = 0 so do once")
            n_iter = 1

        #do Grover iteration
        for i in range(n_iter):
            O.acts_on(Reg_obj, marked_list)
            G.acts_on(Reg_obj)

        print("The resulting quantum register should have a certain state (or states) amplified:")
        print(Reg_obj.Reg)
        for i in range(len(marked_list)):
            print(Reg_obj.Reg[marked_list[i]])






def main(n,marked_list):

    grover = Grover(n, marked_list)
    grover.launch(n,marked_list)


if __name__ == "__main__":
    main(3, [0, 1, 3])

    """
    print('5,    [0,3] \n')
    main(5,[0,3])
    print('6,    [2] \n')
    main(6,[2])
    print('4,    [1,2,3] \n')
    main(4,[1,2,3])
    print('5,    [0,30] \n')
    main(5,[0, 30])
    print('5,    [10] \n')

    main(5,[10])
    """


