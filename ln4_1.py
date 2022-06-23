"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта 
   заработной платы сотрудника. Используйте в нём формулу: 
   (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для 
   конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv


def salary():
    if len(argv) == 4:
        time_work, rate, prize = int(argv[1]), float(argv[2]), float(argv[3])
    else:
        time_work = int(input("Выработка в часах: "))       
        rate = float(input("Ставка в час: "))
        prize = float(input("Премия: "))

    return f'Заработная плата сотрудника: {((time_work * rate) + prize)} руб.'


print(salary())