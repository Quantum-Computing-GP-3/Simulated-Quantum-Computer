import numpy as np

from gate import Gate
from helpers.cartesian_products import stu_cartesian_product_n_qubits
from helpers.misc import get_state_index


class CNOT(Gate):

    def __init__(self):
        """
        initialise CNOT gate
        can be done algorithimically or by matrices, so matrices could be included.
        Either act_on could be used
        so for now, I specify to use the act_CNOT function to act it

        """
        self.matrix = (np.array([[1, 0, 0, 0],
                                 [0, 1, 0, 0],
                                 [0, 0, 0, 1],
                                 [0, 0, 1, 0]]))

        self.size = int(np.round(np.log2(self.matrix.shape[0])))
        self.tensor = np.reshape(self.matrix, (2, 2, 2, 2))

    def acts_on(self, Reg_obj, q):
        """
        function to act CNOT, remembering that all cnot does is swap the amplitude of qubits
        ALGORITHMIC METHOD, NOT MATRIX METHOD

        :param Reg_obj: obj
            Register object
        :param q: list
            qubit(s) to act on
        :return Reg_obj: Updated register
        """

        # Reg_obj is register object, Reg is QuantumRegister class function,
        # reg is what I will call the tensor register in this function
        reg = Reg_obj.Reg
        n = Reg_obj.n

        reg_new = np.zeros_like(reg)

        c = q[0]
        t = q[1]

        # array of cartesian products
        carts = stu_cartesian_product_n_qubits(n)

        # loop through cartesian products
        for count, cart in enumerate(carts):
            """CHANGE CART INDEX SO YOU CAN SWAP THE AMPLITUDES!!!!!!!!!!!"""

            # if c qubit is 1, apply swap t (ie. switch t qubit from state 1 to 0)
            if cart[c] == 1:
                l = 1

                # swap target
                if cart[t] == 1:
                    carts[count][t] = 0
                else:
                    carts[count][t] = 1

            # and if c qubit is 1, leave t alone

        # swap amplitudes
        for i in range(len(carts)):
            ind = get_state_index(carts[i], n)
            reg_new[i] = reg[ind]
        Reg_obj.Reg = reg_new
        Reg_obj.vector_notation()
        return Reg_obj
