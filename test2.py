class Object:
    ''' 
        I represent the data object and I am essential 
    '''
    def __init__(self, ticker) -> None:
        self.ticker = ticker 

    @property
    def info(self,):
        print( f"I AM OBJECT INFO for {self.ticker}, BEEP-BOOP" )
        if self.ticker =='abc':
            return 666
        else:
            return None
        
    @property
    def statistics(self,):
        print(f"I AM OBJECT STATISTICS for {self.ticker}, BEEP-BOOP" )
        if self.ticker =='abc':
            return 123
        else:
            return None

class bigClass:
    def __init__(self, data):
        self.unpack_object(data)
        #self.A = CallbackA()
        #self.B = CallbackB()
        # self.B.point_to_A = self.A
        # #self.B.doRead(data)
        # print(self.A.transmit(), self.B.transmit())

    def unpack_object(self, data):
        self.info = data.info
        self.statistics = data.statistics

    def use_children(self):
        #return self.A.use_data(), self.B.use_data()
        return CallbackA().use_data(), CallbackB().use_data()


class CallbackA(bigClass):

    def __init__(self) -> None:
        super().__init__()

    def use_data(self):
        print("I AM CallbackB and I am using the object data from Object, look:")
        print("     ", self.info)



    #def transmit(self,data):  # See note 1
    #   return [data.statistics , 69]
    """     
    def transmit(self,data):  # See note 1
        do_stuff_with(data)   # See note 1
    """
    #def transmit(self):
    #    return [self.statistics , 69]
     
class CallbackB(bigClass):

    def __init__(self) -> None:
        super().__init__()
    
    def use_data(self):
        print("I AM CallbackB and I am using the object data from Object, look:")
        print("     ", self.info)

    '''
    def doRead(self,data):              # see note 1
        self.point_to_A.transmit(data)  # see note 2
    '''
    #def transmit(self, data):
    #    return [data.info , 420]

    #def transmit(self):
    #    return [self.info , 69]
    

data = Object(ticker='abc')
test = bigClass(data)
test.use_children()
#test.B.doRead(data)
