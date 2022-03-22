from algorithm import Algorithm
<<<<<<< Updated upstream
=======
from gates.hadamard import Hadamard
from gates.grover import Grover
from gates.oracle import Oracle
from gates.cnot import CNOT


from helpers.register import QuantumRegister as QReg
import numpy as np


CNOT = CNOT()

>>>>>>> Stashed changes


class Shor(Algorithm):
    """
    Runs Shor's algorithm
    """

    def launch(self, n, q, pbit=0., psign=0.):
        """
        I DONT THINK THIS WORKS YET
        this runs the Shor code for one qubit in state Psi
        this is qubit 0
        it needs 8 ancilla states
        """
        Reg_obj = QReg(n)
        # we always act with C(NOT) and T on the same configuration of qubits,
        # therefore that way of writing it is easier
        C_list1 = [[0, 1], [3, 4], [6, 7]]
        C_list2 = [[0, 2], [3, 5], [6, 8]]
        T_list = [[1, 2, 0], [4, 5, 3], [7, 8, 6]]

        # reg = Reg_obj.Reg
        CNOT.acts_on(Reg_obj, [0, 3])
        CNOT.acts_on(Reg_obj, [0, 6])
        CNOT.acts_on(Reg_obj, [0, 3, 6])

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
        # but the alpha and beta stayed the same!!!

        alpha_new = 0
        beta_new = 0
        for i in range(Reg_obj.N):
            if i % 2 == 0:  # 0 coefficients
                alpha_new += Reg_obj.Reg[i]
            else:  # 1 coefficients
                beta_new += Reg_obj.Reg[i]
        print(alpha_new, beta_new)


def main(n,q):
    shor = Shor()
    shor.launch(n,q)


if __name__ == "__main__":
    main(9,0)
