from abc import ABC, abstractmethod


class Algorithm(ABC):
    """
    Abstract class acting as a template for our quantum algorithms
    """

    @abstractmethod
    def launch(self):
        """
        Method used to start running the simulation
        """
        pass
