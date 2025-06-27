class Parent:
    def __init__(self,num):
        self.__num=num
    def get_num(self):
        return self.__num
class Child(Parent):
    def __init__(self,val,num):
        self.__val=val
    def __init__(self, num):
        super().__init__(num)
    def get_val(self):
        return self.__val
son=Child(100)
print("Parent: Num:",son.get_num())
