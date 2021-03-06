import numpy as np
from gates.pauli_X import Pauli_X as X
from gates.pauli_Z import Pauli_Z as Z
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

    # now decide randomly if qbit will be corrupted
    # this depends on the corruption probability
    # with this one can tune the noise up or down
    corruptionbit = np.random.random()
    corruptionsign = np.random.random()

    if corruptionsign < psign:
        print('The sign has been corrupted')
        print()
        Z.acts_on(Reg_obj, q)
    else:
        print('No sign corruption')
        print()

    if corruptionbit < pbit:
        print('The bit has been corrupted')
        print()
        X.acts_on(Reg_obj, q)
    else:
        print('No bit corruption')
        print()

    print("The new corrupted state is:")
    print(Reg_obj.Reg)
    print()
