from threading import *
def display():
    print("Hello welcome to the first program")
def disp1():
    print("Bon Voyage")
def disp2():
    print("Byee see you")
t=Thread(target=display)
t1=Thread(target=disp1)
t2=Thread(target=disp2)
t.start()
t1.start()
t2.start()
def disp3(str):
    for i in range(1,5):
    print(i)
t3=Thread(target=disp3,args=("HEYAA",))
t4 = Thread(target=disp3,args=("Bye",))
t3.start()
t4.start()
