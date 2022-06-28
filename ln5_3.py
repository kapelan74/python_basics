"""
3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и 
   величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад 
   менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины 
   дохода сотрудников.
"""

import random

# Эмулятор не программного создания текстового файла
def file_gen():
   workers = ['Иванов', 'Петров', 'Сидоров', 'Сулимов', 'Лазарев',
              'Жданова', 'Скворцова', 'Синицына', 'Ларина', 'Васильева']
   
   with open('ln5_3.txt', 'w') as file:
      for worker in workers:
         line = f'{worker} {random.uniform(15000, 25000):.2f}'
         file.write(line + '\n')


def calc():
   with open('ln5_3.txt', 'r') as file:
      print('Сотрудники с окладом меньше 20т.р\n' + '=' * 30)
      income = []
      for line in file:
         line = line.split()
         sname, salary = line[0], line[1]
         
         income.append(float(salary))
         if float(salary) < 20000:
            print(sname)

      print('=' * 30)
      print(f'Cредняя величина дохода сотрудников:\n{(sum(income) / len(income)):.2f}')


file_gen()
calc()