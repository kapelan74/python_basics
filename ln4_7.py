"""
7. Реализовать генератор с помощью функции с ключевым словом yield, 
   создающим очередное значение. При вызове функции должен создаваться 
   объект-генератор. Функция вызывается следующим образом: for el in fact(n). 
   Она отвечает за получение факториала числа. В цикле нужно выводить только 
   первые n чисел, начиная с 1! и до n!.
"""

from functools import reduce


def fact(n):
   num_list = range(1, n+1)
   print('===============')
   print(f'{n}! = {reduce(lambda n1, n2: n1 * n2, num_list)}')
   for el in num_list:
      yield el


n = int(input('n = '))
for el in fact(n):
   print(el)
