"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора. 
   В список должны войти чётные числа от 100 до 1000 (включая границы). Нужно получить 
   результат вычисления произведения всех элементов списка.
   Подсказка: использовать функцию reduce().
"""

from functools import reduce

# вариант 1
def multip(num1, num2):
    return num1 * num2


def main1():
    num_list = [num for num in range(100, 1001) if num % 2 == 0]
    result = reduce(multip, num_list)
    return result


print(f'RESULT1\n{main1()}\n')


# вариант 2
def main2():
    num_list = [num for num in range(100, 1001) if num % 2 == 0]
    result = reduce(lambda n1, n2: n1 * n2, num_list)
    return result


print(f'RESULT2\n{main2()}\n')
