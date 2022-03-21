import sys
import numpy as np
from algorithm import Algorithm
#Stu has to take away this dot for now, if I forget to put it back: soryyyy
from gates.hadamard import Hadamard
from gates.grover_gate import Grover
from gates.oracle import Oracle
from helpers.register import QuantumRegister as QReg
import matplotlib.pyplot as plt
H = Hadamard()
G = Grover()
O = Oracle()

class Grover(Algorithm):
    """
    Runs Grover's algorithm
    """

    def __init__(self, n_qbits, marked_list):

        self.n_qbits = n_qbits
        self.marked_list = marked_list

    def launch(self,n,marked_list, animation = False):
        """
        Triggers the start of Grover's algorithm
        Function to act grover using Qgate objects, a QReg object and a given state
            :param Reg_obj: QReg object
                register object
            :param state: string of 1&0's etc "1100"
                state for oracle
            :return:
        """
        #error checks ****************
        if animation == True:
            if len(marked_list) != 1:
                raise ValueError("Error: animation only works if only one state is being amplified")

        if len(marked_list)>=2**(self.n_qbits-1):
            raise TypeError("Error: The number of searching states supplied must be less than half the size of the register")


        # Reg_obj is register object, Reg is Quantum_Register class function
        # define number n of qubits in register
        Reg_obj = QReg(n)

        # act hadamard on all qubits
        H.acts_on(Reg_obj, all=True)

        #errors: IS THIS RIGHT????????
        if (max(marked_list) + 1) ** (1 / n) > 2:
            sys.exit("An index given is too large for the register")

        # We now apply the Grover and Oracle gates in order to amplify the required state.
        #the number of Grover iterations is given by the following calculation
        n_iter = int((np.pi / 4 * np.sqrt(2 ** n))/len(marked_list))
        
        if n_iter == 0:
            print("n = 0 so do once")
            n_iter = 1


        #only if user wants animation
        #firt angle for animation
        if animation == True:
            angle_list = []
            coeff = Reg_obj.Reg[marked_list[0]]
            angle = self.angle_vector(coeff)
            angle_list.append(angle)

        # do Grover iteration
        for i in range(n_iter):
            O.acts_on(Reg_obj, marked_list)
            G.acts_on(Reg_obj)

            #only if user wants animation
            if animation == True:
                #take coefficient for plot
                coeff = Reg_obj.Reg[marked_list[0]]
                angle = self.angle_vector(coeff)
                angle_list.append(angle)

        print("The resulting quantum register should have a certain state (or states) amplified:")
        print(Reg_obj.Reg)
        for i in range(len(marked_list)):
            print(Reg_obj.Reg[marked_list[i]])

        print("hello")
        #print(np.degrees(angle_list))
        self.barchart(Reg_obj)
        print("hi")

    def angle_vector(self, array_coefficients):
        """
        Calculates the angle between the quantum register and the basis state we wish to
        amplify. After every iteration of Grover's algorithm, this angle should eventually
        be very close to 0.
        Parameters
        ----------
        array_coefficients : Complex Numpy Array
            List of coefficients of the basis state we are interested in.
        Returns
        -------
        array_angles : Numpy Array

            Contains angle between quantum register and the basis state we wish to amplify.
        """
        array_angles = np.arccos(np.real(array_coefficients))

        return array_angles

    def barchart(self, Reg_obj):

        Reals = np.real(Reg_obj.Reg)
        Reals = np.abs(Reals)

        maximum = np.max(Reals)
        arg_max = np.argwhere(np.isclose(Reals, maximum))
        max_arr = Reals[arg_max]
        strings = []

        for n in range(0, len(arg_max[:, 0])):
            strings.append(str(bin(arg_max[n, 0])))

        # find binary string values
        for s in range(len(strings)):
            string = strings[s].lstrip("0")
            string = string.lstrip("b")
            strings[s] = string

        strings.append("all others")
        minimum = np.min(Reals)
        full_arr = np.append(max_arr, minimum)

        plt.title("Amplified states")
        plt.xlabel("Binary state")
        plt.ylabel("Probability")
        plt.bar(strings, np.real(full_arr ** 2), color="teal")
        plt.show()







def main(n,marked_list,animation=False):

    grover = Grover(n, marked_list)
    grover.launch(n,marked_list, animation = animation)


if __name__ == "__main__":
    #main(5, [0],animation=True)
    main(5, [0,1,2])
    """
    print('5,    [0,3] \n')
    main(5,[0,3])
    print('6,    [2] \n')
    main(6,[2])
    print('4,    [1,2,3] \n')
    main(4,[1,2,3])
    print('5,    [0,30] \n')
    main(5,[0, 30])
    print('5,    [10] \n')

    main(5,[10])
    """


