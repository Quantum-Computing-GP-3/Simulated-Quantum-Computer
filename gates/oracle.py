import sys
import numpy as np

<<<<<<< Updated upstream
from gate import Gate
=======
from gates.gate import Gate
>>>>>>> Stashed changes


class Oracle(Gate):

    #def __init__(self):
    #self.state = state

    def acts_on(self, Reg_obj, state_list):
        """
        function to act oracle
        :param Reg_obj: obj
            Register object
        :param q: list
            qubit(s) to act on
        :param all: bool
            Whether or not th egate should be acted on all qubits
        :param state: string of 1&0's etc "1100"
            state for oracle
        :return:
        """
        n = Reg_obj.n
        """
        #original matrix implimentation which is slower:
        matrix_O = np.eye(2**n)
        #applying a -1 in the matrix for each state in state_list
        for i in range(len(state_list)):
            matrix_O[state_list[i], state_list[i]] = -1
        #if the gate is actually an operator (like G or O)
        Reg_obj.Reg = np.matmul(matrix_O, Reg_obj.Reg)
        """
        #new, non matrix implimentation
        for i in range(len(state_list)):
            #assumes numerical state
            idx = state_list[i]
            Reg_obj.Reg[idx] = - Reg_obj.Reg[idx]
