"""
3. Реализовать функцию my_func(), которая принимает три позиционных 
   аргумента и возвращает сумму наибольших двух аргументов.
"""

def my_func(*nums):
    try:
        terms = list(map(int, nums))
        terms.remove(min(terms))
        return f'Cумма наибольших двух аргументов {terms[0]} и {terms[1]} равна: {terms[0] + terms[1]}'
    except ValueError:
        return f'Нужно вводить числа!'


print(my_func(input('Введите 1е число: '), input('Введите 2е число: '), input('Введите 3е число: ')))
