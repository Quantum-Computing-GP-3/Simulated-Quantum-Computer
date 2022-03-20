from algorithm import Algorithm
import sys
sys.path.append ('C:/Users/admin/Documents/GitHub/Simulated-Quantum-Computer/gates')
sys.path.append ('C:/Users/admin/Documents/GitHub/Simulated-Quantum-Computer/helpers')
sys.path.append ('C:/Users/admin/Documents/GitHub/Simulated-Quantum-Computer/register')
from hadamard import Hadamard
from grover_gate import Grover
from oracle import Oracle
from cnot import CNOT
from toffoli import Toffoli
from pauli_X import Pauli_X as X
from pauli_Z import Pauli_Z as Z


from register import QuantumRegister as QReg
import numpy as np

H = Hadamard()
CNOT = CNOT()
T = Toffoli()
X = X()
Z = Z()



class QECorrection(Algorithm):
    """
    Runs Shor's algorithm
    """

    def launch(self, n, q, alpha, beta, pbit=0., psign=0.):
        """
        I DONT THINK THIS WORKS YET
        this runs the Shor code for one qubit in state Psi
        this is qubit 0
        it needs 8 ancilla states
        """
        Reg_obj = QReg(n, q)
        Reg_obj.Reg[0] = alpha
        Reg_obj.Reg[1] = beta
        
        Reg_obj.norm() #necessary normalization since alpha and beta can be chosen arbitrarily by user
        #print('regob',Reg_obj.Reg)
        print('alpha', Reg_obj.Reg[0], 'beta', Reg_obj.Reg[1])

        # we always act with C(NOT) and T on the same configuration of qubits,
        # therefore those actions can be carried out in loops over the following lists
        C_list1 = [[0, 1], [3, 4], [6, 7]]
        C_list2 = [[0, 2], [3, 5], [6, 8]]
        T_list = [[1, 2, 0], [4, 5, 3], [7, 8, 6]]

        CNOT.acts_on(Reg_obj, [0, 3])
        CNOT.acts_on(Reg_obj, [0, 6])
        H.acts_on(Reg_obj, [0, 3, 6])

        for i in range(3):
            CNOT.acts_on(Reg_obj, C_list1[i])

        for i in range(3):
            CNOT.acts_on(Reg_obj, C_list2[i])

        Reg_obj.error_channel([0], pbit, psign)
        for i in range(3):
            CNOT.acts_on(Reg_obj, C_list1[i])

        for i in range(3):
            CNOT.acts_on(Reg_obj, C_list2[i])

        for i in range(3):
            T.acts_on(Reg_obj, T_list[i])

        H.acts_on(Reg_obj, [0, 3, 6])
        CNOT.acts_on(Reg_obj, [0, 3])
        CNOT.acts_on(Reg_obj, [0, 6])
        T.acts_on(Reg_obj, [3, 6, 0])

        # the new register looks different than the initial one
        # but alpha and beta stayed the same!!!:
        alpha_new = 0
        beta_new = 0
        print(Reg_obj.Reg)
        for i in range(Reg_obj.N):
            if i % 2 == 0:  # 0-coefficients
                alpha_new += Reg_obj.Reg[i]
            else:  # 1-coefficients
                beta_new += Reg_obj.Reg[i]
        print('alphanew',alpha_new,'betanew', beta_new)



def __main__(n,q, alpha, beta,pbit=0., psign=0. ):
    shor = QECorrection()
    shor.launch(n,q, alpha, beta,pbit, psign)


if __name__ == "__main__":
    __main__(9,0, 0.2,0.7, 0.,0.)

