
from algorithm import Algorithm
import sys
sys.path.append ('C:/Users/stuar/OneDrive - University of Edinburgh/Documents/GitHub/Simulated-Quantum-Computer/gates')
sys.path.append ('C:/Users/stuar/OneDrive - University of Edinburgh/Documents/GitHub/Simulated-Quantum-Computer/helpers')
sys.path.append ('C:/Users/stuar/OneDrive - University of Edinburgh/Documents/GitHub/Simulated-Quantum-Computer/register')


from hadamard import Hadamard
from cnot import CNOT
from toffoli import Toffoli
from pauli_X import Pauli_X as X
from pauli_Z import Pauli_Z as Z
from register import QuantumRegister as QReg
from error_channel import error_channel


H = Hadamard()
CNOT = CNOT()
T = Toffoli()
X = X()
Z = Z()


class QECorrection(Algorithm):
    """
    Runs Quantum Error Correction Algorithm
    """

    def launch(self, alpha, beta, pbit=0., psign=0.):
        """
        :param alpha: real number
            coefficient for 0-state
        :param beta: real number
            coefficient for 1-state
        :param pbit: real number between 0 and 1
            probability of bitflip
        :param psign: real number between 0 and 1
            probability of signflip
        runs the Shor code for error correction for one qubit in state Psi = alpha * ket(0)+ beta * ket(1)
        the qubit in state Psi is qubit 0
        the errorchannel acts on this qubit
        in order to reverse effect of errorchannel, one needs 8 ancilla states
        """
        Reg_obj = QReg(9)
        Reg_obj.Reg[0] = alpha
        Reg_obj.Reg[1] = beta

        Reg_obj.norm()  # necessary normalization since alpha and beta can be chosen arbitrarily by user

        print('alpha', Reg_obj.Reg[0], 'beta', Reg_obj.Reg[1])

        # we always act with C(NOT) and T on the same configuration of qubits,
        # therefore those actions can be carried out in loops over the following lists
        C_list1 = [[0, 1], [3, 4], [6, 7]]
        C_list2 = [[0, 2], [3, 5], [6, 8]]
        T_list = [[1, 2, 0], [4, 5, 3], [7, 8, 6]]

        # now we follow the quantum error correction protocol
        CNOT.acts_on(Reg_obj, [0, 3])
        CNOT.acts_on(Reg_obj, [0, 6])
        H.acts_on(Reg_obj, [0, 3, 6])

        for i in range(3):
            CNOT.acts_on(Reg_obj, C_list1[i])

        for i in range(3):
            CNOT.acts_on(Reg_obj, C_list2[i])

        # error channel corrupts bit and sign with a probability given by pbit, psign
        error_channel(Reg_obj,[0], pbit, psign)

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
        for i in range(Reg_obj.N):
            if i % 2 == 0:  # 0-coefficients
                alpha_new += Reg_obj.Reg[i]
            else:  # 1-coefficients
                beta_new += Reg_obj.Reg[i]
        print('alphanew', alpha_new, 'betanew', beta_new)


def __main__(alpha, beta, pbit=0., psign=0.):
    shor = QECorrection()
    shor.launch(alpha, beta, pbit, psign)


if __name__ == "__main__":
    # alpha, beta do not need to be normalized as input
    __main__(0.2, 0.7, 1, 1)





