from gates.gate import Gate

from helpers.cartesian_products import stu_cartesian_product_n_qubits
from helpers.misc import get_state_index


class Pauli_X(Gate):
    def acts_on(self, Reg_obj, q, all = False):
        '''
        function to act X
        :param Reg_obj: obj
            register
        :param q: list
            qubits to act on
        :param all: bool
            whether X should be acted on all qubits
        '''


        #errors *********

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

        #****************

        if all == True:
            q = [i for i in range(Reg_obj.n)]

        
        for qbit in q:
            i = 0
            while i <= Reg_obj.N - 2 ** qbit:
                for _ in range(2 ** qbit):
                    a = Reg_obj.Reg[i]
                    b = Reg_obj.Reg[i + 2 ** qbit]
                    Reg_obj.Reg[i] = b
                    Reg_obj.Reg[i + 2 ** qbit] = a
                    i += 1
                i += 2 ** qbit

