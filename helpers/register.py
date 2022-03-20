import numpy as np
import sys
sys.path.append ('C:/Users/admin/Documents/GitHub/Simulated-Quantum-Computer/gates')
from pauli_X import Pauli_X as X
from pauli_Z import Pauli_Z as Z
import math
import numpy as np
X = X()
Z = Z()


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
        converts self.Reg from tensor to vector notation
        useful for using with Stuart's algorithms
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

    def error_channel(self, q, pbit=0., psign=0.):
        """
        :param q: integer
            qubit that the error_channel actson
        :param pbit: real number between 0 and 1
            probability of bitflip
        :param psign: real number between 0 and 1
            probability of signflip

        error channel is the channel that corrupts the single qubit with certain probability
        it acts on a qubit q. for the easiest case of shor's algorithm, there is only one
        possible qubit to act on and that is qbit 0
        """

        #errors*************
        """
        #q index needs to be within the register size
        if q -1 > self.n:
            raise IndexError ('Error: the qubit you want to act on with error_channel exceeds the Register size')

        #type of q is int (qbit number from 0 to n-1)
        if isinstance(q, (int)) == False:
            raise TypeError('Error: error_channel expects list of integer qubit arguments')
        """
        #*******************



        # now decide randomly if qbit will be corrupted
        # this depends on the corruption probability
        # with this one can tune the noise up or down
        corruptionbit = np.random.random()
        corruptionsign = np.random.random()

        if corruptionsign < psign:
            print('signcorruption')
            Z.acts_on(self, q)
        else:
            print('no signcorruption')

        if corruptionbit < pbit:
            print('bitcorruption')
            X.acts_on(self, q)
        else:
            print('no bitcorruption')


    def norm(self):
        '''
        function to normalize state
        '''

        #errors*************************


        #*******************************

        sum = 0
        
        for i in range(2 ** (self.n)):
            sum += self.Reg[i] ** 2
            #sum over all probabilities ( = (entries of register)**2)
        Norm = 1 / np.sqrt(sum)

        self.Reg *= Norm




