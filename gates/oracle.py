import sys
from gates.gate import Gate



class Oracle(Gate):

    #def __init__(self):
    #self.state = state

    def acts_on(self, Reg_obj, marked_list):
        """
        function to act oracle
        :param Reg_obj: obj
            Register object
        :param state_list: 
            list of states that the oracle marks, expected as index (not binary)
        :return:
        """

        #errors***************

        #state indices need to be within the register size
        if max(marked_list) -1 > Reg_obj.N:
            raise IndexError ('Error: the states you want to act on exceed the Register size')

        #type of state_list is list or similar
        if isinstance(marked_list, (list,tuple)) == False:
            raise TypeError('Error: gate expects list of state arguments')

        #type of each entry in state_list is int (state number from 0 to N-1)
        for state in marked_list:
            if isinstance(state, (int)) == False:
                raise TypeError('Error: gate expects list of integer qubit arguments')


        #*********************


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
        for i in range(len(marked_list)):
            #assumes numerical state
            idx = marked_list[i]
            Reg_obj.Reg[idx] = - Reg_obj.Reg[idx]
