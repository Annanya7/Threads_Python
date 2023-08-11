from threading import *
from time import *
def display():
    for i in range(5):
        print("normal thread ",end="")
        print(i+1)
        sleep(1)
def display_time():
    while True:
        print("Daemon Thread ",end="")
        print(ctime())
        sleep(2)
t=Thread(target=display)
t.start()
d=Thread(target=display_time)
d.setDaemon(True)
d.start()
print("done")
