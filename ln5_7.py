"""
7. Создать вручную и заполнить несколькими строками текстовый файл, 
   в котором каждая строка будет содержать данные о фирме: название, 
   форма собственности, выручка, издержки.

   Необходимо построчно прочитать файл, вычислить прибыль каждой компании, 
   а также среднюю прибыль. Если фирма получила убытки, в расчёт средней 
   прибыли её не включать.

   Далее реализовать список. Он должен содержать словарь с фирмами и их 
   прибылями, а также словарь со средней прибылью. Если фирма получила убытки, 
   также добавить её в словарь (со значением убытков).
"""

import random, json


def file_gen():
   data = ['Фрост ООО', 'Пельмени ЗАО', 'Иванов ИП', 
           'Вареники ОАО', 'Сидоров ИП']
   
   with open('ln5_7.txt', 'w') as file:
      for unit in data:
         line = f'{unit} {random.uniform(25000, 75000):.2f} {random.uniform(25000, 75000):.2f}'
         file.write(line + '\n')


def json_creator(firm_list):
   with open("ln5_7.json", "w", encoding='utf-8') as json_file:
      json.dump(firm_list, json_file, indent=4, ensure_ascii=False,)


def profit_calc():
   with open('ln5_7.txt', 'r') as file:
      firm_list = []
      firm_dict = {}
      avg_profit = 0
      all_profit = 0
      count = 0

      for line in file:
         title, form, proceeds, costs = line.split()
         profit = float(proceeds) - float(costs)
         firm_dict[title] = float(f'{profit:.2f}')

         if profit > 0:
            all_profit += profit
            count += 1
      
      firm_list.append(firm_dict)

      try:
         avg_profit = all_profit / count
      except ZeroDivisionError:
         avg_profit = 0

      firm_list.append({'average_profit': float(f'{avg_profit:.2f}')})

      return firm_list


file_gen()
json_creator(profit_calc())