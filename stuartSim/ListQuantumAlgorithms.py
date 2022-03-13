# -*- coding: utf-8 -*-
"""
Uses the Quantum_Algorithms class to create all the quantum gates that the quantum
computer will need.
"""
from Quantum_Gate import Quantum_Gate as QGate
from Quantum_Algorithm import Quantum_Algorithm as QAlg
import numpy as np
import sys


Grover = QAlg("Grover")
Shor = QAlg("Shor")