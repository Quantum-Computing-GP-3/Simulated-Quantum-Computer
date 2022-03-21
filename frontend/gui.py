import sys
from pathlib import Path
from os.path import join
import matplotlib.pyplot as plt

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, QSpinBox, QLineEdit

from algorithms.grover import Grover
from algorithms.quantum_error_correction import QECorrection
from algorithms.grover_with_refl import Grover_Reflection

PKG_PATH = Path(__file__).parent.parent  # Simulated-Quantum-Computer package path
ALGORITHMS = ["Grover (O & G gates)", "Grover (Reflection gates)", "Grover (Tensor representation)", "Quantum Error Correction"]  # List of algorithms


class MainGUI(QWidget):
    """
    PyQt5 GUI object allowing users to interact with the simulation graphically
    """
    def __init__(self):
        super(MainGUI, self).__init__()
        uic.loadUi(join(PKG_PATH, 'resource', 'mainpage.ui'), self)
        self.widget = None

        # Add Algorithms listed in the appropriate directory
        self.ALG_MENU = self.findChild(QComboBox, "Selector")
        self.ALG_MENU.clear()
        for alg in ALGORITHMS:
            self.ALG_MENU.addItem(alg)

        # Connect Launch button with its callback
        self.LAUNCH_BUTTON = self.findChild(QPushButton, "Launch")
        self.LAUNCH_BUTTON.clicked.connect(self.launch_callback)

        # Display GUI- should always run last in constructor
        self.show()

    # Launch appropriate window
    def launch_callback(self):
        alg_to_run = self.ALG_MENU.currentText()
        if alg_to_run == "Grover (O & G gates)":
            self.widget = GroverOGGUI()  # Launch Grover GUI
        elif alg_to_run == "Quantum Error Correction":
            self.widget = QECGUI()  # Launch Shor GUI
        else:
            sys.exit("ERROR: Invalid Algorithm in Selector.")


class GroverOGGUI(QWidget):
    """
    PyQt5 GUI object for visualising Grover's algorithm
    """
    def __init__(self):
        super(GroverOGGUI, self).__init__()
        uic.loadUi(join(PKG_PATH, 'resource', 'grover.ui'), self)

        # Connect launch button to Grover's algorithm
        self.LAUNCH_GROVER = self.findChild(QPushButton, "RunGrover")
        self.LAUNCH_GROVER.clicked.connect(self.grover_launch)

        # Parameters for Grover
        self.QBIT_SELECTION = self.findChild(QSpinBox, "RegisterSize")
        self.STATE_SELECTION = self.findChild(QLineEdit, "State")

        # Display GUI- should always run last in constructor
        self.show()

    # Launch Grover's algorithm
    def grover_launch(self):
        n_qbits = self.QBIT_SELECTION.value()
        state = self.STATE_SELECTION.text()
        grover = Grover(n_qbits, state)
        grover.launch()


class QECGUI(QWidget):
    """
    PyQt5 GUI object for visualising Shor's algorithm
    """

    def __init__(self):
        super(QECGUI, self).__init__()

        # Display GUI- should always run last in constructor
        self.show()

    # Launch Shor's algorithm
    def shor_launch(self):
        shor = QECorrection()
        shor.launch()


def main():
    """
    Main entry point
    """
    app = QApplication(sys.argv)
    window = MainGUI()
    app.exec_()


if __name__ == '__main__':
    main()
