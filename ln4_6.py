"""
6. Реализовать два небольших скрипта:
   - итератор, генерирующий целые числа, начиная с указанного;
   - итератор, повторяющий элементы некоторого списка, определённого заранее. 
   Подсказка: используйте функцию count() и cycle() модуля itertools. 
   Обратите внимание, что создаваемый цикл не должен быть бесконечным. 
   Предусмотрите условие его завершения.
"""

from itertools import cycle, count


def script_a(start_num, stop_num):
    '''
    итератор, генерирующий целые числа, начиная с указанного
    '''
    print('===== Script_A =====')
    for num in count(start_num):
        if num < stop_num:
            print(num)
        else:
            break


def script_b(start_num, stop_num):
    '''
    итератор, повторяющий элементы некоторого списка, определённого заранее
    '''
    print('===== Script_B =====')
    num_list = range(start_num, stop_num)
    count = 0
    for num in cycle(num_list):
        if count < len(num_list):
            print(num)
            count += 1
        else:
            break


start_num = int(input('Введите начальное число: '))
stop_num = int(input('Введите конечное число: '))

script_a(start_num, stop_num)
script_b(start_num, stop_num)
