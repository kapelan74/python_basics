"""
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. 
   Основная сущность (класс) этого проекта — одежда, которая может иметь определённое 
   название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов 
   одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут 
   быть обычные числа: V и H, соответственно.

   Для определения расхода ткани по каждому типу одежды использовать формулы: 
   для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих 
   методов на реальных данных.
   
   Реализовать общий подсчет расхода ткани. Проверить на практике полученные 
   на этом уроке знания: реализовать абстрактные классы для основных классов 
   проекта, проверить на практике работу декоратора @property.
"""

class Сlothes:
   def __init__(self, V, H):
      self.V = V
      self.H = H

   @property
   def fabric_consumption_full(self):
      return f'Общий расход ткани: {round((self.V / 6.5 + 0.5) + (self.H * 2 + 0.3))}'


class Coat(Сlothes):
   def __init__(self, V, H):
      super().__init__(V, H)
      self.coat = round(self.V / 6.5 + 0.5)

   def __str__(self):
      return f'Расход ткани на пальто {self.coat}'


class Costume(Сlothes):
   def __init__(self, V, H):
      super().__init__(V, H)
      self.costume = round(self.H * 2 + 0.3)
      
   def __str__(self):
      return f'Расход ткани на костюм {self.costume}'


coat = Coat(50, 1.80)
costume = Costume(36, 1.50)

print(coat)
print(costume)

print(coat.fabric_consumption_full)
print(costume.fabric_consumption_full)

