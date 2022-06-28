"""
5. Создать (программно) текстовый файл, записать в него программно 
   набор чисел, разделённых пробелами. Программа должна подсчитывать 
   сумму чисел в файле и выводить её на экран.
"""

import random


def file_gen():
   with open('ln5_5.txt', 'w') as file:
      line = ' '.join([str(random.randrange(10, 100)) for _ in range(random.randrange(10, 30))])
      file.write(line)


def sum_nums():
   with open('ln5_5.txt', 'r') as file:
      num_list = list(map(int, file.read().split()))
      print(f'Сумма чисел в файле = {sum(num_list)}')


file_gen()
sum_nums()