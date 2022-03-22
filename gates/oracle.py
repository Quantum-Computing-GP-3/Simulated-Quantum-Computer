from .gate import Gate


class Oracle(Gate):

    #def __init__(self):
    #self.state = state
    def Error_checker(self, Reg_obj, marked_list):

        if marked_list or Reg_obj == None:
            raise TypeError("Error: gate expects 2 inputs")
        if len(marked_list) > len(Reg_obj.N):
            raise IndexError('Error: the marked list you want to act on exceed the Register size')
        if isinstance(Reg_obj, QReg) != True:
            raise TypeError("Error: gate expects register object as input")

        if isinstance(marked_list, list) != True:
            raise TypeError("Error: gate list object as input")

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
        self.Error_checker(Reg_obj,marked_list)
        # no proper error check yet


            #*********************


        n = Reg_obj.n


        #new, non matrix implimentation
        for i in range(len(marked_list)):
            #assumes numerical state
            idx = marked_list[i]
            Reg_obj.Reg[idx] = - Reg_obj.Reg[idx]





