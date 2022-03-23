from .gate import Gate


class Pauli_X(Gate):
    def acts_on(self, Reg_obj, q=None, all=None):
        '''
        function to act X
        :param Reg_obj: obj
            register
        :param q: list
            qubits to act on
        :param all: bool
            whether X should be acted on all qubits
        '''

        if all:
            q = [i for i in range(Reg_obj.n)]

        for qbit in q:
            # X flips 0 and 1 for qbit
            # it switches the entries of states i and 2**qbit
            i = 0
            while i <= Reg_obj.N - 2 ** qbit:
                for _ in range(2 ** qbit):
                    a = Reg_obj.Reg[i]
                    b = Reg_obj.Reg[i + 2 ** qbit]
                    Reg_obj.Reg[i] = b
                    Reg_obj.Reg[i + 2 ** qbit] = a
                    i += 1
                i += 2 ** qbit
