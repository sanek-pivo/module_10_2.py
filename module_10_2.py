from threading import Thread # импортируем threading
from time import sleep # импортируем time

class Knight(Thread): # Создаем класс Knight, наследованный от Thread
    voin = 100
    days = 0

    def __init__(self, name, power):  # используем метод __init__
        super().__init__() # вызываем конструктор через super
        self.name = name
        self.power = power

    def run(self): # метод run с порядком действия потока
        print(f'{self.name}, на нас напали!')
        while self.voin> 0:
            self.voin -= self.power
            self.days += 1
            sleep(1.0)
            if self.voin >= 0:
                print(f'{self.name} сражается {self.days} дней(дня), осталось {self.voin} воинов. \n')
        print(f'{self.name} одержал победу спустя {self.days} дней(дня)!')

  # по условию домашнего задания
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)
first_knight.start()  # запуск потока
second_knight.start()
first_knight.join() # вспомогательный поток
second_knight.join()
print(f'Все битвы закончились!')