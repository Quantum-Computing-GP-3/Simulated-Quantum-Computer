import numpy as np

from gates.gate import Gate
#from helpers.acts_on import Stu_acts_on, acts_on_all


class Toffoli(Gate):

    def acts_on(self, Reg_obj, q=None, all=False, state=None):

        # error catching if q is not a 3 tupel
        '''
        function to act CNOT
        :param Reg_obj: obj
            register
        :param q: list
            qubits to act on
        :param all: bool
            whether Hadamard should be acted on all qubits
        :param state:
            state for oracle
        '''
        size = 2 ** (Reg_obj.n)
        reg = Reg_obj.Reg

        if all == True:
            return 1  # error!

        c1 = q[0]  # control position
        c2 = q[1]  # control position2
        t = q[2]
        #qprime = np.sort(q)  # sorting a list with 3 entries
        qprime = sorted(q)
        cond1 = 2 ** qprime[0]
        cond2 = 2 ** qprime[1]
        cond3 = 2 ** qprime[2]
        between1 = cond2 / (cond1 * 2)
        between2 = cond3 / (cond2 * 2)

        i = 2 ** (c1) + 2 ** (c2)

        while i < size - 1:
            for _ in range(int(between2)):
                for _ in range(int(between1)):
                    for _ in range(cond1):
                        a = reg[i]
                        b = reg[i + 2 ** t]
                        reg[i] = b
                        reg[i + 2 ** t] = a
                        i += 1
                    i += cond1
                i += cond2
            i += cond3
        Reg_obj.Reg = reg
