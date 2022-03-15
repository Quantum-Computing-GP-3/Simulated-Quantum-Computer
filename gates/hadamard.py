import numpy as np

from .gate import Gate
from helpers.acts_on import Stu_acts_on, acts_on_all


class Hadamard(Gate):

    def __init__(self, all=False):
        """
        Initialise Hadamard gate
        """
        self.matrix = 1/np.sqrt(2)*np.array([[1, 1],
                                             [1, -1]])
        self.size = int(np.round(np.log2(self.matrix.shape[0])))

        self.tensor = np.reshape(self.matrix, (2, 2))

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
