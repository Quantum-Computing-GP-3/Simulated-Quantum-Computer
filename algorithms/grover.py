import sys
import numpy as np
from algorithm import Algorithm
#Stu has to take away this dot for now, if I forget to put it back: soryyyy
from gates.hadamard import Hadamard
from gates.grover_gate import Grover
from gates.oracle import Oracle
from helpers.register import QuantumRegister as QReg
from matplotlib import pyplot as plt



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


    def launch(self,n,marked_list, angle_plot = False):

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
        if angle_plot == True:
            if len(marked_list) != 1:
                raise ValueError("Error: angle plot only works if only one state is being amplified")

        #check that the length of the marked list is less than half the size of the register
        if len(self.marked_list)>=2**(self.n_qbits-1):
            raise TypeError("Error: The number of searching states supplied must be less than half the size of the register")


        # Reg_obj is register object, Reg is Quantum_Register class function
        # define number n of qubits in register
        Reg_obj = QReg(self.n_qbits)

        # act hadamard on all qubits
        H.acts_on(Reg_obj, all=True)

        #errors: IS THIS RIGHT????????
        if (max(self.marked_list) + 1) ** (1 / self.n_qbits) > 2:
            sys.exit("An index given is too large for the register")

        # We now apply the Grover and Oracle gates in order to amplify the required state.
        #the number of Grover iterations is given by the following calculation
        n_iter = int((np.pi / 4 * np.sqrt(2 ** self.n_qbits))/len(self.marked_list))
        
        if n_iter == 0:
            print("n = 0 so do once")
            n_iter = 1


        #only if user wants angle_plot
        #firt angle for angle_plot
        if angle_plot == True:
            angle_list = []
            coeff = Reg_obj.Reg[self.marked_list[0]]
            angle = self.angle_vector(coeff)
            angle_list.append(angle)

        # do Grover iteration
        for i in range(n_iter):
            O.acts_on(Reg_obj, self.marked_list)
            G.acts_on(Reg_obj)

            #only if user wants angle_plot
            if angle_plot == True:
                #take coefficient for plot
                coeff = Reg_obj.Reg[self.marked_list[0]]
                angle = self.angle_vector(coeff)
                angle_list.append(angle)

        print("The resulting quantum register should have a certain state (or states) amplified:")
        print(Reg_obj.Reg)
        for i in range(len(self.marked_list)):
            print(Reg_obj.Reg[self.marked_list[i]])


        self.barchart(Reg_obj)

        # only if user wants angle_plot
        if angle_plot == True:
            print("here")
            self.plot_angles(angle_list)


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


    def plot_angles(self, angle_list):
        #define the max and min x values for each line
        x_lines = np.zeros((len(angle_list), 2))
        x_lines[:,1] = np.sin(angle_list)

        # define the max and min y values for each line
        y_lines = np.zeros((len(angle_list), 2))
        y_lines[:,1] = np.cos(angle_list)

        #create colour gradient
        colors = np.linspace(0.8,0,len(angle_list), dtype = "str")

        #plot lines
        plt.xlabel("Register component perpendicular to Amplified State ")
        plt.ylabel("Register component parallel to amplified State ")
        plt.title("Evolution of amplified state | Grover's")

        for i in range(len(angle_list)):

            if len(angle_list) > 6 and len(angle_list) <= 9:
                if i/2 == i//2:
                    plt.plot(x_lines[i,:],y_lines[i,:], color = colors[i], label = "iteration  "+str(i))
                else:
                    plt.plot(x_lines[i, :], y_lines[i, :], color=colors[i])
            elif len(angle_list) > 9:
                if i/3 == i//3:
                    plt.plot(x_lines[i,:],y_lines[i,:], color = colors[i], label = "iteration  "+str(i))
                else:
                    plt.plot(x_lines[i, :], y_lines[i, :], color=colors[i])
            else:
                plt.plot(x_lines[i, :], y_lines[i, :], color=colors[i], label="iteration  " + str(i))

        plt.legend(loc = 1)
        plt.gca().set_aspect('equal')#


        plt.show()






    def barchart(self, Reg_obj):

        Reals = np.real(Reg_obj.Reg)
        Reals = np.abs(Reals)

        maximum = np.max(Reals)
        arg_max = np.argwhere(np.isclose(Reals, maximum))
        max_arr = Reals[arg_max]
        strings = []

        for n in range(0, len(arg_max[:, 0])):
            #append index
            strings.append(str(arg_max[n, 0]))
            #or append binary value
            #strings.append(str(bin(arg_max[n, 0])))
            #print(strings)


        """
        # find binary string values
        for s in range(len(strings)):
            string = strings[s].lstrip("0")
            string = string.lstrip("b")
            strings[s] = string
        """


        strings.append("all others")
        minimum = np.min(Reals)
        full_arr = np.append(max_arr, minimum)

        plt.title("Quantum Register after Grover's Algorithm")
        plt.xlabel("Basis states in decimal representation")
        plt.ylabel("Probability of measuring basis state")
        plt.bar(strings, np.real(full_arr ** 2), color="teal")
        plt.show()







def main(n,marked_list,angle_plot=False):

    grover = Grover(n, marked_list)
    grover.launch(n,marked_list, angle_plot = angle_plot)


if __name__ == "__main__":
    #main(6, [0],angle_plot=True)
    main(8, [0], angle_plot = True)
    #Reg_1 = QReg(6,increasing_integers= True)#weights = np.array([[0,1,2],[1,2,3]]))#increasing_integers = True)



