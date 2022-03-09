def act_H(self,Reg_obj, q = None, all = False, state = None):
    #register array, size of register, 
    # qubit positions q for qubits that H acts on, q is array
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
    size = 2**(Reg_obj.n)
    for j in q: 
        i = 0
        while i <= size-2**j:         
            a = reg[i]
            b = reg[i+2**j]
        
            reg[i] = 1/np.sqrt(2) * (a+b)
            reg[i+2**j] = 1/np.sqrt(2) * (a-b)

            if (i+1)%(2**j) ==0:
                step = 2**j+1
            else:
                step = 1
            i += step