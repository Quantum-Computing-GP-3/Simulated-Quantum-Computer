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
                "O": self.O_init,
                "G": self.G_init,
                "X": self.X_init,
                "Z": self.Z_init,
                "R": self.R_init,
                "Toffoli": self.T_init

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
        #self.act = self.act_choose

        self.act = self.act_H
    def act_H(self, Reg_obj, q=None, all=False, state=None):
        #cosiv2
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
        size = 2 ** (Reg_obj.n)


        for qbit in q:
            i = 0
            # print(j)
            while i <= size - 2 ** qbit:
                for _ in range(2 ** qbit):
                    # print('i',i)
                    a = reg[i]
                    b = reg[i + 2 ** qbit]
                    # for H acting on state i, we need to find out the two states that are the result of H acting on i
                    # those are i and i+2**qbit
                    # since those are the same as the states involved for H acting on i+2**qbit, we take care of the
                    # action of H on both states at once -> less looping

                    # print(a,b, a+b, a-b)
                    reg[i] = 1 / np.sqrt(2) * (a + b)
                    reg[i + 2 ** qbit] = 1 / np.sqrt(2) * (a - b)
                    # then we need to redefine the amplitudes of states i and i+2**qbit, considering the action of H

                    # print(i, reg[i], i+2**j, reg[i+2**j], -2/np.sqrt(2))
                    i += 1
                i += 2 ** qbit
                # the variation of the step width achieves that we don't loop over any second state i+2**qbit again that we already took care of
        Reg_obj.Reg = reg



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
    def act_CNOT(self, Reg_obj, q=None, all=False, state=None):
        #cosiv2
        # error catching if q is not a 2 tupel
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
        size = 2 ** (Reg_obj.n)
        reg = Reg_obj.Reg

        if all == True:
            return 1  # error!!!!!!

        c = q[0]  # control position
        t = q[1]  # target position

        i = 0
        qprime = np.sort(q)  # yes I am sorting a list of size 2
        cond1 = 2 ** qprime[0]
        cond2 = 2 ** qprime[1]
        between = cond2 / (cond1 * 2)
        i = 2 ** (c)
        while i < size - 1:
            for _ in range(int(between)):
                for _ in range(cond1):
                    a = reg[i]
                    b = reg[i + 2 ** t]
                    reg[i] = b
                    reg[i + 2 ** t] = a
                    i += 1
                i += cond1
            i += cond2

        Reg_obj.Reg = reg



    def O_init(self):
        """
        initialise O gate
        calculated algorithmically, so pass self.act to own act function, act_O
        """
        #if act called, it calls act_O
        self.act = self.act_O
    def act_O(self, Reg_obj,state_list):
        """
        function to act oracle
        :param Reg_obj: obj
            Register object
        :param q: list
            qubit(s) to act on
        :param all: bool
            Whether or not th egate should be acted on all qubits
        :param state: string of 1&0's etc "1100"
            state for oracle
        :return:
        """
        n = Reg_obj.n
        """
        #original matrix implimentation which is slower:
        matrix_O = np.eye(2**n)

        #applying a -1 in the matrix for each state in state_list
        for i in range(len(state_list)):
            matrix_O[state_list[i], state_list[i]] = -1


        #if the gate is actually an operator (like G or O)
        Reg_obj.Reg = np.matmul(matrix_O, Reg_obj.Reg)

        """
        #new, non matrix implimentation
        for i in range(len(state_list)):
            #assumes numerical state
            idx = state_list[i]
            Reg_obj.Reg[idx] = - Reg_obj.Reg[idx]



    def G_init(self):
        """
        initialise G gate
        calculated algorithmically, so pass self.act to own act function, act_G
        """
        #if act called, it calls act_G
        self.act = self.act_G
    def act_G(self,Reg_obj, q = None, all = False, state = None):
        """
        function to act grovers operator thingy
        :param Reg_obj: obj
            Register object
        :param q: list
            qubit(s) to act on
        :param all: bool
            Whether or not th egate should be acted on all qubits
        :param state: string of 1&0's etc "1100"
            state for oracle
        :return:
        """

        #original implimentation
        n = Reg_obj.n
        N = 2**n
        matrix_G = np.ones((N, N)) * 2 / N

        for i in range(N):
            matrix_G[i, i] -= 1

        Reg_obj.Reg = np.matmul(matrix_G, Reg_obj.Reg)
        """
        #new cosi implimentation, way slower
        n = Reg_obj.n
        N = Reg_obj.N

        diag = 2/N-1
        rest = 2/N

        reg_old = Reg_obj.Reg
        reg_new = np.zeros(N, dtype = "complex")

        for i in range(N):
            for j in range(N):
                if i==j:
                    reg_new[i] += diag * reg_old[j]
                else:
                    reg_new[i] += rest * reg_old[j]

        Reg_obj.Reg = reg_new
        """



    def X_init(self):
        """
        initialise X gate
        calculated algorithmically, so pass self.act to own act function, act_X
        """
        #if act called, it calls act_X
        self.act = self.act_X
    def act_X(self,Reg_obj, q = None, all = False):
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
        size = 2**(Reg_obj.n)
        #error if q is not ???
        for qbit in q:
            i=0
            while i <= size-2**qbit:
                #print(i)
                for _ in range (2**qbit):
                    a = reg[i]
                    b = reg[i+2**qbit]
                    reg[i] = b
                    reg[i+2**qbit] = a
                    i += 1
                i += 2**qbit
        Reg_obj.Reg = reg



    def Z_init(self):
        """
        initialise Z gate
        calculated algorithmically, so pass self.act to own act function, act_Z
        """
        #if act called, it calls act_Z
        self.act = self.act_Z
    def act_Z(self,Reg_obj, q = None, all = False):
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
        size = 2**(Reg_obj.n)
        #error if q is not ???

        for qbit in q:
            print(qbit)
            i= 2**qbit
            while i <= size-1:
                for _ in range(2**qbit):
                    reg[i] = reg[i]* (-1)
                    i += 1
                i += 2**qbit
        Reg_obj.Reg = reg





    def R_init(self):
        """
        initialise Reflection gate
        calculated algorithmically, so pass self.act to own act function, act_R
        """
        #if act called, it calls act_R
        self.act = self.act_R
    def act_R(self,Reg_obj, projection_state, oracle = False):
        """
        explanations and eceptions
        """


        N = Reg_obj.N
        m = Reg_obj.n

        Reg_obj.Norm


        save_total_state = np.copy(Reg_obj.Reg)
        new_state = np.copy(save_total_state)

        for i in range(N):
            new_state_entryi = 0
            for j in range(N):
                new_state_entryi += projection_state[i] * projection_state[j] * save_total_state[j]
            # print(new_state_entryi,projection_state[i])
            new_state[i] = new_state_entryi
            # print(new_state, save_total_state)
        refl = 2 * new_state - 1 * save_total_state
        refl =norm(refl)
        if oracle == False:
            Reg_obj.Reg = refl
        if oracle == True:
            Reg_obj.Reg = -refl




    def T_init(self):
        """
        initialise Z gate
        calculated algorithmically, so pass self.act to own act function, act_Z
        """
        #if act called, it calls act_Z
        self.act = self.act_T
    def act_T(self,Reg_obj, q = None, all = False, state = None):

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
        size = 2**(Reg_obj.n)
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

        while i < size-1:
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
        Reg_obj.Reg = reg






def norm(Reg_obj, q = None, all = False, state = None):
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



















    def act_choose(self, Reg_obj, q=None, all=False, state=None):
        """
        function to decide what was to act a gate if not doing gate algorithmically

        :param Reg_obj: obj
            Register object
        :param q: list
            qubit(s) to act on
        :param all: bool
            Whether or not th egate should be acted on all qubits
        :param state: string of 1&0's etc "1100"
            state for oracle

        :return:
        """
        # if user wants it acted on all qubits
        if all == True:
            self.acts_on_all(Reg_obj)
        else:
            self.Stu_acts_on(q, Reg_obj)











    def acts_on(self, q, Reg_obj):
        """

        NOW TAKES A 2D INPUT AND CONVERTS TO TENSOR

        Given a quantum register, the quantum gate will act on the quantum qubits
        specified in the list q. 
        
        For example, if q = [0,1], the quantum gate will act on the first and second
        qubit of the register.   

        Parameters
        ----------
        q : List
            Specifies on which qubit(s) of the quantum register the quantum gate 
            will act on. Numbering of the qubits starts at zero. 
        reg : Complex Numpy Array
            Specifies the quantum register the quantum gate will act on.

        Returns
        -------
        reg_new : Complex Numpy Array
            Resulting quantum register.

        """
        # Complex array to store the resulting quantum register after the quantum
        # gate has been applied.

        #Reg_obj is register object, Reg is Quantum_Register class function, reg is what I will call the tensor register in this function
        Reg_obj.tensor_notation()
        reg = Reg_obj.Reg


        reg_new = np.zeros_like(reg)
        
        # Checks we are acting on the amount of qubits the quantum gate is designed for.
        if len(q) != self.size:
            sys.exit("This quantum gate does not act on the number of qubits specified")
        
        # Checks we are not acting on more qubits than exist in the register.
        if len(q) > np.ndim(reg):
            sys.exit("You cannot act on more qubits than exist in the register.")
        
        # The first cartesian product is for iterating over the unprimed indices.
        for xs in cartesian_product_n_qubits(np.ndim(reg)):   
            
            # The second cartesian product is for iterating over the primed indices.
            # Equivalent to Einstein summation. The number of primed indices the Einstein
            # summation is done over is specified by len(q).
            for ys in cartesian_product_n_qubits(len(q)):
                
                # We now set the indices of each tensor according to tensor notation.
                indices = np.asarray(xs)
                indices_prime = indices
                indices_gate = np.zeros(len(q)*2, dtype = int)
    
                for i,y in enumerate(ys):
                    indices_prime[q[i]] = y
                    
                    indices_gate[i] = xs[q[i]]
                    indices_gate[i+len(q)]= y
     
                xs_prime = tuple(indices_prime)
                xs_gate = tuple(indices_gate)
            
                # We are now able to do the tensor product with the correct indices.
                reg_new[xs] += self.tensor[xs_gate] * reg[xs_prime]
            Reg_obj.Reg = reg_new
            Reg_obj.vector_notation()
        return


    def Stu_acts_on(self, q,Reg_obj):
        """
        Given a quantum register, the quantum gate will act on the quantum qubits
        specified in the list q.

        For example, if q = [0,1], the quantum gate will act on the first and second
        qubit of the register.

        :param Reg_obj: obj
            Register object
        :param q: list
            qubit(s) to act on


        """
        # Reg_obj is register object, Reg is Quantum_Register class function, reg is what I will call the tensor register in this function
        reg = Reg_obj.Reg
        n = Reg_obj.n

        # Checks we are acting on the amount of qubits the quantum gate is designed for.
        numq = len(q)
        if numq != self.size:
            sys.exit("This quantum gate does not act on the number of qubits specified")

        # Checks we are not acting on more qubits than exist in the register.
        if numq > n:
            sys.exit("You cannot act on more qubits than exist in the register.")

        #if number of qubits to act on is 1
        if numq == 1:
            q = q[0]


            #set start matrix (ie if its the first qubit then the first matrix is the gate, else, it is the identiy
            if q == 0:
                M = self.matrix
            else:
                M = np.eye(2, dtype=complex)



            #act the identity matrix if its not the qubit that the gate is acting on, if it is the correct qubit then act self.matrix
            for i in range(1,n):
                if q == i:
                    A = self.matrix
                else:
                    A = np.eye(2, dtype=complex)
                M = stu_kron(M, A)

            reg_new = np.matmul(M, reg)
            Reg_obj.Reg = reg_new
            return


        # if number of qubits to act on is 2
        elif numq >1:
            print("This will have to be passed to pablo's original act_on ")
            #havent done yet, shouldnt be hard atall




    def acts_on_all(self,Reg_obj):
        """
        function to act a 1 qubit gate on all qubits
        :param Reg_obj: obj
            Register object
        :return:
        """
        # Reg_obj is register object, Reg is Quantum_Register class function, reg is what I will call the tensor register in this function
        reg = Reg_obj.Reg
        n = Reg_obj.n

        #if the gate isn't 2x2, this wont work
        if self.matrix.shape != (2,2):
            sys.exit("You cannot act anything other than a 1 qubit gate using this function")

        #iterate through kron products untill we have a full matrix
        M = self.matrix
        for i in range(n-1):
            M = stu_kron(M, self.matrix)

        #matrix multiply the matrix we have built, and the state vector for new reg
        reg_new = np.matmul(M, reg)
        Reg_obj.Reg = reg_new
        return






def cartesian_product_n_qubits(n):
    """
    Given an n qubit system generates all the possible index combinations.
    
    For example, for a four qubit system it would yield the following values:
        (0,0,0,0), (0,0,0,1), (0,0,1,0),(0,0,1,1), [...], (1,1,1,1)

    Equivalent to n-nested for loops. We use yield instead of return because there
    is no need to remember the list of all index combinations. Saves memory.

    Parameters
    ----------
    n : integer
        Number of qubits in the system.

    Yields
    ------
    tuple
        Cartesian product of n indices.

    """
    pools = [(0,1)] * n
    
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for product in result:
        yield tuple(product)


def stu_kron(a, b):
    """
    kronecker product function
    ASSUMING NUMBER OF DIMENSIONS OF BOTH IS THE SAME so basically only works for 2x2
    !!!!!!!!!!!!! basically copied from numpy source code, stripped down alot !!!!!!





    [[1 2]
     [3 4]]
    [[1. 0.]
     [0. 1.]]
    results in
    [[1. 0. 2. 0.]
     [0. 1. 0. 2.]
     [3. 0. 4. 0.]
     [0. 3. 0. 4.]]


    Parameters
    ----------
    a, b : array_like
        arrays to find the kronecker product of

    Returns
    ----------
    Kron: array_like
        Kronecker product

    """
    a_dim = a.ndim
    b_dim = b.ndim

    # if one is a scalar, normal multiply
    if a_dim == 0 or b_dim == 0:
        return a * b

    #outer product
    outer = a.flatten()[:, np.newaxis] * b.flatten()[np.newaxis, :]

    #reshape and concantenate for kron product
    kron = outer.reshape(a.shape + b.shape)
    # concantenate for correct dimensions
    for i in range(a_dim):
        kron = np.concatenate(kron, axis=a_dim - 1)

    return kron


def get_state_index(ind,n):
    """
    function to find the amplitude of a certain state
    :param ind: list of 1 or 0's
        specifies the state we want to view
    :param n: int
        number of qubits
    :return: coefficient of state
    """

    # could be a magic function or something
    # very ineficient in its current form but only have to call once

    """ ie.

        get_state_index([0, 0, 0, 1])
        returns 1

        get_state_index([1, 1, 1, 1])
        returns 15

        as expected

        """


    rang = np.flip(np.arange(0, n))
    reg_route = np.zeros(len(rang))
    for count, i in enumerate(rang):
        reg_route[count] = 2 ** i

    state_2d_index = np.sum(np.array(ind) * reg_route)

    return int(state_2d_index)


def stu_cartesian_product_n_qubits(n):
    """
    Stu needed the full return not yield so added this function

    Given an n qubit system generates all the possible index combinations.

    For example, for a four qubit system it would yield the following values:
        (0,0,0,0), (0,0,0,1), (0,0,1,0),(0,0,1,1), [...], (1,1,1,1)

    Equivalent to n-nested for loops. We use yield instead of return because there
    is no need to remember the list of all index combinations. Saves memory.

    Parameters
    ----------
    n : integer
        Number of qubits in the system.

    Yields
    ------
    tuple
        Cartesian product of n indices.

    """
    pools = [(0, 1)] * n

    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    return result

def norm(Reg_obj, q=None, all=False, state=None):
    if all == True:
        return 1
    N = len(Reg_obj)
    n = int(np.log2(N))
    sum = 0
    reg = Reg_obj
    for i in range(N):
        sum += reg[i] ** 2
    Norm = 1 / np.sqrt(sum)
    return Norm * reg

