import sys
from subprocess import call
from pathlib import Path
from os.path import join
from os import listdir

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox

from algorithms.grover import Grover
from algorithms.shor import Shor


# Simulated-Quantum-Computer package path
PKG_PATH = Path(__file__).parent.parent

ALGORITHMS = ["Grover", "Shor"]


class MainGUI(QWidget):
    """
    PyQt5 GUI object allowing users to interact with the simulation graphically
    """
    def __init__(self):
        super(MainGUI, self).__init__()
        uic.loadUi(join(PKG_PATH, 'resource/mainpage.ui'), self)
        self.widget = None

        # Add Algorithms listed in the appropriate directory
        self.ALG_MENU = self.findChild(QComboBox, "Selector")
        for alg in ALGORITHMS:
            self.ALG_MENU.addItem(alg)

        # Connect Launch button with its callback
        self.LAUNCH_BUTTON = self.findChild(QPushButton, "Launch")
        self.LAUNCH_BUTTON.clicked.connect(self.launch_callback)

        # Display GUI- should always run last in constructor
        self.show()

    def launch_callback(self):
        # Temporarily running algorithms here instead of in a new window
        alg_to_run = self.ALG_MENU.currentText()
        if alg_to_run == "Grover":
            self.widget = GroverGUI()
        elif alg_to_run == "Shor":
            self.widget = ShorGUI()
        else:
            sys.exit("ERROR: Invalid Algorithm in Selector.")


class GroverGUI(QWidget):
    """
    PyQt5 GUI object for visualising Grover's algorithm
    """
    def __init__(self):
        super(GroverGUI, self).__init__()
        uic.loadUi(join(PKG_PATH, 'resource/grover.ui'), self)

        self.LAUNCH_GROVER = self.findChild(QPushButton, "RunGrover")
        self.LAUNCH_GROVER.clicked.connect(self.grover_launch)

        # Display GUI- should always run last in constructor
        self.show()

    def grover_launch(self):
        grover = Grover()
        grover.launch()


class ShorGUI(QWidget):
    """
    PyQt5 GUI object for visualising Shor's algorithm
    """

    def __init__(self):
        super(ShorGUI, self).__init__()

        # Display GUI- should always run last in constructor
        self.show()
        

def main():
    app = QApplication(sys.argv)
    window = MainGUI()
    app.exec_()


if __name__ == '__main__':
    main()
