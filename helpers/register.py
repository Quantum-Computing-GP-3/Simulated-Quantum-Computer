import numpy as np


class QuantumRegister(object):

    def __init__(self, n, simple = True, index = None, weight = None, increasing_integers = None):
        """
            THIS FUNCTION NEEDS EITHER SOLID ERROR CATCHING OR A NICER LAYOUT currently stuff will override and my brain cant think about it rn
        Initialise register object
         can add more parameters/ functions to create different starting states etc.
        :param n: int
            number of qubits in register
        :param simple: bool
            if simple [1,0,0,0...,0] array required. Overridden if other arguments supplied
        :param index: array
            index's to apply weights to
        :param weight: array
            weights to apply to index's
        :param increasing_integers: bool
            an example of different starting registers, obviously this one is uselss other than to see how cnot works


        """




        # First step is to initialise a quantum register of n qubits to the 0 state.
        reg = np.zeros((2 ** n), dtype=complex)




        self.n = n      #number of qubits
        self.N = 2**n   #length of register
        self.Reg = reg  #actual array




        #if user wants the simplest register
        if simple == True:
            #initialise with the first state = 1
            self.Reg[0] = 1

        # Useful sometimes for visualisation and troubleshooting particularly cnot
        elif increasing_integers != None:
            self.inc_int_vector()

        #if user has given index and corresponding weights, apply them
        elif (index and weight) != None:
            self.Reg[index] = weight

        #if user has incorrectly supplied weights without index or vice-versa
        elif index or weight != None:
            raise TypeError("Error: Both index and weight must be supplied, or neither.")



    def inc_int_vector(self):
        """
        useful sometimes for visualisation and troubleshooting particularly cnot

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



        
        for i in range(2 ** (self.n)):
            sum += self.Reg[i] ** 2
            #sum over all probabilities ( = (entries of register)**2)
        Norm = 1 / np.sqrt(sum)


        self.Reg *= Norm

