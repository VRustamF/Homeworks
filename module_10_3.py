import threading
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            rand_numb = randint(50, 500)
            self.balance += rand_numb
            print(f"Пополнение: {rand_numb}. Баланс: {self.balance}")
            if self.balance >= 500 and self.lock.locked() == True:
                self.lock.release()
            sleep(0.001)

    def take(self):
        for _ in range(100):
            rand_numb = randint(50, 500)
            print(f"Запрос на {rand_numb}")
            if self.balance >= rand_numb:
                self.balance -= rand_numb
                print(f"Снятие: {rand_numb}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

