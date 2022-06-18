"""
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. 
   Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента 
   — номер товара и словарь с параметрами, то есть характеристиками товара: название, цена, 
   количество, единица измерения. Структуру нужно сформировать программно, запросив все 
   данные у пользователя.
"""

products = [(1, {'название': 'компьютер', 'цена': 30000, 'количество': 5, 'eд': 'шт.'}),
            (2, {'название': 'принтер', 'цена': 15000, 'количество': 2, 'eд': 'шт.'}), 
            (3, {'название': 'сканер', 'цена': 7000, 'количество': 7, 'eд': 'шт.'}),
            (4, {'название': 'монитор', 'цена': 10000, 'количество': 4, 'eд': 'шт.'})]


def analytics():
    analytics_dict = {}

    for dict in products:
        for key, value in dict[1].items():
            if analytics_dict.get(key) is None:
                analytics_dict[key] = []
            if value not in analytics_dict.get(key):
                analytics_dict[key].append(value)

    for key, value in analytics_dict.items():
        print(f'{key}: {value}')


def add_product():
    data = {}
    fields = ('name', 'price', 'number', 'unit')
    for field in fields:
        data[field] = input(f'Введите {field}: ')

    if data['name'].isalpha() and data['price'].isdigit() and \
       data['number'].isdigit() and data['unit'].isalpha():
        products.append((len(products) + 1, {'название': str(data['name']), 
                                             'цена': float(data['price']), 
                                             'количество': int(data['number']), 
                                             'eд': str(data['unit'])}))
        print('Товар добавлен.')
    else:
        print('Не корректно заданы параметры товара.')
        return 


menu = (f'====================================\n'
        f'1. Добавить новый товар - add\n'
        f'2. Показать таблицу товаров - pshow\n'
        f'3. Показать аналитику товаров - ashow\n'
        f'4. Показать меню - menu\n'
        f'5. Выйти из пограммы - exit\n'
        f'====================================')

key = 0
print(menu)
while key != 'exit':
    key = input('Введите комманду # ')

    if key == 'add':
        add_product()
    elif key == 'pshow':
        for product in products:
            print(product)
    elif key == 'ashow':
        analytics()
    elif key == 'menu':
        print(menu)
    elif key == 'exit':
        print('Выход из программы.')
    else:
        print('Не верная команда.')
