from .gate import Gate


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
        # no proper error check yet
        #*********************


        n = Reg_obj.n


        #new, non matrix implimentation
        for i in range(len(marked_list)):
            #assumes numerical state
            idx = marked_list[i]
            Reg_obj.Reg[idx] = - Reg_obj.Reg[idx]
