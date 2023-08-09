from threading import *
def fun(str):
    print("Helo I am",str)
t=Thread(target=fun,args=("Lila",))
t.start()
t.join()
t2=Thread(target=fun,args=("Mina",))
t2.start()
t3=Thread(target=fun,args=("Shamma",))
t3.start()
    
