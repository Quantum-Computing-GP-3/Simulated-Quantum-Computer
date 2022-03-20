import numpy as np
from gate import Gate
import sys
sys.path.append ('C:/Users/admin/Documents/GitHub/Simulated-Quantum-Computer/helpers')
from cartesian_products import stu_cartesian_product_n_qubits
from misc import get_state_index



class CNOT(Gate):

    def __init__(self):
        """
        initialise CNOT gate
        can be done algorithimically or by matrices, so matrices could be included.
        """
        #IS THIS STILL NECESSARY??
        self.matrix = (np.array([[1, 0, 0, 0],
                                 [0, 1, 0, 0],
                                 [0, 0, 0, 1],
                                 [0, 0, 1, 0]]))

        self.size = int(np.round(np.log2(self.matrix.shape[0])))
        self.tensor = np.reshape(self.matrix, (2, 2, 2, 2))

    def acts_on(self, Reg_obj, q):
        '''
        function to act CNOT
        :param Reg_obj: QReg object
            register for state vector
        :param q: list
            qubits to act on
        '''

        #errors**************
        """
        #q needs to be tuple with nonidentical entries
        if len(q)!= 2 or len(q) != len(set(q)):
            raise ValueError('Error: gate expects 2 nonidentical qubit arguments')
    
        #q indices need to be within the register size
        if max(q) -1 > Reg_obj.n:
            raise IndexError ('Error: the qubits you want to act on exceed the Register size')
        #********************
        """

        c = q[0]  # control position
        t = q[1]  # target position

        i = 0

        if c < t:
            cond1 = 2 **c
            cond2 = 2 **t
        else:
            cond1 = 2**t
            cond2 = 2**c
        #these two conditions define the steps that have to be taken to target the right register indices/basis states
        #cond1 < cond2        
        
        between = cond2 / (cond1 * 2)

        #starting index is first one where control qubit is 1
        i = 2 ** (c)

        while i < Reg_obj.N - 1:
            for _ in range(int(between)):
                for _ in range(cond1):
                    a = Reg_obj.Reg[i]
                    b = Reg_obj.Reg[i + 2 ** t] #CNOT flips the entries of state i and state i+2**t
                    Reg_obj.Reg[i] = b
                    Reg_obj.Reg[i + 2 ** t] = a
                    i += 1
                i += cond1
            i += cond2
