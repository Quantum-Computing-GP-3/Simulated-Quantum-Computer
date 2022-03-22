import numpy as np
from .gate import Gate


class Grover(Gate):
    
    def acts_on(self, Reg_obj):
        """
        function to act grovers operator thingy
        :param Reg_obj: obj
            Register object
        """


        #no error check yet
        
        n = Reg_obj.n #number of qubits
        N = Reg_obj.N #length of register


        diag = 2/N-1 #diagonal entries of grover matrix
        rest = 2/N   #entries on non-diagonals of grover matrix

        reg_old = Reg_obj.Reg
        reg_new = np.zeros(N, dtype = "complex") #we don't necessarily need this to be a register object; an array does the work as well
        
        #act the 'matrix' on the statevectorregister
        for i in range(N):
            for j in range(N):
                if i==j:
                    reg_new[i] += diag * reg_old[j]
                else:
                    reg_new[i] += rest * reg_old[j]


        #the following is for the iteration comparison
        #print('iteration grovergate', max(reg_new)**2)

        Reg_obj.Reg = reg_new #update register state vector

