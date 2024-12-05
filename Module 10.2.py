import threading
from time import sleep
class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.counter_days = 0
        self.number_of_enemies = 100

    def fight(self):
        while self.number_of_enemies:
            self.number_of_enemies -= self.power
            sleep(1)
            self.counter_days += 1
            if self.number_of_enemies < 0:
                break
            print(f"{self.name} сражается {self.counter_days} "
                  f"{'день' if self.counter_days == 1 else ('дня' if 1 < self.counter_days < 5 else 'дней')}, "
                  f"осталось {self.number_of_enemies} воинов.")


    def run(self):
        print(f"{self.name}, на нас напали!")
        self.fight()
        print(f"{self.name} одержал победу спустя {self.counter_days} "
              f"{'день' if self.counter_days == 1 else ('дня' if 1 < self.counter_days < 5 else 'дней')}!")

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
third_knight = Knight("Sir Urban", 30)

# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
third_knight.start()
