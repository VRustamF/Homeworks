from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name: str, power: int):
        Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies_count = 100
        self.days = 0


    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies_count:
            sleep(1)
            self.days += 1
            self.enemies_count -= self.power
            print(f"{self.name} сражается {self.days} дней(дня)..., осталось {self.enemies_count} воинов.")
        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
sleep(1.1)
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")