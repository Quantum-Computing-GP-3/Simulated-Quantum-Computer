# -*- coding: utf-8 -*-
"""
Uses the Quantum_Gate class to create all the quantum gates that the quantum
computer will need.
"""
from .Quantum_Gate import Quantum_Gate as QGate

import numpy as np 
import sys

H = QGate("Hadamard")
CNOT = QGate("CNOT")
O = QGate("O")
G = QGate("G")



    
    

    

