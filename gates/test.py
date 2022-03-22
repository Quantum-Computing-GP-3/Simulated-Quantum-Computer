<<<<<<< Updated upstream
import numpy as np
import math

import sys
sys.path.append ('C:/Users/mabon/Documents/GitHub/Simulated-Quantum-Computer/register')
from hadamard import Hadamard
from register import QuantumRegister as QReg

#from pauli_X import Pauli_X as X



H = Hadamard()




Reg_obj = QReg(2)
test_q = [1]
all = None
print(Reg_obj.Reg)

H.acts_on(Reg_obj,test_q,all)
print("H",Reg_obj.Reg)
=======


>>>>>>> Stashed changes
