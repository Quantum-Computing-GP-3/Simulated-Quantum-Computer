from .algorithm import Algorithm


class Grover(Algorithm):
    """
    Runs Grover's algorithm
    """

    def __init__(self, n_qbits, state):
        self.n_qbits = n_qbits
        self.state = state

    def launch(self):
        """
        Triggers the start of Grover's algorithm
        """
        pass


def main():
    grover = Grover()
    grover.launch()


if __name__ == "__main__":
    main()
