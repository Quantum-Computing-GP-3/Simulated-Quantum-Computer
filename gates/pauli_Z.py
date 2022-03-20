from gate import Gate
import sys
sys.path.append ('C:/Users/admin/Documents/GitHub/Simulated-Quantum-Computer/helpers')
from cartesian_products import stu_cartesian_product_n_qubits
from misc import get_state_index


class Pauli_Z(Gate):

    def acts_on(self, Reg_obj, q, all = False):
        '''
                function to act Z
                :param Reg_obj: obj
                    register
                :param q: list
                    qubits to act on
                :param all: bool
                    whether Z should be acted on all qubits
                '''

        #errors***************

       #q indices need to be within the register size
        if max(q) -1 > Reg_obj.n:
            raise IndexError ('Error: the qubits you want to act on exceed the Register size')

        #type of q is list or similar
        if isinstance(q, (list,tuple)) == False:
            raise TypeError('Error: gate expects list of qubit arguments')

        #type of each entry in q is int (qbit number from 0 to n-1)
        for qbit in q:
            if isinstance(qbit, (int)) == False:
                raise TypeError('Error: gate expects list of integer qubit arguments')

        #*********************

        if all == True:
            q = [i for i in range(Reg_obj.n)]

        for qbit in q:
            i = 2 ** qbit
            while i <= Reg_obj.N - 1:
                for _ in range(2 ** qbit):
                    Reg_obj.Reg[i] = Reg_obj.Reg[i] * (-1)
                    i += 1
                i += 2 ** qbit


