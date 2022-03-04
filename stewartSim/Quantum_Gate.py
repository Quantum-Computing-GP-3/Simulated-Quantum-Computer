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
                "G": self.G_init
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


    def O_init(self):
        """
        initialise O gate
        calculated algorithmically, so pass self.act to own act function, act_O
        """
        #if act called, it calls act_O
        self.act = self.act_O


    def G_init(self):
        """
        initialise G gate
        calculated algorithmically, so pass self.act to own act function, act_G
        """
        #if act called, it calls act_G
        self.act = self.act_G

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




    def act_O(self, Reg_obj, q = None, all = False, state = None):
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
        matrix_O = np.eye(2**n)


        # We check that "state" has the same length as the number of qubits in the register.
        if len(state) != n:
            sys.exit("The state the oracle should single out is not a valid basis state of the quantum register.")
        # "state" is then converted to decimal in order to modify the correct diagonal entry of the Oracle matrix representation.
        matrix_O[int(state, 2), int(state, 2)] = -1

        #if the gate is actually an operator (like G or O)
        Reg_obj.Reg = np.matmul(matrix_O, Reg_obj.Reg)


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
        n = Reg_obj.n
        N = 2**n
        matrix_G = np.ones((N, N)) * 2 / N

        for i in range(N):
            matrix_G[i, i] -= 1

        Reg_obj.Reg = np.matmul(matrix_G, Reg_obj.Reg)


    def act_CNOT(self,Reg_obj, q = None, all = False, state = None):
        """
        function toa ct CNOT, remembering that all cnot does is swap the amplitude of qubits
        ALGORITHMIC METHOD, NOT MATRIX METHOD

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

        # Reg_obj is register object, Reg is Quantum_Register class function, reg is what I will call the tensor register in this function
        reg = Reg_obj.Reg
        n = Reg_obj.n

        reg_new = np.zeros_like(reg)

        c = q[0]
        t = q[1]

        # array of cartesian products
        carts = stu_cartesian_product_n_qubits(n)

        #loop through cartesian products
        for count, cart in enumerate(carts):
            """CHANGE CART INDEX SO YOU CAN SWAP THE AMPLITUDES!!!!!!!!!!!"""

            # if c qubit is 1, apply swap t (ie. switch t qubit from state 1 to 0)
            if cart[c] == 1:
                l = 1

                # swap target
                if cart[t] == 1:
                    carts[count][t] = 0
                else:
                    carts[count][t] = 1


            # and if c qubit is 1, leave t alone


        # swap amplitudes
        for i in range(len(carts)):
            ind = get_state_index(carts[i], n)
            reg_new[i] = reg[ind]
        Reg_obj.Reg = reg_new







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

