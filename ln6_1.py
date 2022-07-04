"""
1. Создать класс TrafficLight (светофор).
   определить у него один атрибут color (цвет) и метод running (запуск);
   атрибут реализовать как приватный;
   в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
   продолжительность первого состояния (красный) составляет 7 секунд, 
   второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
   переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
   проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

from time import sleep


class TrafficLight:
   __color = {'red': 7, 'yellow': 2, 'green': 0}

   def __init__(self, green_duration, cycles):
       self.green_duration = green_duration
       self.cycles = cycles

   def running(self):
      cycle_count = 0 
      while cycle_count < self.cycles:
         cycle_count += 1
         
         print('=' * 25)
         for key, value in TrafficLight.__color.items():
            if key == 'red':
               print('Загорелся красный свет')
               sleep(value)
            elif key == 'yellow':
               print('Загорелся желтый свет')
               sleep(value)          
            elif key == 'green':
               print('Загорелся зеленый свет')
               sleep(self.green_duration)
            else:
               print('Сбой работы программы.')
               exit(-1)      


trl = TrafficLight(5, 10) # Продолжительность зеленого света и количество циклов
trl.running()
