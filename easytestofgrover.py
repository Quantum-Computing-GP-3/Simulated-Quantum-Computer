#%%
import numpy as np
import sys
import matplotlib.pyplot as plt


#defitions***************************+

def norm(Reg_obj, q = None, all = False, state = None):
        if all == True:
            return 1
        N = len(Reg_obj)
        n = int(np.log2(N))
        sum = 0
        reg = Reg_obj
        for i in range (N):
            sum += reg[i]**2
        Norm = 1/np.sqrt(sum)
        return Norm*reg

def act_H(Reg_obj, q = None, all = False, state = None):    
        n = int(np.log2(len(Reg_obj)))
        N = len(Reg_obj)
        #print('act_H: n, len(Reg_obj)', n, len(Reg_obj))
        
        if all == True:
            q = [i for i in range(n)]

        reg = Reg_obj
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
        #print(reg)
        return reg




def act_R( total_state, projection_state): 
    N = len(total_state)
    n = np.log2(N)
    #print(projection_state, total_state)
    total_state = norm(total_state)
    #print('total_state after norm', total_state)
    
    save_total_state = np.copy(total_state)
    new_state = np.copy(total_state)

    for i in range(N):
        new_state_entryi = 0
        for j in range(N):
            new_state_entryi += projection_state[i]*projection_state[j]*total_state[j]
        #print(new_state_entryi,projection_state[i])
        new_state[i] = new_state_entryi    
    #print(new_state, save_total_state)             
    refl = 2*new_state - 1*save_total_state
    #print('\n\n reflection', refl)
    return refl




#main******************************

state_list= [0,9]  #which state is the one we are looking for, as given in index form (e.g. 6 = 0110)
#using multiple states is easy: we need to have a list anyways and it can be rather long
number_right_answers = len(state_list)
n_required = len(bin(max(state_list)))-2       
N_required = 2**n_required

state_list_as_Reg_obj = np.zeros(N_required)
for i in range (number_right_answers):
    state_list_as_Reg_obj [state_list[i]] = 1
print('desired state in register form',state_list_as_Reg_obj)
#now we got a register only with the desired states marked
#we will need that for the Oracle reflection function
#if you can think of a better way to get the states across to act_R, that'd be awesome




#now we can test it out

Reg_1 = np.zeros(N_required)
Reg_1 [0] = 1
initial_state = np.copy(Reg_1)
initial_state = act_H(initial_state, all = True)
Reg = act_H(Reg_1, all = True)
print('initialized state',Reg)


n_iter = int(np.pi / 4 * np.sqrt(N_required)/number_right_answers)

#now we do O and G, both with a call to the reflection operator
# O reflects Reg around our desired states
#don't forget *(-1): since effect is '1 - projection on s'
# G reflecs our new Reg around the initial state of equal probability superpositions
for _ in range (n_iter):
    Reg = -act_R(Reg, state_list_as_Reg_obj) #minus that!!!
    #print('\n Reg after Oracle call \n',Reg)
    Reg = act_R(Reg, initial_state)
    
print('\n Reg_final', Reg)

# %%
