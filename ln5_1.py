"""
1. Создать программный файл в текстовом формате, записать в 
   него построчно данные, вводимые пользователем. Об окончании 
   ввода данных будет свидетельствовать пустая строка.
"""

def text_writer():

    file = open('ln5_1.txt', 'w')
    print("Вводите текст:")
    
    while True:
        new_line = str(input(f'- '))
        if new_line:
            file.write(new_line + "\n")
        elif not new_line:
            print('Выход.')
            break

    file.close()


text_writer()