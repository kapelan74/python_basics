"""
3. Реализовать базовый класс Worker (работник).
   определить атрибуты: name, surname, position (должность), income (доход);
   последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
   элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
   создать класс Position (должность) на базе класса Worker;
   в классе Position реализовать методы получения полного имени сотрудника (get_full_name) 
   и дохода с учётом премии (get_total_income);
   проверить работу примера на реальных данных: создать экземпляры класса Position, 
   передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""

from tkinter import W


class Worker:
   def __init__(self, name, surname, position, wage, bonus):
       self.name = name
       self.surname = surname
       self.position = position
       self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
      def get_full_name(self):
         print(f'Полное имя сотрудника: {self.name} {self.surname}')

      def get_total_income(self):
         print(f'Доход с учетом премии: {self._income["wage"] + self._income["bonus"]}р')


worker1 = Position('Вася', 'Пупкин', 'Инженер', 15000, 0)
worker2 = Position('Петя', 'Васькин', 'Инженер', 15000, 5000)
worker3 = Position('Алексей', 'Царев', 'Начальник Отдела', 300000, 10000)

for person in (worker1, worker2, worker3):
   print('='* 25)
   person.get_full_name()
   person.get_total_income()

