class Parent:
    def mtd(self):
        print("Parent")
class Child(Parent):
    def mtd(self):
        print("Child")
def change(o=Child()):
    o.mtd()
change(Parent())
