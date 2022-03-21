from gate import Gate
import sys
#sys.path.append ('C:/Users/mabon/Documents/GitHub/Simulated-Quantum-Computer/helpers')
#from E_checker import Error_checker


from cartesian_products import stu_cartesian_product_n_qubits
from misc import get_state_index


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
        #Error_checker(q, Reg_obj, all)

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

