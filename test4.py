
class Base(object):
    def __init__(self):
        print("Base called")
        self.item = 0 
    
    def assign_ticker(self, ticker):
        self.ticker = ticker
        if self.ticker=='appl':
            self.item = 69
            self.item2 = 666

        elif self.ticker=='lsg':
            self.item = 420
            self.item2 = 333

        else:
            self.item = 0 
            self.item2 = 111

class ChildA(Base):
    #def __init__(self, base):
    def __init__(self):
        super().__init__()
        #Base.__init__(self)
        
    @property
    def processItem(self):
        print(TARGET.item)
        return TARGET.item + 1


class ChildB(Base):
    #def __init__(self, base):
    def __init__(self):
        super().__init__()
        #Base.__init__(self)
        
    @property
    def processItem2(self):
        print(TARGET.item)
        return TARGET.item2 + 1


class MainClass(ChildA, ChildB):

    def __init__(self):
        super().__init__()

    @property
    def fully_processed(self):

        return (self.processItem * 2) /self.processItem2


TARGET = Base()
TARGET.assign_ticker('appl')

#print(TARGET.item)

COMPEDITOR = Base()
COMPEDITOR.assign_ticker('lsg',)


#print(TARGET.item, COMPEDITOR.item)

#print(ChildA().processItem)
print(MainClass().fully_processed)

# class Grandparent(object):
#     def my_method(self):
#         print ("Grandparent")

# class Parent(Grandparent):
#     def my_method(self):
#         print ("Parent")

# class Child(Parent):
#     def my_method(self):
#         print ("Hello Grandparent")
#         Grandparent.my_method(self)


# c=Child()
# c.my_method()


# print(

#     '''_____________________________________________________________________________________________________________________
#     '''
# )



# class Base(object):
#     def __init__(self, ticker):
#         self.ticker=ticker
#         print("Base created")
    
#     @property
#     def baseItem(self):
#         return 69
        
# class ChildA(Base):
#     def __init__(self, base):
#         Base.__init__(self)

#     def processItem(self):
#         return self.baseItem + 1
        
# class ChildB(Base):
#     def __init__(self, base):
#         super(ChildB, self).__init__()

#     def processItem(self):
#         return self.baseItem + 1
    

# class Parent(Base):
    

#     def __init__(self, base):
#         super(Base, self,).__init__()
#         self.base = base
#         self.a = ChildA(base) 
#         self.a = ChildB(base)

#     def sum_processed_items(self):
#         return self.a.processItem() + self.b.processItem()

# base = Base(ticker='abc')
# Parent(base)



# """
# print(

#     '''_____________________________________________________________________________________________________________________
#     '''
# )



# class Base(object):
#     def __init__(self, ticker):
#         self.ticker=ticker
#         print("Base created")
    
#     @property
#     def baseItem(self):
#         return 69
        
# class ChildA(Base):
#     def __init__(self, base):
#         Base.__init__(self)

#     def processItem(self):
#         return self.baseItem + 1
        
# class ChildB(Base):
#     def __init__(self, base):
#         super(ChildB, self).__init__()

#     def processItem(self):
#         return self.baseItem + 1
    

# class Parent(Base):
    

#     def __init__(self, base):
#         super(Base, self,).__init__()
#         self.base = base
#         self.a = ChildA(base) 
#         self.a = ChildB(base)
    
#     def get_base(self):
#         return self.base
    
#     def sum_processed_items(self):
#         return self.a.processItem() + self.b.processItem()

# base = Base(ticker='abc')
# print(Parent(base).sum_processed_items())

# """