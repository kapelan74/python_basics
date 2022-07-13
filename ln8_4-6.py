"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
   А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — 
   конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите параметры, 
   общие для приведённых типов. В классах-наследниках реализуйте параметры, 
   уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники 
   на склад и передачу в определённое подразделение компании. Для хранения данных о наименовании и 
   количестве единиц оргтехники, а также других данных, можно использовать любую 
   подходящую структуру (например, словарь).

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. 
   Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""

from datetime import datetime


class SkladBase:
   time = f'{datetime.now()}'
   base = {}

   def __init__(self, title):
      self.title = title

   def to_depot(self, unit, deport):
      self.base[unit.name] = {'Инв.номер': unit.serial_num, 
                              'Дата выдачи.возврата': self.time, 
                              'Место положения': deport}

      print(f'{unit.name} выдан отделу {deport}')

   def to_sklad(self,unit):
      self.base[unit.name] = {'Инв.номер': unit.serial_num, 
                              'Дата выдачи.возврата': self.time, 
                              'Место положения': 'Склад'}

      print(f'{unit.name} возвращен на склад')

   def print_base(self):
      print(f'===== База {self.title} =====')
      for key, value in self.base.items():
         print(key, value)


class Sklad:
   def __init__(self, name, serial_num):
      self.name = name
      self.serial_num = serial_num

   def __str__(self):
      return f'Название: {self.name}\nИнв.номер: {self.serial_num}\n'


class Printer(Sklad):
   def __init__(self, name, serial_num, print_type, print_speed):
      Sklad.__init__(self, name, serial_num)
      self.print_type = print_type
      self.print_speed = print_speed
      
   def parameters(self):
      return (f'Тип принтера: {self.print_type}\n'
              f'Скорость печати: {self.print_speed} Стр\Мин.\n')


class Scanner(Sklad):
   def __init__(self, name, serial_num, scan_type, scan_permission):
      Sklad.__init__(self, name, serial_num)
      self.scan_type = scan_type
      self.scan_permission = scan_permission

   def parameters(self):
      return (f'Тип сканера: {self.scan_type}\n'
              f'Разрешение: {self.scan_permission} dpi.\n')


class Copier(Sklad):
   def __init__(self, name, serial_num, copier_type, copier_speed):
      Sklad.__init__(self, name, serial_num)
      self.copier_type = copier_type
      self.copier_speed = copier_speed

   def parameters(self):
      return (f'Тип копира: {self.copier_type}\n'
              f'Скорость печати: {self.copier_speed} Копий\Мин.\n')


base1 = SkladBase('Орг.Техника')

unit_1 = Printer('HP MF2210', 'SNP120340', 'Лазерный.', 10)
unit_2 = Scanner('Canon LiDE 110', 'SNS345789', 'Планшетный.', '2400x4800')
unit_3 = Copier('Xerox', 'SNC098345', 'Офисный.', 30)

print(unit_1)
print(unit_1.parameters())

base1.to_depot(unit_1, 'Бухгалтерия')
base1.print_base()

base1.to_depot(unit_2, 'ОПТ')
base1.to_sklad(unit_1)

base1.print_base()