import numpy as np
import sys
from ListQuantumGates import H, CNOT, O, G
from Quantum_Gate import get_state_index





#import gates!!!!!!!!!!!!!

class Quantum_Algorithm(object):
    def __init__(self, algorithm):
        """
        expects the name of an algorithm "Grover" for example

        :param algorithm: Str
            name of algorithm

        """

        act_func_dict = {
            "Grover": self.act_Grover,
        }

        # check if gate in dict
        if algorithm not in act_func_dict:
            sys.exit("You must specify a correct name of a supported algorithm")

        #label may be useful when we have multiple algorithms
        self.label = algorithm

        #specify what function from dict to use when user does QAlg.act
        self.act = act_func_dict[self.label]





    def act_Grover(self, Reg_obj, state):
        """
        Function to act grover using Qgate objects, a QReg object and a given state
        :param Reg_obj: QReg object
            register object
        :param state: string of 1&0's etc "1100"
            state for oracle
        :return:
        """

        #Reg_obj is register object, Reg is Quantum_Register class function
        #define number of qubits in register
        n = Reg_obj.n

        #make the state into a list of 1's and 0's
        state_list = list(state)
        for i in range(len(state_list)):
            state_list[i] = int(state_list[i])
        if len(state_list) != n:
            sys.exit("the state you have supplied is for the wrong number of qubits")


        #act hadamard on all qubits
        H.act(Reg_obj, all = True)


        # We now apply the Grover and Oracle gates in order to amplify the required state.
        n_iter = int(np.pi / 4 * np.sqrt(2 ** n))
        for i in range(n_iter):
            O.act(Reg_obj, state = state)
            G.act(Reg_obj)

        print("The resulting quantum register should have a certain state amplified:")
        print("In this case the amplified state is " + state)


        #uses get_state_index from Quantum_Gate class to get the index and print
        print(Reg_obj.Reg[get_state_index(state_list,n)])




