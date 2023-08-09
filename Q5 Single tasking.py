# Single Tasking is when one thread performs all the operations
from threading import *
from time import *
class MyThreadSample():
    def get_threads(self):
        self.task1()
        self.task2()
    def task1(self):
        print("Boil milk")
        sleep(5)
        print("Done")
    def task2(self):
        print("Add ingredients")
        sleep(10)
        print("Done")
obj=MyThreadSample()
t1=Thread(target=obj.get_threads)
t1.start()

