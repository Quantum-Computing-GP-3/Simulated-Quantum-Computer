import numpy as np

from gate import Gate
from helpers.acts_on import Stu_acts_on, acts_on_all


class General(Gate):

    def __init__(self, matrix, all):
        """
        The matrix and tensor representation of the quantum gate has to be established.

        Parameters
        ----------
        matrix : Complex numpy array
            Stores the matrix representation of the quantum gate.

        Returns
        -------
        None.
        """
        self.matrix = matrix

        # self.size is the number of qubits the gate is designed to act on.
        # Can be obtained by looking at the number of rows in its matrix representation.
        self.size = int(np.round(np.log2(matrix.shape[0])))

        # self.tensor is the tensor representation of the quantum gate, which is needed
        # for the tensor calculations of its action on the quantum register.
        self.tensor = np.reshape(matrix, (2,)*2*self.size)

        self.all = all

    def acts_on(self, Reg_obj, q):
        """
        function to act hadamard
        :param Reg_obj: obj
            Register object
        :param q: list
            qubit(s) to act on
        :return Reg_obj: Updated register
        """
        if self.all:
            return acts_on_all(Reg_obj, self.matrix)
        else:
            return Stu_acts_on(Reg_obj, q, self.matrix, self.size)
