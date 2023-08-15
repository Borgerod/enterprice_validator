class Parent:
    def __init__(self) -> None:
        self.info = "I AM PARENT INFO, BEEP-BOOP"

    def get_child(self):
        return Child()

class Child(Parent):
    def __init__(self) -> None:
        
        super().__init__()
        print(self.info)


p = Parent()

print(p.get_child())
""" 

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


class ParentClass:
    '''
        I represent the parent class for processing the Objects data 
    '''
    def __init__(self, object_1) -> None:
    #def __init__(self, ) -> None:
        pass
        
    def GET(self, object_1):
        return self.object_1
        

    def process(self,): 
        '''
            processing data from Object, will call child classes (calculators / formulas) to get processed data.
            then finally returns a fully processed data output
        '''
        return [Child_A().x], [Child_B().y]
    


#class Child_A:
class Child_A(Object, ParentClass):
    '''
        I represent a calculator class and are a child of Parent 
    '''

    def __init__(self) -> None:
        #passing for now 
        pass

    @property
    def x(self,):
        return self.info, 69



#class Child_B:
class Child_B(Object, ParentClass):
    '''
        I represent a calculator class and are a child of Parent 
    '''

    def __init__(self) -> None:
        #passing for now 
        pass

    @property
    def y(self,): 
        return self.statistics, 420


def main():
    object_1 = Object(ticker='abc')

    p = ParentClass(object_1)    
    print(
        p.process()
    )


if __name__ == '__main__':
    main()


"""