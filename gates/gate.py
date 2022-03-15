from abc import ABC, abstractmethod


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
