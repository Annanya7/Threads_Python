# Here the object is treated as a thread itself, as we have inherited the superclass
from threading import *
class MyClass(Thread):
    def __init__(self,n):
        self.n=n
    def disp(self):
        print("Heloo I am",self.n)
obj=MyClass("Sheela")
obj.disp()
obj2=MyClass("Himani")
obj2.disp()
