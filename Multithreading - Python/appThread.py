import threading
import time
import random

class BankAccount(threading.Thread):

    accBalance = 100
    def __init__(self, name, moneyRequest):
        threading.Thread.__init__(self)
        self.name = name
        self.moneyRequest = moneyRequest

    def run(self):
        threadLock.acquire()
        BankAccount.getMoney(self)
        threadLock.release()

    @staticmethod
    def getMoney(customer):
        print("{} tries to withdraw ${} at {}".format(customer.name,
            customer.moneyRequest,time.strftime("%H: %M: %S",time.gmtime())))

        if BankAccount.accBalance - customer.moneyRequest > 0:
            BankAccount.accBalance -= customer.moneyRequest
            print("New Account Balance : ${}".format(BankAccount.accBalance))
        else:
            print("Not enough money in account")
            print("Current Balance: ${}".format(BankAccount.accBalance))

        time.sleep(3)

threadLock = threading.Lock()
ajith = BankAccount("Ajith",1)
gowtham = BankAccount("Gowtham",100)
arvind = BankAccount("Arvind", 50)

ajith.start()
gowtham.start()
arvind.start()

ajith.join()
gowtham.join()
arvind.join()

print("Transaction ends")
