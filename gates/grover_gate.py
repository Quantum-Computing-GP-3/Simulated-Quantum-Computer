import numpy as np
from .gate import Gate
from helpers.register import QuantumRegister as QReg


class Grover(Gate):

    def Error_checker(self, Reg_obj):
        if isinstance(Reg_obj, QReg) != True:
            raise TypeError("Error: gate expects register object as input")

    def acts_on(self, Reg_obj):
        """
        function to act grovers operator thingy
        :param Reg_obj: obj
            Register object
        """

        # errors***************
        self.Error_checker(Reg_obj)

        n = Reg_obj.n  # number of qubits
        N = Reg_obj.N  # length of register

        diag = 2 / N - 1  # diagonal entries of grover matrix
        rest = 2 / N  # entries on non-diagonals of grover matrix

        reg_old = Reg_obj.Reg
        # we don't necessarily need this to be a register object; an array does
        # the work as well
        reg_new = np.zeros(N, dtype="complex")

        # act the 'matrix' on the statevectorregister
        for i in range(N):
            for j in range(N):
                if i == j:
                    reg_new[i] += diag * reg_old[j]
                else:
                    reg_new[i] += rest * reg_old[j]

        Reg_obj.Reg = reg_new  # update register state vector
