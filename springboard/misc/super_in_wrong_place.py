from abc import ABCMeta,abstractmethod
class Parent(metaclass=ABCMeta):
    def __init__(self):
        self.a=100
    @abstractmethod
    def sample(self): pass
class Child(Parent):
    def __init__(self):
        self.a=200
    pass
class GrandChild(Child):
    def sample(self): 
        #super().__init__()
        #output is the same whether the above statement is present or not
        print(self.a)
g=GrandChild()
g.sample()
