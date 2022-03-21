from gate import Gate
#from helpers.acts_on import Stu_acts_on, acts_on_all
import math



class Hadamard(Gate):

    def acts_on(self, Reg_obj, q = None, all = None):
        '''
        function to act Hadamard
        :param Reg_obj: obj
            register
        :param q: list
            qubits to act on
        :param all: bool
            whether Hadamard should be acted on all qubits
        '''

        self.Error_checker(Reg_obj, q, all)
        if all == True:
            q = [i for i in range(Reg_obj.n)]



        if all == True:
            q = [i for i in range(Reg_obj.n)]

        for qbit in q: 
            #Hadamard action separately for each selected qubit in the passed q list
            i = 0 
            #i is iteration of H action on qbit over the basis states;
            # due to handling action of two states simultaneously, that makes N/2 iterations

            while i <= Reg_obj.N - 2 ** qbit:
                for _ in range(2 ** qbit):
                    a = Reg_obj.Reg[i]
                    b = Reg_obj.Reg[i + 2 ** qbit]
                    # for H acting on state i, we need to find out the two states that are the result of H acting on i
                    # those are i and i+2**qbit
                    # since those are the same as the states involved for H acting on i+2**qbit, we take care of the
                    # action of H on both states at once -> less looping

                    #then we need to redefine the amplitudes of states i and i+2**qbit, considering the action of H
                    Reg_obj.Reg[i] = 1 / math.sqrt(2) * (a + b)
                    Reg_obj.Reg[i + 2 ** qbit] = 1 / math.sqrt(2) * (a - b)
                    
                    i += 1
                i += 2 ** qbit
                # the variation of the step width achieves that we don't loop over any second state i+2**qbit again that we already took care of
