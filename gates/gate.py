from abc import ABC, abstractmethod
from register import QuantumRegister as QReg

class Gate(ABC):
    """
    An abstract class to act as a template for Quantum Gates
    """

    @abstractmethod
    def acts_on(self, Reg_obj, q = None, all = None):
        """
        Method that acts the current quantum gate onto a supplied qbit
        """
        pass



    def Error_checker(self, Reg_obj, q, all):

        # check they have supplied a register object, not array or anything else
        if isinstance(Reg_obj, QReg) != True:
            raise TypeError("Error: gate expects register object as input")  # check either q or all are supplied
        if q != None and all != None:
            raise TypeError("Error: gate cannot take both 'q' and 'all' arguments")  # check that either q or all are supplied

        if q == None and all == None:
            raise TypeError("Error: gate must take either 'q' or 'all' arguments")  # check they have given a q argument
        if q != None:  # q indices need to be within the register size
            if isinstance(q, (list, tuple)) == False:
                raise TypeError(
                    'Error: gate expects list of qubit arguments')  # type of each entry in q is int (qbit number from 0 to n-1)
            if max(q) - 1 > Reg_obj.n:

                raise IndexError(
                    'Error: the qubits you want to act on exceed the Register size')  # type of q is list or similar

            for qbit in q:
                if isinstance(qbit, (int)) == False:
                    raise TypeError('Error: gate expects list of integer qubit arguments')

