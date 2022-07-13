"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату 
   в виде строки формата «день-месяц-год». В рамках класса реализовать два метода. 
   Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и 
   преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, 
   должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). 
   Проверить работу полученной структуры на реальных данных.
"""

import re


class Data:

    @classmethod
    def extract(cls, my_date):
        my_date = my_date.split('-')
        if len(my_date[0]) == 2 and len(my_date[1]) == 2 and len(my_date[2]) == 4:
            if re.search(r'^0', my_date[0]) and re.search(r'^0', my_date[1]):
                return int(my_date[0][1:]), int(my_date[1][1:]), int(my_date[2])
            else:
                return int(my_date[0]), int(my_date[1]), int(my_date[2])
        else:
            return 0, 0, 0


    @staticmethod
    def valid(verified_date):
        day, month, year = verified_date
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return f'Дата {verified_date} введена корректно.'
                else:
                    return f'Неправильно введен год.'
            else:
                return f'Неправильно введен месяц.'
        else:
            return f'Неправильно введен день.'


for date in ('211-01-2022', '41-01-2022', '21-21-2022', '21-01-3022', '21-01-2022'):
    verified_date = Data.extract(date)
    print(Data.valid(verified_date))
