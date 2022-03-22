import numpy as np
import sys
from .ListQuantumGates import H, CNOT, X,Z, R


# -*- coding: utf-8 -*-

"""
QuantumGate is a class whose instances can represent the action of any quantum
gate.

"""
import numpy as np
import sys

class Quantum_Gate(object):
    def __init__(self, gate = None, matrix = None):
        """

        Establish a quantum gate object from the name of the gate for example, "Hadamard"

        :param gate: str
             name of required gate
        :param matrix: 2d numpy array
             matrix of other gate one would like to apply
        """

        if matrix and gate == None:
            sys.exit("You must specify either the name of a gate, or the matrix of a gate")
        elif matrix and gate != None:
            sys.exit("You must specify either the name of a gate, or the matrix of a gate, not both")

        #if specific gate is specified
        elif gate != None:

            func_dict = {
                "Hadamard": self.Hadamard_init,
                "CNOT": self.CNOT_init,
                "X": self.X_init,
                "Z": self.Z_init,
                "R": self.R_init,
            }

            # check if gate in dict
            if gate not in func_dict:
                sys.exit("You must specify a correct name of a gate")

            #give gate a label and allocate initialisation function
            self.label = gate
            func_dict[self.label]()

        #if user has inputted their own gate
        elif matrix != None:

            """sys exit checks on this plz
            this wont work yet I dont think
            """

            self.matrix = matrix
            self.size = self.matrix.size
            self.tensor = np.reshape(matrix, (2,)*2*self.size)



    def Hadamard_init(self):

        """
        initialise hadamard gate
        so far I havent done a true algorithmic way of doing this, but I think it's efficient enough to use Stu_acts_on or acts_on_all
        """
        self.matrix = 1/np.sqrt(2)*np.array([[1,1],
                                              [1,-1]])
        self.size = int(np.round(np.log2(self.matrix.shape[0])))

        self.tensor = np.reshape(self.matrix, (2,2))

        #reroutes to act_choose
        self.act = self.act_choose



    def CNOT_init(self):
        """
        initialise CNOT gate
        can be done algorithimically or by matrices, so matrices could be included.
        Either act_on could be used
        so for now, I specify to use the act_CNOT function to act it

        """
        #if act called, it calls act_CNOT
        self.act = self.act_CNOT
        self.matrix = (np.array([[1,0,0,0],
                             [0,1,0,0],
                             [0,0,0,1],
                             [0,0,1,0]]))

        self.size = int(np.round(np.log2(self.matrix.shape[0])))
        self.tensor = np.reshape(self.matrix, (2,2,2,2))


    def X_init(self):
        """
        initialise X gate
        calculated algorithmically, so pass self.act to own act function, act_X
        """
        #if act called, it calls act_X
        self.act = self.act_X


    def Z_init(self):
        """
        initialise Z gate
        calculated algorithmically, so pass self.act to own act function, act_Z
        """
        #if act called, it calls act_Z
        self.act = self.act_Z

    
    def R_init(self):
        """
        initialise Reflection gate
        calculated algorithmically, so pass self.act to own act function, act_R
        """
        #if act called, it calls act_R
        self.act = self.act_R
    
    











    #now to the codes

    def norm(self,Reg_obj, q = None, all = False, state = None):
        '''
        function to normalize state
        :param Reg_obj: obj
            register
        :param q: list
            qubits to act on
        :param all: bool
            whether gate should be acted on all qubits
        :param state:
            state for oracle

        '''
        #errorcatching:
        if all == True:
            return 1
        
        sum = 0
        reg = Reg_obj.Reg
        for i in range (2**(Reg_obj.n)):
            sum += reg[i]**2
        Norm = 1/np.sqrt(sum)
        return Norm*reg




    def act_H(self,Reg_obj, q = None, all = False, state = None):    
        '''
        function to act Hadamard
        :param Reg_obj: obj
            register
        :param q: list
            qubits to act on
        :param all: bool
            whether Hadamard should be acted on all qubits
        :param state:
            state for oracle

        '''
        if all == True:
            q = [i for i in range(Reg_obj.n)]

        reg = Reg_obj.Reg
        N = 2**(Reg_obj.n)

        start = time.time()
        for qbit in q: 
            i = 0
            while i <= N-2**qbit:    
                for _ in range (2**qbit):   
                    a = reg[i]
                    b = reg[i+2**qbit]
                    reg[i] = 1/np.sqrt(2) * (a+b)
                    reg[i+2**qbit] = 1/np.sqrt(2) * (a-b)
                    i +=1
                i += 2**qbit
        end = time.time()
        return reg






    def act_X(self,Reg_obj, q = None, all = False, state = None):    
        '''
        function to act X
        :param Reg_obj: obj
            register
        :param q: list
            qubits to act on
        :param all: bool
            whether X should be acted on all qubits
        :param state:
            state for oracle

        '''
        if all == True:
            q = [i for i in range(Reg_obj.n)]

        reg = Reg_obj.Reg
        N = 2**(Reg_obj.n)
        #error if q is not ???
        for qbit in q:
            i=0
            while i <= N-2**qbit:
                #print(i)
                for _ in range (2**qbit):
                    a = reg[i]
                    b = reg[i+2**qbit]
                    reg[i] = b
                    reg[i+2**qbit] = a
                    i += 1
                i += 2**qbit
        return reg



    def act_Z(self,Reg_obj, q = None, all = False, state = None):    
        '''
        function to act Z
        :param Reg_obj: obj
            register
        :param q: list
            qubits to act on
        :param all: bool
            whether Z should be acted on all qubits
        :param state:
            state for oracle

        '''
        if all == True:
            q = [i for i in range(Reg_obj.n)]

        reg = Reg_obj.Reg
        N = 2**(Reg_obj.n)
        #error if q is not ???
        
        for qbit in q:
            print(qbit)
            i= 2**qbit
            while i <= N-1:
                for _ in range(2**qbit):
                    #print(i)
                    reg[i] = reg[i]* (-1)
                    #print(reg[i])
                    i += 1
                i += 2**qbit
        return reg

    def act_CNOT(self,Reg_obj, q = None, all = False, state = None):

        #error catching if q is not a 2 tupel
        '''
        function to act CNOT
        :param Reg_obj: obj
            register
        :param q: list
            qubits to act on
        :param all: bool
            whether CNOT should be acted on all qubits
        :param state:
            state for oracle

        '''
        N = 2**(Reg_obj.n)
        reg = Reg_obj.Reg

        if all == True:
            return 1 # error!!!!!!


        c= q[0]  # control position
        t= q[1]  # target position
        
        i = 0
        qprime = np.sort(q) #yes I am sorting a list of size 2
        cond1 = 2**qprime[0]
        cond2 = 2**qprime[1]
        between = cond2/(cond1*2)
        i = 2**(c)
        while i < N-1:
            for _ in range(int(between)):
                for _ in range (cond1):
                    a = reg[i]
                    b = reg[i+2**t]
                    reg[i] = b
                    reg[i+2**t] = a
                    i+=1
                i += cond1
            i += cond2
        return reg




    def act_TOFFOLI(self,Reg_obj, q = None, all = False, state = None):

        #error catching if q is not a 3 tupel
        '''
        function to act CNOT
        :param Reg_obj: obj
            register
        :param q: list
            qubits to act on
        :param all: bool
            whether Hadamard should be acted on all qubits
        :param state:
            state for oracle

        '''
        N = 2**(Reg_obj.n)
        reg = Reg_obj.Reg
        
        if all == True:
            return 1 # error!

        c1= q[0]  # control position
        c2= q[1]  # control position2
        t = q[2]
        qprime = np.sort(q) # sorting a list with 3 entries
        
        cond1 = 2**qprime[0]
        cond2 = 2**qprime[1]
        cond3 = 2**qprime[2]
        between1 = cond2/(cond1*2)
        between2 = cond3/(cond2*2)
            
        i = 2**(c1) +2**(c2)

        while i < N-1:
            for _ in range(int(between2)):
                for _ in range (int(between1)):
                    for _ in range (cond1):
                        a = reg[i]
                        b = reg[i+2**t]
                        reg[i] = b
                        reg[i+2**t] = a
                        i+=1 
                    i += cond1
                i += cond2
            i += cond3
        return reg



        

    def act_R(self,Reg_obj, q = None, all = False, state = None):
        """
        explanations and eceptions
        """
        n = Reg_obj.n 
        N = 2**n
        sizestate = len(state) #how do i transfer state around which to reflect
        #make state a vector with reg_obj properties!!!!!!!!!!!!!!!!!!

        #errors
        #check that state and Reg_obj have same size
        
        #normalizations
        state = norm(state)
        reg_original = norm(np.copy(Reg_obj))
        reg = norm(Reg_obj)

       # print(state,reg)
        for i in range(sizestate):
            regentryi = 0
            for j in range(sizestate):
                regentryi += state[i]*state[j]*reg[j]
                print(regentryi, reg[j], state[i], state[j])
            reg[i] = regentryi    
        
        
        refl = 2*reg - 1*reg_original
        return refl
