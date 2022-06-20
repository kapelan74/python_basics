"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и 
   выполняющую их деление. Числа запрашивать у пользователя, предусмотреть 
   обработку ситуации деления на ноль.
"""

# вариант 1
def division1(arg1, arg2):
    try:
        return int(arg1) / int(arg2)
    except ValueError:
        return 'Ошибка ввода!'
    except ZeroDivisionError:
        return 'Нельзя делить на ноль!'


print(division1(input('Введите 1е число: '), input('Введите 2е число: ')))

# вариант 2
def division2(arg1, arg2):
    if arg1.isdigit() and arg2.isdigit():
        arg1, arg2 = int(arg1), int(arg2)
        if arg2 != 0:
            return arg1 / arg2
        else:
            return 'Нельзя делить на ноль!'
    else:
        return 'Ошибка ввода!'


print(division2(input('Введите 1е число: '), input('Введите 2е число: ')))