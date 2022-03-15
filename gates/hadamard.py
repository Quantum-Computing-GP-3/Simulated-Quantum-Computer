import numpy as np

<<<<<<< Updated upstream
from gate import Gate
from helpers.acts_on import Stu_acts_on, acts_on_all
=======
from gates.gate import Gate
#from helpers.acts_on import Stu_acts_on, acts_on_all
>>>>>>> Stashed changes


class Hadamard(Gate):

    def __init__(self, all=None):
        """
        Initialise Hadamard gate
        """
        self.matrix = 1/np.sqrt(2)*np.array([[1, 1],
                                             [1, -1]])
        self.size = int(np.round(np.log2(self.matrix.shape[0])))

        self.tensor = np.reshape(self.matrix, (2, 2))

        self.all = all

    def acts_on(self, Reg_obj, q = None, all = None):
        # cosiv2
        '''
        function to act Hadamard
        :param Reg_obj: obj
            register
        :param q: list
            qubits to act on
        :param all: bool
            whether Hadamard should be acted on all qubits
        :param state:
            state for oracle
        '''
        if all == True:
            q = [i for i in range(Reg_obj.n)]

        reg = Reg_obj.Reg
        size = 2 ** (Reg_obj.n)

        for qbit in q:
            i = 0
            # print(j)
            while i <= size - 2 ** qbit:
                for _ in range(2 ** qbit):
                    # print('i',i)
                    a = reg[i]
                    b = reg[i + 2 ** qbit]
                    # for H acting on state i, we need to find out the two states that are the result of H acting on i
                    # those are i and i+2**qbit
                    # since those are the same as the states involved for H acting on i+2**qbit, we take care of the
                    # action of H on both states at once -> less looping

                    # print(a,b, a+b, a-b)
                    reg[i] = 1 / np.sqrt(2) * (a + b)
                    reg[i + 2 ** qbit] = 1 / np.sqrt(2) * (a - b)
                    # then we need to redefine the amplitudes of states i and i+2**qbit, considering the action of H

                    # print(i, reg[i], i+2**j, reg[i+2**j], -2/np.sqrt(2))
                    i += 1
                i += 2 ** qbit
                # the variation of the step width achieves that we don't loop over any second state i+2**qbit again that we already took care of
        Reg_obj.Reg = reg
