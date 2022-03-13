import numpy as np
class Quantum_Register(object):

    def __init__(self, n, increasing_integers = False):
        """
        Initialise register object
         can add more parameters/ functions to create different starting states etc.
        :param n: int
            number of qubits in register
        :param increasing_integers: bool
            an example of different starting registers, obviously this one is uselss other than to see how cnot works

        """


        # First step is to initialise a quantum register of n qubits to the 0 state.
        reg = np.zeros((2 ** n), dtype=complex)
        #for now, initialise with the first state = 1
        reg[0] = 1


        self.n = n
        self.N = 2**n
        self.Reg = reg


        #useful sometimes for visualisation and troubleshooting particularly cnot
        if increasing_integers == True:
            self.inc_int_vector()


    def tensor_notation(self):
        """
        converts self.Reg from vector to tensor notation
        useful for using with pablo's original act_on
        :return:
        """
        self.Reg = np.reshape(self.Reg, (2,)*self.n)

        return

    def vector_notation(self):
        """
        converts self.Reg from vector to tensor notation
        useful for using with pablo's original act_on
        :return:
        """
        self.Reg = self.Reg.flatten()
        return


    def inc_int_vector(self):
        """
        useful sometimes for visualisation and troubleshooting particularly cnot
        :return:
        """
        for i in range(2**self.n):
            self.Reg[i] = i
        return



    def Norm(self):

        sum = 0

        for i in range (self.N):
            sum += self.Reg[i]**2
        Norm = 1/np.sqrt(sum)
        self.Reg = Norm*self.Reg
