
import sys
sys.path.append ('C:/Users/admin/Documents/GitHub/Simulated-Quantum-Computer/gates')
from pauli_X import Pauli_X as X
from pauli_Z import Pauli_Z as Z
import numpy as np
X = X()
Z = Z()

def error_channel(Reg_obj, q, pbit=0., psign=0.):

    """
    error channel is the channel that corrupts the single qubit with certain probability
    pbit: prob of bitflip
    psign: prob of signflip
    it acts on a qubit q. for the easiest case of just shor's algorithm there is only one
    possible qubit to act on and that is qbit 0
    """

    # errors*************
    """
    #q index needs to be within the register size
    if q -1 > self.n:
        raise IndexError ('Error: the qubit you want to act on with error_channel exceeds the Register size')

    #type of q is int (qbit number from 0 to n-1)
    if isinstance(q, (int)) == False:
        raise TypeError('Error: error_channel expects list of integer qubit arguments')
    """
    # *******************

    # now decide randomly if qbit will be corrupted
    # this depends on the corruption probability
    # with this one can tune the noise up or down
    corruptionbit = np.random.random()
    corruptionsign = np.random.random()

    if corruptionsign < psign:
        print('signcorruption')
        Z.acts_on(Reg_obj,  q)
    else:
        print('no signcorruption')

    if corruptionbit < pbit:
        print('bitcorruption')
        X.acts_on(Reg_obj, q)
    else:
        print('no bitcorruption')




