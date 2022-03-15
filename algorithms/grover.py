from .algorithm import Algorithm


class Grover(Algorithm):
    """
    Runs Grover's algorithm
    """

    def launch(self):
        """
        Triggers the start of Grover's algorithm
        """
        print("WOo Grover worked")


def main():
    grover = Grover()
    grover.launch()


if __name__ == "__main__":
    main()
