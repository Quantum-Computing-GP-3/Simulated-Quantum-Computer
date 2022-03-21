import numpy as np

from gate import Gate
#from helpers.acts_on import Stu_acts_on, acts_on_all


class Toffoli(Gate):

    def acts_on(self, Reg_obj, q):
        '''
        function to act Toffoli
        :param Reg_obj: obj
            register
        :param q: list
            qubits to act on, expects list with three nonidentical entries
        '''

        #errors******************
        """
        #q needs to be triple with nonidentical entries
        if len(q)!= 3 or len(q) != len(set(q)):
            raise ValueError('Error: gate expects 3 nonidentical qubit arguments')
    
        #q indices need to be within the register size
        if max(q) -1 > Reg_obj.n:
            raise IndexError ('Error: the qubits you want to act on exceed the Register size')

        if isinstance(q, (list,tuple)) == False:
            raise TypeError('Error: gate expects list of qubit arguments')

        for qbit in q:
            if isinstance(qbit, (int)) == False:
                raise TypeError('Error: gate expects list of integer qubit arguments')
        """
                
        #************************
        #errors******************
        self.Error_checker(Reg_obj,q, None)
        if len(q) != 3 or len(q) != len(set(q)):
            raise ValueError('Error: gate expects 3 nonidentical qubit arguments')



        c1 = q[0]  # control position
        c2 = q[1]  # control position2
        t = q[2] #target position
        
        # sorting the list with 3 entries to fix the conditions for iteration according to qubit order
        qprime = np.sort(q)
        cond1 = 2 ** qprime[0]
        cond2 = 2 ** qprime[1]
        cond3 = 2 ** qprime[2]
        #the conditions ensure that we target and switch the correct states by defining the steps between them
        #cond1 < cond2 < cond3

        between1 = cond2 / (cond1 * 2)
        between2 = cond3 / (cond2 * 2)
        #this is the number of iterations over one of the cond-steps in alternation

        #starting from the first state where both control quits are 1
        i = 2 ** (c1) + 2 ** (c2)

        #iteration over all states for which both control qubits are 1, then define action on target
        while i < Reg_obj.N - 1:
            for _ in range(int(between2)):
                for _ in range(int(between1)):
                    for _ in range(cond1):
                        a = Reg_obj.Reg[i]
                        b = Reg_obj.Reg[i + 2 ** t] #action on t is switch states i and i+2**t
                        Reg_obj.Reg[i] = b
                        Reg_obj.Reg[i + 2 ** t] = a
                        i += 1
                    i += cond1
                i += cond2
            i += cond3

