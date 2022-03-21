import numpy as np


class QuantumRegister(object):

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
        #For now, initialise with the first state = 1
        reg[0] = 1

        self.n = n     #number of qubits
        self.N = 2**n  #length of register
        self.Reg = reg

        # Useful sometimes for visualisation and troubleshooting particularly cnot
        if increasing_integers:
            self.inc_int_vector()


    def inc_int_vector(self):
        """
        useful sometimes for visualisation and troubleshooting particularly cnot
        :return:
        """
        for i in range(2**self.n):
            self.Reg[i] = i
        return


    def norm(self):
        '''
        function to normalize state
        '''

        # errors*************************

        # *******************************

        sum = 0

        # sprint('testnorm')

        for i in range(2 ** (self.n)):
            sum += self.Reg[i] *np.conjugate(self.Reg[i])
            # print('within norm', self.Reg[i]**2)
        Norm = 1 / np.sqrt(sum)

        # print("hi")
        # print(self.Reg)
        # print(Norm)

        # self.Reg = [Norm * i for i in self.Reg]


        
        for i in range(2 ** (self.n)):
            sum += self.Reg[i] ** 2
            #sum over all probabilities ( = (entries of register)**2)
        Norm = 1 / np.sqrt(sum)


        self.Reg *= Norm

