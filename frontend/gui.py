import sys
from pathlib import Path
from os.path import join
import numpy as np

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, QSpinBox, QLineEdit

from algorithms.grover import Grover
from algorithms.quantum_error_correction import QECorrection
from algorithms.grover_with_refl import Grover_Reflection

PKG_PATH = Path(__file__).parent.parent  # Simulated-Quantum-Computer package path


class GroverOGGUI(QWidget):
    """
    PyQt5 GUI object for visualising Grover's algorithm using O and G gates
    """
    def __init__(self):
        super(GroverOGGUI, self).__init__()
        loadUi(join(PKG_PATH, 'resource', 'groverOG.ui'), self)

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
        try:
            n_qbits = int(self.QBIT_SELECTION.value())
            marked_list = np.array(self.STATE_SELECTION.text().replace(" ", "").split(','), dtype=int)
            grover = Grover(n_qbits, marked_list)
            grover.launch()
        except Exception as exc:
            print(exc)
            return
        

class GroverRefGUI(QWidget):
    """
    PyQt5 GUI object for visualising Grover's algorithm using reflections
    """
    def __init__(self):
        super(GroverRefGUI, self).__init__()
        loadUi(join(PKG_PATH, 'resource', 'groverRef.ui'), self)

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
        grover = Grover_Reflection(n_qbits, state)
        grover.launch()


class GroverTensGUI(QWidget):
    """
    PyQt5 GUI object for visualising Grover's algorithm using tensor notation
    """
    def __init__(self):
        super(GroverTensGUI, self).__init__()
        loadUi(join(PKG_PATH, 'resource', 'groverTens.ui'), self)

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
        # grover = Grover(n_qbits, state)
        # grover.launch()


class QECGUI(QWidget):
    """
    PyQt5 GUI object for visualising Quantum Error Correction
    """

    def __init__(self):
        super(QECGUI, self).__init__()

        # Display GUI- should always run last in constructor
        self.show()

    # Launch Error Correction algorithm
    def QEC_launch(self):
        qec = QECorrection()
        qec.launch()


class MainGUI(QWidget):
    """
    PyQt5 GUI object allowing users to interact with the simulation graphically
    """
    def __init__(self):
        super(MainGUI, self).__init__()
        loadUi(join(PKG_PATH, 'resource', 'mainpage.ui'), self)
        self.widget = None

        # Dict of algorithms
        self.algs = {
            "Grover (O & G gates)": GroverOGGUI,
            "Grover (Reflection gates)": GroverRefGUI,
            "Grover (Tensor representation)": None,
            "Quantum Error Correction": QECGUI
            }

        # Add Algorithms listed in the appropriate directory
        self.ALG_MENU = self.findChild(QComboBox, "Selector")
        self.ALG_MENU.clear()
        for alg in self.algs.keys():
            self.ALG_MENU.addItem(alg)

        # Connect Launch button with its callback
        self.LAUNCH_BUTTON = self.findChild(QPushButton, "Launch")
        self.LAUNCH_BUTTON.clicked.connect(self.launch_callback)

        # Display GUI- should always run last in constructor
        self.show()

    # Launch appropriate window
    def launch_callback(self):
        alg_to_run = self.ALG_MENU.currentText()
        self.widget = self.algs[alg_to_run]()


def main():
    """
    Main entry point
    """
    app = QApplication(sys.argv)
    window = MainGUI()
    app.exec_()


if __name__ == '__main__':
    main()
