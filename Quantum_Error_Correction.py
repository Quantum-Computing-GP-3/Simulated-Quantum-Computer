import numpy as np
from .ListQuantumGates import H, CNOT, O, G,X,Z, TOFFOLI
from .Quantum_Gate import get_state_index



def error_channel (self, Reg_obj, q, pbit = 0., psign = 0.):
    #YES THIS NEEDS PBIT AND PSIGN
    #MAYBE A **KWARGS ARGUMENT WOULD BE BETTER FOR THE QUANTUM GATE CLASS
    """
    error channel is the channel that corrupts the single qubit with certain probability
    pbit: prob of bitflip
    psign: prob of signflip
    it acts on a qubit q. for the easiest case of just shor's algorithm there is only one
    possible qubit to act on and that is qbit 0
    since it acts using X and Z, it is a Quantum 
    """

    reg = Reg_obj.Reg

    #now decide randomly if qbit will be corrupted
    #this depends on the corruption probability
    #with this one can tune the noise up or down 
    corruptionbit = np.random.random()
    corruptionsign = np.random.random()

    if corruptionbit < pbit:
        print('bitcorruption')
        X.act(reg, q)
    else:
        print('no bitcorruption')

    if corruptionsign < psign:
        print('signcorruption')
        Z.act(Reg_obj, q)
    else: print('no signcorruption')

    Reg_obj.Reg = reg





#IMPORTANT QUESTION: IF I DO H.ACT (REG) WILL REG BE CHANGED OR DO I HAVE TO DO REG = H.ACT(REG)
#YES I DO NOT NEED TO FEED IN A WHOLE STATEVECTOR
#I CAN DO SO IF IT IS MORE COMFORTABLE THOUGH
#for Shor the following can also be done INSIDE the algorithm
"""
    alpha, beta can be chosen freely (that is the state we have), alpha 0 + beta 1

    n = 9
    N = 2**n
    Reg = QReg(n)
    Reg[0] = alpha 
    Reg[1] = beta 
    Reg = Reg.norm
"""
def shor(self, Reg_obj, pbit = 0., psign = 0. ):
    """
    this runs the Shor code for one qubit in state Psi
    this is qubit 0
    it needs 8 ancilla states 
    """

    #we always act with C(NOT) and T on the same configuration of qubits,
    #therefore that way of writing it is easier
    C_list1 = [[0,1], [3,4], [6,7]]
    C_list2 = [[0,2], [3,5], [6,8]]
    T_list = [[1,2,0], [4,5,3], [7,8,6]]

    reg = Reg_obj.Reg
    CNOT.act(reg, [0,3])
    CNOT.act(reg, [0,6])
    CNOT.act(reg, [0,3,6])

    for i in range (3):
        CNOT.act(reg , C_list1[i])

    for i in range (3):
        CNOT.act(reg , C_list2[i])
    
    reg = error_channel(reg, [0], pbit, psign)

    for i in range (3):
        CNOT.act(reg, C_list1[i])

    for i in range (3):
        CNOT.act(reg, C_list2[i])

    for i in range (3):
        TOFFOLI.act(reg, T_list[i])

    H.act(reg , [0,3,6])
    CNOT.act(reg , [0,3])
    CNOT.act(reg, [0,6])
    TOFFOLI.act (reg , [3,6,0])
    Reg_obj.Reg = reg
    

    #the new register looks different than the initial one
    #but the alpha and beta stayed the same!!!

    alpha_new = 0
    beta_new = 0
    for i in range(Reg_obj.N):
        if i%2 == 0:#0 coefficients
            alpha_new += reg[i]
        else: #1 coefficients
            beta_new += reg[i]
    print( alpha_new, beta_new)

