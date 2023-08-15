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


class ObjectUnpacker:
    def __init__(self,):
        #uper().__init__()
        #self.unpack_object(data)
        self.info = data.info
        self.statistics = data.statistics
        CallbackA(data)
        #CallbackB(data)


        

class CallbackA(ObjectUnpacker):

    def __init__(self, data) -> None:
        super().__init__()
        pass

    def use_data(self):
        print("I AM CallbackB and I am using the object data from Object, look:")
        print("     ", self.info)

''
class CallbackB:

    def __init__(self, data) -> None:
        #super().__init__()
        pass
    
    def use_data(self):
        pass
        #print("I AM CallbackB and I am using the object data from Object, look:")
        #print("     ", self.info)
''
class MainClass(CallbackA, CallbackB): #masterclass / childclass 
    def __init__(self, data):
        super().__init__(data)
        #ObjectUnpacker(data)
        #self.unpack_object(data)
        
        
    def unpack_object(self, data):
        self.info = data.info
        self.statistics = data.statistics

    def use_children(self):
        return CallbackA().use_data(), CallbackB().use_data()



data = Object(ticker='abc')
test = MainClass(data)
test.use_children()
