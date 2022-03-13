import numpy as np
import sys
from ListQuantumGates import H, CNOT, O, G,R, T
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
            "Shor": self.act_Shor
        }

        # check if gate in dict
        if algorithm not in act_func_dict:
            sys.exit("You must specify a correct name of a supported algorithm")

        #label may be useful when we have multiple algorithms
        self.label = algorithm

        #specify what function from dict to use when user does QAlg.act
        self.act = act_func_dict[self.label]





    def act_Grover(self, Reg_obj, state_list):
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

        """
        #make the state into a list of 1's and 0's
        state_list = list(state)
        for i in range(len(state_list)):
            state_list[i] = int(state_list[i])
        if len(state_list) != n:
            sys.exit("the state you have supplied is for the wrong number of qubits")

        """

        #act hadamard on all qubits
        H.act(Reg_obj, all = True)


        if (np.max(state_list)+1)**(1/n)>2:
            sys.exit("An index given is too large for the register")

        # We now apply the Grover and Oracle gates in order to amplify the required state.
        n_iter = int(np.pi / 4 * np.sqrt(2 ** n))
        for i in range(n_iter):
            O.act(Reg_obj, state_list)
            G.act(Reg_obj)

        print("The resulting quantum register should have a certain state (or states) amplified:")
        print(Reg_obj.Reg)
        print(Reg_obj.Reg[state_list[0]])


    def act_Grover_cosi(self,Reg_obj, state_list):
        n = Reg_obj.n
        N = Reg_obj.N
        # desired length of register

        # which state is the one we are looking for, as given in index form (e.g. 6 = 0110)
        # using multiple states is easy: we need to have a list anyways and it can be rather long


        number_right_answers = len(state_list)
        if (np.max(state_list)+1)**(1/n)>2:
            sys.exit("An index given is too large for the register")



        state_list_as_Reg_obj = np.zeros(N)
        for i in range(number_right_answers):
            state_list_as_Reg_obj[state_list[i]] = 1

        H.act(Reg_obj, all = True)
        initial_state = np.copy(Reg_obj.Reg)


        n_iter = int(np.pi / 4 * np.sqrt(N) / number_right_answers)


        for _ in range(n_iter):
            R.act(Reg_obj, state_list_as_Reg_obj, oracle = True)  # minus that!!!
            R.act(Reg_obj, initial_state)

        #print(Reg_obj.Reg)

        #print([Reg[i] for i in state_list])

    def error_channel(self, Reg_obj, q, pbit=0., psign=0.):
        # YES THIS NEEDS PBIT AND PSIGN
        # MAYBE A **KWARGS ARGUMENT WOULD BE BETTER FOR THE QUANTUM GATE CLASS
        """
        error channel is the channel that corrupts the single qubit with certain probability
        pbit: prob of bitflip
        psign: prob of signflip
        it acts on a qubit q. for the easiest case of just shor's algorithm there is only one
        possible qubit to act on and that is qbit 0
        since it acts using X and Z, it is a Quantum
        """



        # now decide randomly if qbit will be corrupted
        # this depends on the corruption probability
        # with this one can tune the noise up or down
        corruptionbit = np.random.random()
        corruptionsign = np.random.random()

        if corruptionbit < pbit:
            print('bitcorruption')
            X.act(Reg_obj, q)
        else:
            print('no bitcorruption')

        if corruptionsign < psign:
            print('signcorruption')
            Z.act(Reg_obj, q)
        else:
            print('no signcorruption')


    # IMPORTANT QUESTION: IF I DO H.ACT (REG) WILL REG BE CHANGED OR DO I HAVE TO DO REG = H.ACT(REG)
    # YES I DO NOT NEED TO FEED IN A WHOLE STATEVECTOR
    # I CAN DO SO IF IT IS MORE COMFORTABLE THOUGH
    # for Shor the following can also be done INSIDE the algorithm
    """
        alpha, beta can be chosen freely (that is the state we have), alpha 0 + beta 1
        n = 9
        N = 2**n
        Reg = QReg(n)
        Reg[0] = alpha 
        Reg[1] = beta 
        Reg = Reg.norm
    """

    def act_Shor(self, Reg_obj, pbit=0., psign=0.):
        """
        I DONT THINK THIS WORKS YET
        this runs the Shor code for one qubit in state Psi
        this is qubit 0
        it needs 8 ancilla states
        """

        # we always act with C(NOT) and T on the same configuration of qubits,
        # therefore that way of writing it is easier
        C_list1 = [[0, 1], [3, 4], [6, 7]]
        C_list2 = [[0, 2], [3, 5], [6, 8]]
        T_list = [[1, 2, 0], [4, 5, 3], [7, 8, 6]]

        #reg = Reg_obj.Reg
        CNOT.act(Reg_obj, [0, 3])
        CNOT.act(Reg_obj, [0, 6])
        CNOT.act(Reg_obj, [0, 3, 6])

        for i in range(3):
            CNOT.act(Reg_obj, C_list1[i])

        for i in range(3):
            CNOT.act(Reg_obj, C_list2[i])

        self.error_channel(Reg_obj, [0], pbit, psign)

        for i in range(3):
            CNOT.act(Reg_obj, C_list1[i])

        for i in range(3):
            CNOT.act(Reg_obj, C_list2[i])

        for i in range(3):
            T.act(Reg_obj, T_list[i])

        H.act(Reg_obj, [0, 3, 6])
        CNOT.act(Reg_obj, [0, 3])
        CNOT.act(Reg_obj, [0, 6])
        T.act(Reg_obj, [3, 6, 0])

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



