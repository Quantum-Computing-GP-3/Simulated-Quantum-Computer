#version for our structure
#qubits from riht to left like in binary!!!

#if you have a register array with integer only, it will stay integer!!!! DANGER
#e.g. 0 0 -2 0 use 0. 0. -2. 0.
#i counted from right to left!!!!!!!!

#also: hadamard vs cnotccnot: one uses if and step the other uses algorithm to do +=
#TODo: error catching, rename indices, especially unused ones
# decide against if structure
#test ends if it works till N
#run comparison to stuarts version
#what if q is out of bounds with n?????
#error q larger than size of register
#error toffoli not exactly 3 cnot not exactly 2 qubits
#what if all in toffoli or cnot
#what do we seriously need to have as arguments of function


#z is still wrong??

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
                #for H acting on state i, we need to find out the two states that are the result of H acting on i
                #those are i and i+2**qbit
                # since those are the same as the states involved for H acting on i+2**qbit, we take care of the
                # action of H on both states at once -> less looping 
                
                #print(a,b, a+b, a-b)
                reg[i] = 1/np.sqrt(2) * (a+b)
                reg[i+2**qbit] = 1/np.sqrt(2) * (a-b)
                #then we need to redefine the amplitudes of states i and i+2**qbit, considering the action of H
                i +=1
            i += 2**qbit
            #the variation of the step width achieves that we don't loop over any second state i+2**qbit again that we already took care of

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
    size = 2**(Reg_obj.n)
    #error if q is not ???
    for qbit in q:
        i=0
        while i <= size-2**qbit:
            for _ in range (2**qbit):
                #for X acting on state i, we need to find out the stat that is the result of the action
                # this is i+2**qbit
                # since on the opposite i is the result of X acting on i+2**qbit,
                # we take care of the action of X on both states at once -> less looping 
                a = reg[i]
                b = reg[i+2**qbit]
                reg[i] = b
                reg[i+2**qbit] = a
                i += 1
            i += 2**qbit
            #the variation of the step width achieves that we don't loop over any second state i+2**qbit again that we already took care of

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
    size = 2**(Reg_obj.n)
    #error if q is not ???
    
    for qbit in q:
        # Z acts by flipping the sign on all states where qbit is 1
        #loop over all those states

        i= 2**qbit
        while i <= size-1:
            for _ in range(2**qbit):
                reg[i] = reg[i]* (-1)
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

    i = 2**(c) #starting index (state)
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



