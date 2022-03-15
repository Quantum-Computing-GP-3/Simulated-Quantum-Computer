import numpy as np


from gates.gate import Gate

from helpers.cartesian_products import stu_cartesian_product_n_qubits
from helpers.misc import get_state_index


class Pauli_X(Gate):



    def acts_on(self, Reg_obj, q):

        '''
        function to act X
        :param Reg_obj: obj
            register
        :param q: list
            qubits to act on
        :param all: bool
            whether X should be acted on all qubits
        :param state:
            state for oracle
        '''
        if all == True:
            q = [i for i in range(Reg_obj.n)]

        Reg_obj.Reg

        # error if q is not ???
        for qbit in q:
            i = 0
            while i <= Reg_obj.N - 2 ** qbit:
                # print(i)
                for _ in range(2 ** qbit):
                    a = Reg_obj.Reg[i]
                    b = Reg_obj.Reg[i + 2 ** qbit]
                    Reg_obj.Reg[i] = b
                    Reg_obj.Reg[i + 2 ** qbit] = a
                    i += 1
                i += 2 ** qbit

