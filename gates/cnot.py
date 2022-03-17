import numpy as np
from gates.gate import Gate

from helpers.cartesian_products import stu_cartesian_product_n_qubits
from helpers.misc import get_state_index


class CNOT(Gate):

    def __init__(self):
        """
        initialise CNOT gate
        can be done algorithimically or by matrices, so matrices could be included.
        Either act_on could be used
        so for now, I specify to use the act_CNOT function to act it

        """
        self.matrix = (np.array([[1, 0, 0, 0],
                                 [0, 1, 0, 0],
                                 [0, 0, 0, 1],
                                 [0, 0, 1, 0]]))

        self.size = int(np.round(np.log2(self.matrix.shape[0])))
        self.tensor = np.reshape(self.matrix, (2, 2, 2, 2))

    def acts_on(self, Reg_obj, q):
        '''
        function to act CNOT
        :param Reg_obj: obj
            register
        :param q: list
            qubits to act on
        '''

        #errors**************

        #q needs to be tuple with nonidentical entries
        if len(q)!= 2 or len(q) != len(set(q)):
            raise ValueError('Error: gate expects 2 nonidentical qubit arguments')
    
        #q indices need to be within the register size
        if max(q) -1 > Reg_obj.n:
            raise IndexError ('Error: the qubits you want to act on exceed the Register size')
        #********************


        c = q[0]  # control position
        t = q[1]  # target position

        i = 0
        #qprime = np.sort(q)  # yes I am sorting a list of size 2

        qprime = sorted(q)
        cond1 = 2 ** qprime[0]
        cond2 = 2 ** qprime[1]
        between = cond2 / (cond1 * 2)

        #starting index is first one where control qubit is 1
        i = 2 ** (c)


        while i < Reg_obj.N - 1:
            for _ in range(int(between)):
                for _ in range(cond1):
                    a = Reg_obj.Reg[i]
                    b = Reg_obj.Reg[i + 2 ** t]
                    Reg_obj.Reg[i] = b
                    Reg_obj.Reg[i + 2 ** t] = a
                    i += 1
                i += cond1
            i += cond2
