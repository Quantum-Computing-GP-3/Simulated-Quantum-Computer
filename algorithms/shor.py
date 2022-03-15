from algorithm import Algorithm


class Shor(Algorithm):
    """
    Runs Shor's algorithm
    """

    def launch(self):
        """
        Triggers the start of Shor's algorithm
        """
        print("WOo Shor worked")


def main():
    shor = Shor()
    shor.launch()


if __name__ == "__main__":
    main()
