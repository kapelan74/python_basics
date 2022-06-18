"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. 
   Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). 
   Напишите решения через list и dict.
"""

# решение через list
def search_in_list(month):
    month_list = ['Зима', 'Весна', 'Лето', 'Осень']

    if month >= 1 and month <= 12:
        if month in [12, 1, 2]:
            print(month_list[0])
        elif month in [3, 4, 5]:
            print(month_list[1])
        elif month in [6, 7, 8]:
            print(month_list[2])
        else:
            print(month_list[3])
    else:
        print('Нет такого месяца!')

# решение через dict
def search_in_dict(month):
    month_dict = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 
                   'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}

    if month >= 1 and month <= 12:
        for key, value in month_dict.items():
            if month in value:
                print(key)
    else:
        print('Нет такого месяца!')


month = int(input('Введите номер месяца: '))
search_in_list(month)
search_in_dict(month)


