import numpy as np
from gates.pauli_X import Pauli_X as X
from gates.pauli_Z import Pauli_Z as Z
import math
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
        #reg = np.zeros((2 ** n), dtype=complex)
        # For now, initialise with the first state = 1
        #reg[0] = 1
        #print(reg)
        reg = [0,]*2**n
        reg[0] = 1
        print(reg)


        self.n = n
        self.N = 2**n
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
        # YES THIS NEEDS PBIT AND PSIGN
        # MAYBE A **KWARGS ARGUMENT WOULD BE BETTER FOR THE QUANTUM GATE CLASS
        """
        error channel is the channel that corrupts the single qubit with certain probability
        pbit: prob of bitflip
        psign: prob of signflip
        it acts on a qubit q. for the easiest case of just shor's algorithm there is only one
        possible qubit to act on and that is qbit 0
        since it acts using X and Z, it is a Quantum
        """

        # now decide randomly if qbit will be corrupted
        # this depends on the corruption probability
        # with this one can tune the noise up or down
        corruptionbit = np.random.random()
        corruptionsign = np.random.random()

        if corruptionbit < pbit:
            print('bitcorruption')
            X.acts_on(self, q)
        else:
            print('no bitcorruption')

        if corruptionsign < psign:
            print('signcorruption')
            Z.acts_on(self, q)
        else:
            print('no signcorruption')

    def norm(Reg_obj, q=None, all=False, state=None):
        '''
        function to normalize state
        :param Reg_obj: obj
            register
        :param q: list
            qubits to act on
        :param all: bool
            whether gate should be acted on all qubits
        :param state:
            state for oracle
        '''
        # errorcatching:
        if all == True:
            return 1

        sum = 0


        for i in range(2 ** (Reg_obj.n)):
            sum += Reg_obj.Reg[i] ** 2
        Norm = 1 / math.sqrt(sum)

        print("hi")
        print(Reg_obj.Reg)
        print(Norm)

        Reg_obj.Reg = [Norm * i for i in Reg_obj.Reg]

        #Reg_obj.Reg *= Norm




