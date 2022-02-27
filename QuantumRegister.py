import numpy as np
from numpy.testing import assert_almost_equal


class QuantumRegister:
    """
    Class representing a quantum register
    """
    
    def __init__(self, coeffs, n_qbits):
        self.n = n_qbits
        # Verify coefficients are complex and can cast to numpy array
        self.reg = np.array(coeffs, dtype=complex)
        # Reshape to standard shape
        self.reg.reshape((2,)*n_qbits)

    def validate_register(self):
        """
        Verify whether this register is normalised
        """
        assert_almost_equal(np.sum(np.square(self.reg)), 1.0, 5, "this is an invalid state.", True)

    def __str__(self):
        """
        Wrapper for str casting to allow pretty printing of states
        e.g. try creating a register then directly print it, it should display in a nice way
        """
        iterator = np.nditer(self.reg, flags=['multi_index'])  # Fancy iterator to loop over full array and get indices
        string = ""
        for coeff in iterator:
            string += "{}|{}> + ".format(coeff, iterator.multi_index)

        return string[:-3]  # Remove trailing " + "

