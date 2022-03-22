import numpy as np


class QuantumRegister(object):

    def __init__(self, n, weights = None, increasing_integers = None):
        """
         Initialise register object

         If no optional arguments given, simple register of form [1,0,0...,0] will be made.

        :param n: int
            number of qubits in register

        :param weights: (2xN) array
            N weights to apply to N index's, where index's are first row and weights are column

        :param increasing_integers: bool
            Forms a register of increasing values with index


        """




        # First step is to initialise a quantum register of n qubits to the 0 state.
        reg = np.zeros((2 ** n), dtype=complex)


        self.n = n      #number of qubits
        self.N = 2**n   #length of register
        self.Reg = reg  #actual array



        #if user has given index and corresponding weights, apply them
        if isinstance(weights, np.ndarray) == True:
            index = weights[0, :]
            weight = weights[1, :]
            self.Reg[index] = weight

        # Useful sometimes for visualisation and troubleshooting particularly cnot
        elif increasing_integers != None:
            self.inc_int_vector()

        # if user wants the simplest register
        else:
            # initialise with the first state = 1
            self.Reg[0] = 1

        self.norm()
        print(self.Reg)


    def inc_int_vector(self):
        """
        Forms a register of increasing values with index
        useful sometimes for visualisation and troubleshooting particularly  visualising cnot

        updates self.Reg with a register of increasing integer values.
        This is very useful for troubleshooting and visualisation of index etc,
        """
        for i in range(2**self.n):
            self.Reg[i] = i
        return


    def norm(self):
        '''
        function to normalize state
        '''


        sum = 0

        for i in range(2 ** (self.n)):
            sum += self.Reg[i] *np.conjugate(self.Reg[i])
            # print('within norm', self.Reg[i]**2)
        Norm = 1 / np.sqrt(sum)

        self.Reg *= Norm

