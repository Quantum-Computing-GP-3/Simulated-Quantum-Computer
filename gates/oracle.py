import sys
import numpy as np

from .gate import Gate


class Oracle(Gate):

    def __init__(self, state):
        self.state = state

    def acts_on(self, Reg_obj, q):
        """
        function to act oracle
        :param Reg_obj: obj
            Register object
        :param q: list
            qubit(s) to act on
        :return Reg_obj: Updated register
        """
        n = Reg_obj.n
        matrix_O = np.eye(2**n)

        # We check that "state" has the same length as the number of qubits in the register.
        if len(self.state) != n:
            sys.exit(
                "The state the oracle should single out is not a valid basis state of the quantum register.")
        # "state" is then converted to decimal in order to modify the correct
        # diagonal entry of the Oracle matrix representation.
        matrix_O[int(self.state, 2), int(self.state, 2)] = -1

        # if the gate is actually an operator (like G or O)
        Reg_obj.Reg = np.matmul(matrix_O, Reg_obj.Reg)
        Reg_obj.vector_notation()
        return Reg_obj
