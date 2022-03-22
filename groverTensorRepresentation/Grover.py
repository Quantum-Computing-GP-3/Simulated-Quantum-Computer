# -*- coding: utf-8 -*-
"""
Given the appropriate quantum gates, it applies Grover's algorithm to a quantum
register. This is the file to run.

"""
# From ListQuantumGates we import the number of qubits of the quantum register (n)
# and the needed quantum gates.
from .ListQuantumGates import  get_Hadamard, get_O, get_G
import numpy as np
import matplotlib.pyplot as plt

def launch(n, marked_state):
    # First step is to initialise a quantum register of n qubits to the 0th state.
    reg = np.zeros((2,)*n, dtype = complex) 
    reg[(0,)*n] = 1 
    
    # We then use Hadamard gates to get the quantum register into an equal superposition
    # of all states.
    for i in range(n):
       reg = Hadamard.acts_on([i], reg)

    # At each iteration of Grover's algorithm, we wish to save the coefficient of the 
    # basis state with the highest amplitude.
    coefficient_list = []

    # We now apply the Grover and Oracle gates in order to amplify the needed state.
    number_iterations = int( np.pi / 4 * np.sqrt(2**n) )
    
    for i in range(number_iterations):
        reg = O.acts_on([j for j in range(n)], reg)
        reg = G.acts_on([j for j in range(n)], reg)
        
        ind_amplified = np.unravel_index(np.argmax(reg, axis = None), reg.shape)
        coefficient_list.append(reg[ind_amplified])
    
    # We now search for the index of the amplified state.
    ind = np.unravel_index(np.argmax(reg, axis = None), reg.shape)
    
    print(f"\nIn this case the amplified state is {ind}:")
    print(f"Probability of measuring it is: {abs(reg[ind])}")
    
    # We now create a plot of the situation
    plt.bar([f"{ind}", "all other states"], [abs(reg[ind])**2, 1 - abs(reg[ind])**2], color = 'teal')
    plt.ylabel("Probability of measuring basis state")
    plt.title("Quantum Register after Grover's Algorithm")
    plt.show()
    
    # We also create plot of the quantum register approaching the state we wish to amplify.
    array_angles = angle_vector(np.asarray(coefficient_list))
    plot_angles(array_angles)
    
    
def angle_vector(array_coefficients):
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
    
def plot_angles(array_angles):
    """
    Plots the component of the quantum register in the direction of the 
    amplified basis state. 
    
    Parameters
    ----------
    array_angles : Numpy Array
        After every iteration of Grover's the Euclidean angle between the quantum register
        and the basis state that we want to amplify is stored.
    
    Returns
    -------
    None.
    """
    #define the max and min x values for each line
    x_lines = np.zeros((len(array_angles), 2))
    x_lines[:,1] = np.sin(array_angles)
    
    # define the max and min y values for each line
    y_lines = np.zeros((len(array_angles), 2))
    y_lines[:,1] = np.cos(array_angles)
    
    #create colour gradient
    colors = np.linspace(0.8,0,len(array_angles), dtype = "str")
    
    #plot lines
    plt.xlabel("Register component perpendicular to amplified state ")
    plt.ylabel("Register component parallel to amplified atate ")
    plt.title("Evolution of Amplified State | Grover's")
    
    for i in range(len(array_angles)):
    
        if len(array_angles) > 6 and len(array_angles) <= 9:
            if i/2 == i//2:
                plt.plot(x_lines[i,:],y_lines[i,:], color = colors[i], label = "iteration  "+str(i))
            else:
                plt.plot(x_lines[i, :], y_lines[i, :], color=colors[i])
        elif len(array_angles) > 9:
            if i/3 == i//3:
                plt.plot(x_lines[i,:],y_lines[i,:], color = colors[i], label = "iteration  "+str(i))
            else:
                plt.plot(x_lines[i, :], y_lines[i, :], color=colors[i])
        else:
            plt.plot(x_lines[i, :], y_lines[i, :], color=colors[i], label="iteration  " + str(i))
    
    plt.legend(loc = 1)
    plt.axis('square')
    
    plt.show()
            

    
# Execute main method, but only when directly invoked
#if __name__ == "__main__":
#    main()