"""
5. Реализовать класс Stationery (канцелярская принадлежность).
   определить в нём атрибут title (название) и метод draw (отрисовка). 
   Метод выводит сообщение «Запуск отрисовки»;
   создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
   в каждом классе реализовать переопределение метода draw. 
   Для каждого класса метод должен выводить уникальное сообщение;
   создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""

import random

class Stationery:
   def __init__(self, title='неизвестное пишущее средство'):
      self.title = title

   def draw(self):
      print(f'Запуск отрисовки. Используется {self.title}.')


class Pen(Stationery):
   def draw(self):
      print(f'Запуск отрисовки. Используется {self.title}.')


class Pencil(Stationery):
   def draw(self):
      print(f'Запуск отрисовки. Используется {self.title}.')


class Handle(Stationery):
   def draw(self):
      print(f'Запуск отрисовки. Используется {self.title}.')


some_writing_tool = Stationery()
pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')

random.choice((some_writing_tool, pen, pencil, handle)).draw()
