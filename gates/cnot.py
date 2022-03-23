from .gate import Gate


class CNOT(Gate):

    def acts_on(self, Reg_obj, q):
        '''
        function to act CNOT
        :param Reg_obj: QReg object
            register for state vector
        :param q: list
            qubits to act on
        '''

        # errors**************
        self.Error_checker(Reg_obj, q, None)
        if len(q) != 2 or len(q) != len(set(q)):
            raise ValueError(
                'Error: gate expects 2 nonidentical qubit arguments')
        #**********************


        c = q[0]  # control position
        t = q[1]  # target position

        i = 0     #index counting variable

        if c < t:
            cond1 = 2 ** c
            cond2 = 2 ** t
        else:
            cond1 = 2**t
            cond2 = 2**c
        # these two conditions define the steps that have to be taken to target the right register indices/basis states
        #cond1 < cond2

        between = cond2 / (cond1 * 2) 
        #between defines the number of same-state-blocks of the qubit with the smallest number position within one same-state-block of the larger qubit number position

        
        i = 2 ** (c)
        # starting index is first one where control qubit is 1

        while i < Reg_obj.N - 1:
            for _ in range(int(between)):
                for _ in range(cond1):
                    a = Reg_obj.Reg[i]
                    # NOT gate flips the entries of state i and state i+2**t
                    b = Reg_obj.Reg[i + 2 ** t]
                    Reg_obj.Reg[i] = b
                    Reg_obj.Reg[i + 2 ** t] = a
                    i += 1
                i += cond1
            i += cond2
