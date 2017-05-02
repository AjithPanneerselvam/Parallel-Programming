import threading
import time
import random

class CustomThread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        getTime(self.name)
        print("Thread", self.name, "Execution Ends")

def getTime(name):
    print("Thread {} sleeps at {}".format(name, time.strftime("%H: %M: %S",time.gmtime())))
    randSleepTime = random.randint(1,10)
    time.sleep(randSleepTime)

thread1 = CustomThread("One")
thread2 = CustomThread("Two")

thread1.start()
thread2.start()

print("Thread 1 Alive: ", thread1.is_alive())
print("Thread 2 Alive: ", thread2.is_alive())

print("Thread 1 Name: ", thread1.getName())
print("Thread 2 Name: ", thread2.getName())

thread1.join()
thread2.join()

print("Execution ends")
