"""
4. Реализуйте базовый класс Car.
   у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
   А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
   опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
   добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
   для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости 
   свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""

import random


class Car:
   def __init__(self, name, speed, color, is_police=False):
      self.name = name
      self.speed = speed
      self.color = color
      self.is_police = bool(is_police)

   def go(self):
      print(f'{self.name} поехала.')

   def stop(self):
      print(f'{self.name} остановилась.')

   def turn(self, side):
      print(f'{self.name} повернула в {side}.')
      
   def show_speed(self):
      print(f'{self.name} едет со скоростью {self.speed}.')


class TownCar(Car):
   def show_speed(self):
      if self.speed > 40:
         print(f'{self.name} превышает скорость.')
      else:
         print(f'{self.name} едет с нормальной скоростью.')


class SportCar(Car):
   """Спортивный автомобиль"""


class WorkCar(Car):
   def show_speed(self):
      if self.speed > 60:
         print(f'{self.name} превышает скорость.')
      else:
         print(f'{self.name} едет с нормальной скоростью.')


class PoliceCar(Car):
   def __init__(self, speed, color, name, is_police=True):
      super().__init__(speed, color, name, is_police)


ferrari = SportCar('Феррари', 100, 'Красный')
toyota = TownCar('Тойота', 30, 'Белый')
lada = WorkCar('Лада', 70, 'Черный')
honda = PoliceCar('Хонда', 110, 'Синий')

cars = (ferrari, toyota, lada, honda)
for car in random.choices(cars):
   car.go()
   car.show_speed()
   car.turn(random.choice(('лево','право')))
   car.stop()
