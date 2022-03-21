
import sys
sys.path.append ('C:/Users/admin/Documents/GitHub/Simulated-Quantum-Computer/gates')
sys.path.append ('C:/Users/admin/Documents/GitHub/Simulated-Quantum-Computer/helpers')
sys.path.append ('C:/Users/admin/Documents/GitHub/Simulated-Quantum-Computer/register')
from gate import Gate
import copy
from register import QuantumRegister as QReg
from algorithm import Algorithm
from hadamard import Hadamard
from grover_gate import Grover
from oracle import Oracle
from cnot import CNOT
from toffoli import Toffoli
from pauli_X import Pauli_X as X
from pauli_Z import Pauli_Z as Z
import numpy as np
H = Hadamard()
CNOT = CNOT()
T = Toffoli()
X = X()
Z = Z()
import time
import math


class Reflection(Gate):

    #IS THIS NECESSARY????????
    #def __init__(self):
    #self.state = state

    def acts_on(self,Reg_obj_state, Reg_obj_op):
        """
        function to reflect around
        :param Reg_obj_state
            Register Object that the reflection acts on
        :param Reg_obj_op
            Register Object around which to reflect about
        """

        #No error check for this yet!!!!!!!


        n = Reg_obj_op.n 
        N = Reg_obj_op.N
        
        #normalizations
        Reg_obj_op.norm()
        Reg_obj_state.norm()

        #in order to calculate all entries, one needs to save the original register state separately
        reg_original = copy.deepcopy(Reg_obj_state)

        
        for i in range(N):
            regentryi = 0
            for j in range(N):
                regentryi += Reg_obj_op.Reg[i]*Reg_obj_op.Reg[j]*reg_original.Reg[j]
                
            Reg_obj_state.Reg[i] = regentryi    
        

        #reflection
        Reg_obj_state.Reg = 2*Reg_obj_state.Reg - reg_original.Reg
        Reg_obj_state.norm()
        
        #print('iteration reflection', max(Reg_obj_state.Reg)**2)
        #keep the print for the graphs