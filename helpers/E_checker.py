import numpy as np
import math

import sys
sys.path.append ('C:/Users/mabon/Documents/GitHub/Simulated-Quantum-Computer/register')
from register import QuantumRegister as QReg


def Error_checker(q,Reg_obj, all):

    #check they have supplied a register object, not array or anything else
    if isinstance(Reg_obj, QReg) != True:
        raise TypeError ("Error: gate expects register object as input") #check either q or all are supplied
    if q!= None and all != None:
        raise TypeError ("Error: gate cannot take both 'q' and 'all' arguments") #check that either q or all are supplied

    if q == None and all == None:
        raise TypeError("Error: gate must take either 'q' or 'all' arguments") #check they have given a q argument
    if q != None: # q indices need to be within the register size
        if isinstance(q, (list,tuple)) == False:
            raise TypeError('Error: gate expects list of qubit arguments') #type of each entry in q is int (qbit number from 0 to n-1)
        if max(q) -1 > Reg_obj.n:
            raise IndexError ('Error: the qubits you want to act on exceed the Register size') #type of q is list or similar

        for qbit in q:
            if isinstance(qbit, (int)) == False:
                raise TypeError('Error: gate expects list of integer qubit arguments')

