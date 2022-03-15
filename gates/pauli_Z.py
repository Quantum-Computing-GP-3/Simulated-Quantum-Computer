import numpy as np


from gates.gate import Gate

from helpers.cartesian_products import stu_cartesian_product_n_qubits
from helpers.misc import get_state_index


class Pauli_Z(Gate):



    def acts_on(self, Reg_obj, q):
        '''
                function to act Z
                :param Reg_obj: obj
                    register
                :param q: list
                    qubits to act on
                :param all: bool
                    whether Z should be acted on all qubits
                :param state:
                    state for oracle
                '''
        if all == True:
            q = [i for i in range(Reg_obj.n)]


        # error if q is not ???

        for qbit in q:
            print(qbit)
            i = 2 ** qbit
            while i <= Reg_obj.N - 1:
                for _ in range(2 ** qbit):
                    Reg_obj.Reg[i] = Reg_obj.Reg[i] * (-1)
                    i += 1
                i += 2 ** qbit


