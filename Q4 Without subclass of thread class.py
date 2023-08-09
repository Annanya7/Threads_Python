from threading import *
class MySample():
    def __init__(self,n):
        self.n=n
    def disp(self):
        print("hEYA",self.n)
obj=MySample("Hema")
t1=Thread(target=obj.disp)
t1.start()
print(t1.getName())
t1.setName("MYTHREAD")
print(t1.getName())
