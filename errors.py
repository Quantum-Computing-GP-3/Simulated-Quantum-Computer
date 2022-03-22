


class error (Exception):
    pass


#errors regarding quantum gates***************************************

class qbitidcsexceeded_in_inputERROR (error):
    #if user wants to act on a qubit outside of the size of our register
    def _init_ (self,message):
        self.message = message
    pass

#determine this error via
if max(q) -1 > Reg_obj.n:
    raise qbitidcsexceeded_in_inputERROR ('Error: the qubits you want to act on exceed the Register size')


#*************************


class state_idcs_is_not_arrayERROR(error):
    #the state indices are handed over as a list of numbers that correspond to the indices in decimal system
    def _init_ (self,message):
        self.message = message
    pass

#determine error via
if isinstance(state_list, array):
    pass
else:
    raise state_idcs_is_not_arrayERROR ('wrong format for state_list. expect array')


#******************

class state_idcs_entries_are_not_integersERROR(error):
    #the state indices are handed over as a list of numbers that correspond to the indices in decimal system
    def _init_ (self,message):
        self.message = message
    pass

#determine error via
for i in range(len(state_list)):
    if isinstance(state_list[i], int):
        pass
    else:
        raise state_idcs_entries_are_not_integersERROR ('wrong format for entries in state_list. expect integers')




#****************


class state_idcs_has_same_state_twiceERROR(error):
    #if state_list has same state twice, that one won't be amplified
    def _init_ (self,message):
        self.message = message
    pass

#where: 
#Grover

#determine error via
for i in state_list:
    if state_list.count(i) >1:
        raise state_idcs_has_same_state_twiceERROR('state_list contains some states twice. expected are distinct states')

#alternative: just change statelist so it doesnt have any element twice



#********************



class act_on_same_qubitERROR(error):
    #CNOT, Toffoli etc act on multiple distince qubits
    def _init_ (self,message):
        self.message = message
    pass

#where: 
#Toffoli, CNOT

#determine error via
for i in q:
    if q.count(i)>1:
        raise act_on_same_qubitERROR('This gate acts on multiple distinct qubits. they cannot be the same')





#************
class notnormalized(error):
    #inputstate needs to be normalized
    #alternative:
    def _init_ (self,message):
        self.message = message
    pass


#**********************

class dims_of_Regobj_and_stateERROR(error):
    #for reflection gate the Regobj size and the state size have to be the same!! 
    def _init_ (self,message):
        self.message = message
    pass

#where
#Reflection

#determine error
if len(projection) != len(input):
    raise dims_of_Regobj_and_stateERROR ('the register sizes have to be the same')





#***************************************************************************
#errors if user can type in their own initial register state:************

class wrong_register_sizeERROR(error):
    #input register size needs to be a power of 2**m
    def _init_ (self,message):
        self.message = message
    pass

#determine error
if len(Reg_obj) %2 != 0:
    raise wrong_register_sizeERROR('Error: the register size needs to be a power of 2**m')



#******************************



class initial_Regobj_does_not_contain_wanted_entryERROR(error):
    #for arbitrary input register, the desired index needs to be contained with a probability larger than 1
    def _init_ (self,message):
        self.message = message
    pass

#where:
Grover 
Reflection, Projection

#determine error
prblems = 0
for i in len(q):
    if Reg_obj[q[i] == 0:
        prblems +=1
if prblems >0:
    raise initial_Regobj_does_not_contain_wanted_entryERROR('Error: your Registerobject does not contain the states you want to amplify or project')



#**********************



class wrong_register_dim(error):
#input register needs to be 1d array
    def _init_ (self,message):
        self.message = message
    pass

