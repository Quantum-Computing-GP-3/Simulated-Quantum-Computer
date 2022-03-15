import numpy as np
import sys
from .ListQuantumGates import H, CNOT, X,Z,R
from .Quantum_Gate import get_state_index



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

    



    def act_Grover(self, Reg_obj, state_list):

        #input
        """
        input_state_list = input('please enter the positions of the states that the oracle function has marked')
        input_starting_Reg_obj = input ('if you wish, enter an array that is the starting state')

        state_list = input_state_list #howww?
        Reg_obj = input_starting_Reg_obj

        #about state_list
        number_right_answers = len(state_list)
        n_required = len(bin(max(state_list)))-2       
        N_required = 2**n_required

        state_list_as_Reg_obj = np.zeros(N_required)
        for i in range (number_right_answers):
            state_list_as_Reg_obj [state_list[i]] = 1
        #print(state_list_as_Reg_obj)
        

        #errorcatching**********************
            #Reg_obj is array 1d

            #len Reg_obj is 2**m


            #statelist list of state indices within range of Reg_obj
        #for state in state_list:
         #   error
        
        #********************

        if Reg_obj != None:
            n_Reg_input = Reg_obj.n
            if Reg_obj.n < n_required:
                print('error')
            original_state = np.copy(Reg_obj)
            Reg = Reg_obj


        #now do Grover
        if Reg_obj == None:
            #act hadamard on all qubits
            original_state = H.act(np.copy(Reg_obj), all = True)
            Reg = H.act(Reg_obj, all = True)
            """


        number_right_answers = len(state_list)
        n_required = len(bin(max(state_list)))-2       
        N_required = 2**n_required

        state_list_as_Reg_obj = np.zeros(N_required)
        for i in range (number_right_answers):
            state_list_as_Reg_obj [state_list[i]] = 1
        print(state_list_as_Reg_obj)
        



        original_state = H.act(np.copy(Reg_obj), all = True)
        Reg = H.act(Reg_obj, all = True)
            # We now apply the Grover and Oracle gates in order to amplify the required state.
        n_iter = int(np.pi / 4 * np.sqrt(2 ** n)/number_right_answers)
        for _ in range (n_iter):
            Reg = -R.act(Reg, stateasindex = state_list_as_Reg_obj) #minus that!!!
            Reg = R.act(Reg, state = original_state)
            print(Reg)

        return Reg

