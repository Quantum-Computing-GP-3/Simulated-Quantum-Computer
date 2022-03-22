import numpy as np
from numpy.testing import assert_almost_equal


class QuantumRegister:
    """
    Class representing a quantum register
    """
    
    def __init__(self, coeffs=None, n_qbits=1):
        self.n = n_qbits
        if coeffs == None:
            coeffs = np.zeros(2**n_qbits)
            coeffs[0] = 1

        # Verify coefficients are complex and can cast to numpy array
        self.reg = np.array(coeffs, dtype=complex)
        # Reshape to standard shape
        self.reg = np.reshape(self.reg, (2,)*n_qbits)

        # Ensure register is normalised
        self.validate_register()

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
            if coeff != 0:
                string += "{}|{}> + ".format(coeff, iterator.multi_index)

        return string[:-3]  # Remove trailing " + "
        