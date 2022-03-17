import sys
from gates.gate import Gate



class Reflection(Gate):

    #def __init__(self):
    #self.state = state

    def acts_on(self,Reg_obj_state, Reg_obj_op):
        """
        function to reflect around
        :param Reg_obj_op
            Register Object around which to reflect about
        :param Reg_obj_state
            Register Object that the reflection acts on
        """

        #errors***********
        if len(Reg_obj_op.Reg) != len(Reg_obj_state.Reg):
            raise ValueError('Error: the register sizes need to be the same')

        #*****************

        n = Reg_obj_op.n 
        N = 2**n
        
        #normalizations
        Reg_obj_op.norm
        Reg_obj_state.norm

        reg_original = Reg_obj_state.Reg.copy()
        #DOES THAT WORK??????
        
        for i in range(N):
            regentryi = 0
            for j in range(N):
                regentryi += Reg_obj_op.Reg[i]*Reg_obj_op.Reg[j]*reg_original[j]
                
            Reg_obj_state.Reg[i] = regentryi    
        
        Reg_obj_state.Reg = 2*Reg_obj_state.Reg - reg_original