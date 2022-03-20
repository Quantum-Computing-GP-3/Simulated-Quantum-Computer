import numpy as np
from gate import Gate


class Grover(Gate):
    """
    def acts_on(self, Reg_obj):

        function to act grovers operator thingy
        :param Reg_obj: obj
            Register object
        :param q: list
            qubit(s) to act on
        :return Reg_obj: Updated register

        n = Reg_obj.n
        N = 2**n
        matrix_G = np.ones((N, N)) * 2 / N

        for i in range(N):
            matrix_G[i, i] -= 1

        Reg_obj.Reg = np.matmul(matrix_G, Reg_obj.Reg)
        Reg_obj.vector_notation()
        return Reg_obj
    """
    def acts_on(self, Reg_obj):
        """
        function to act grovers operator thingy
        :param Reg_obj: obj
            Register object
        """

        
        n = Reg_obj.n
        N = Reg_obj.N

        diag = 2/N-1
        rest = 2/N

        reg_old = Reg_obj.Reg
        #reg_new = np.zeros(N)
        reg_new =[0]*N

        for i in range(N):
            for j in range(N):
                if i==j:
                    reg_new[i] += diag * reg_old[j]
                else:
                    reg_new[i] += rest * reg_old[j]

        Reg_obj.Reg = reg_new
