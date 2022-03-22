import sys
from pathlib import Path
from os.path import join
import numpy as np

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, QSpinBox, QLineEdit

from algorithms.grover import Grover
from algorithms.quantum_error_correction import QECorrection
from algorithms.grover_with_refl import Grover_Reflection

# from groverTensorRepresentation import Grover as Grover_Tens

PKG_PATH = Path(__file__).parent.parent  # Simulated-Quantum-Computer package path


class GroverOGGUI(QWidget):
    """
    PyQt5 GUI object for visualising Grover's algorithm using O and G gates
    """
    def __init__(self):
        super(GroverOGGUI, self).__init__()
        loadUi(join(PKG_PATH, 'resource', 'groverOG.ui'), self)

        # Connect launch button to Grover's algorithm
        self.LAUNCH_GROVER = self.findChild(QPushButton, "Run")
        self.LAUNCH_GROVER.clicked.connect(self.grover_launch)

        # Parameters for Grover
        self.QBIT_SELECTION = self.findChild(QSpinBox, "RegisterSize")
        self.STATE_SELECTION = self.findChild(QLineEdit, "State")
        self.STATE_SELECTION.setText("e.g. 1, 2, 3, 4...")

        # Display GUI- should always run last in constructor
        self.show()

    # Launch Grover's algorithm
    def grover_launch(self):
        n_qbits = int(self.QBIT_SELECTION.value())
        marked_list = self.STATE_SELECTION.text().replace(" ", "").split(',')
        state = []
        for item in marked_list:
            if item.isdigit() and (0 < int(item) < (2**(n_qbits) - 1)) and (int(item) not in state):
                state.append(int(item))
            else:
                print("Input Error: '{}' is not a valid index. Inputs must be unique, comma seperated integers from 0 -> 2^no.qbits - 1".format(item))
                return
        
        grover = Grover(n_qbits, state)
        grover.launch()

        
class GroverRefGUI(QWidget):
    """
    PyQt5 GUI object for visualising Grover's algorithm using O and G gates
    """
    def __init__(self):
        super(GroverRefGUI, self).__init__()
        loadUi(join(PKG_PATH, 'resource', 'groverRef.ui'), self)

        # Connect launch button to Grover's algorithm
        self.LAUNCH_GROVER = self.findChild(QPushButton, "Run")
        self.LAUNCH_GROVER.clicked.connect(self.grover_launch)

        # Parameters for Grover
        self.QBIT_SELECTION = self.findChild(QSpinBox, "RegisterSize")
        self.STATE_SELECTION = self.findChild(QLineEdit, "State")
        self.STATE_SELECTION.setText("e.g. 1, 2, 3, 4...")

        # Display GUI- should always run last in constructor
        self.show()

    # Launch Grover's algorithm
    def grover_launch(self):
        n_qbits = int(self.QBIT_SELECTION.value())
        marked_list = self.STATE_SELECTION.text().replace(" ", "").split(',')
        state = []
        for item in marked_list:
            if item.isdigit() and (0 < int(item) < (2**(n_qbits) - 1)) and (int(item) not in state):
                state.append(int(item))
            else:
                print("Input Error: '{}' is not a valid index. Inputs must be unique, comma seperated integers from 0 -> 2^no.qbits - 1".format(item))
                return
        
        grover = Grover_Reflection(n_qbits, state)
        grover.launch()


class GroverTensGUI(QWidget):
    """
    PyQt5 GUI object for visualising Grover's algorithm using O and G gates
    """
    def __init__(self):
        super(GroverTensGUI, self).__init__()
        loadUi(join(PKG_PATH, 'resource', 'groverTens.ui'), self)

        # Connect launch button to Grover's algorithm
        self.LAUNCH_GROVER = self.findChild(QPushButton, "Run")
        self.LAUNCH_GROVER.clicked.connect(self.grover_launch)

        # Parameters for Grover
        self.QBIT_SELECTION = self.findChild(QSpinBox, "RegisterSize")
        self.STATE_SELECTION = self.findChild(QLineEdit, "State")
        self.STATE_SELECTION.setText("e.g. 1, 2, 3, 4...")

        # Display GUI- should always run last in constructor
        self.show()

    # Launch Grover's algorithm
    def grover_launch(self):
        n_qbits = int(self.QBIT_SELECTION.value())
        marked_list = self.STATE_SELECTION.text().replace(" ", "").split(',')
        state = []
        for item in marked_list:
            if item.isdigit() and (0 < int(item) < (2**(n_qbits) - 1)) and (int(item) not in state):
                state.append(int(item))
            else:
                print("Input Error: '{}' is not a valid index. Inputs must be unique, comma seperated integers from 0 -> 2^no.qbits - 1".format(item))
                return

        # Grover_Tens.main()
        print("Running Grover Tensor")


class QECGUI(QWidget):
    """
    PyQt5 GUI object for visualising Quantum Error Correction
    """

    def __init__(self):
        super(QECGUI, self).__init__()
        loadUi(join(PKG_PATH, 'resource', 'errorCorrection.ui'), self)

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
            "Grover (Tensor representation)": GroverTensGUI,
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
