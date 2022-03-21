from gate import Gate
import sys
sys.path.append ('C:/Users/admin/Documents/GitHub/Simulated-Quantum-Computer/helpers')
from cartesian_products import stu_cartesian_product_n_qubits
from misc import get_state_index


class Pauli_Z(Gate):

    def acts_on(self, Reg_obj, q = None, all = None):
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
        self.Error_checker(Reg_obj, q, all)


        if all == True:
            q = [i for i in range(Reg_obj.n)]

        #action of Z: signflip if qbit is 1
        for qbit in q:
            i = 2 ** qbit
            while i <= Reg_obj.N - 1:
                for _ in range(2 ** qbit):
                    Reg_obj.Reg[i] = Reg_obj.Reg[i] * (-1)
                    i += 1
                i += 2 ** qbit


