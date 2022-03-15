import numpy as np

from gate import Gate


class Grover(Gate):

    def acts_on(self, Reg_obj, q):
        """
        function to act grovers operator thingy
        :param Reg_obj: obj
            Register object
        :param q: list
            qubit(s) to act on
        :return Reg_obj: Updated register
        """
        n = Reg_obj.n
        N = 2**n
        matrix_G = np.ones((N, N)) * 2 / N

        for i in range(N):
            matrix_G[i, i] -= 1

        Reg_obj.Reg = np.matmul(matrix_G, Reg_obj.Reg)
        Reg_obj.vector_notation()
        return Reg_obj
