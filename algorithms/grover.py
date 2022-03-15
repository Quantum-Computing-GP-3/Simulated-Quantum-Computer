from algorithm import Algorithm
<<<<<<< Updated upstream
=======
from gates.hadamard import Hadamard
from gates.grover import Grover
from gates.oracle import Oracle
from helpers.register import QuantumRegister as QReg
import numpy as np
>>>>>>> Stashed changes

H = Hadamard()
G = Grover()
O = Oracle()

class Grover(Algorithm):
    """
    Runs Grover's algorithm
    """

    def __init__(self, n_qbits, state_list):
        self.n_qbits = n_qbits
        self.state_list = state_list

    def launch(self,n,state_list):
        """
        Triggers the start of Grover's algorithm
        """
<<<<<<< Updated upstream
        print("WOo Grover worked")
        print("Hi")
=======
>>>>>>> Stashed changes

        """
                Function to act grover using Qgate objects, a QReg object and a given state
                :param Reg_obj: QReg object
                    register object
                :param state: string of 1&0's etc "1100"
                    state for oracle
                :return:
                """

        # Reg_obj is register object, Reg is Quantum_Register class function
        # define number of qubits in register

        Reg_obj = QReg(n)

        """
        #make the state into a list of 1's and 0's
        state_list = list(state)
        for i in range(len(state_list)):
            state_list[i] = int(state_list[i])
        if len(state_list) != n:
            sys.exit("the state you have supplied is for the wrong number of qubits")
        """

        # act hadamard on all qubits
        H.acts_on(Reg_obj, all=True)

        if (np.max(state_list) + 1) ** (1 / n) > 2:
            sys.exit("An index given is too large for the register")

        # We now apply the Grover and Oracle gates in order to amplify the required state.
        n_iter = int((np.pi / 4 * np.sqrt(2 ** n))/len(state_list))
        if n_iter == 0:
            print("n = 0 so do once")
            n_iter = 1
        print(n_iter)
        for i in range(n_iter):
            O.acts_on(Reg_obj, state_list)
            G.acts_on(Reg_obj)

        print("The resulting quantum register should have a certain state (or states) amplified:")
        print(Reg_obj.Reg)
        for i in range(len(state_list)):
            print(Reg_obj.Reg[state_list[i]])








def main(n,state_list):

    grover = Grover(n,state_list)
    grover.launch(n,state_list)


if __name__ == "__main__":
    main(3,[0,1,2,3,4])
