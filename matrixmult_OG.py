
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


        # We check that "state" has the same length as the number of qubits in the register.
        if len(state) != n:
            sys.exit("The state the oracle should single out is not a valid basis state of the quantum register.")
        # "state" is then converted to decimal in order to modify the correct diagonal entry of the Oracle matrix representation.
        
        idx = int(state,2)
        Reg_obj.Reg[idx] = - Reg_obj.Reg[idx]
    


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

        diag = 2/N-1
        rest = 2/N

        reg_old = Reg_obj.Reg
        reg_new = np.zeros(N)

        for i in range(N):
            for j in range(N):
                if i==j:
                    reg_new[i] += diag * reg_old[j]
                else:
                    reg_new[i] += rest * reg_old[j]

        Reg_obj.Reg = reg_new

