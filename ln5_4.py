"""
4. Создать (не программно) текстовый файл со следующим содержимым:
   One — 1
   Two — 2
   Three — 3
   Four — 4
   Напишите программу, открывающую файл на чтение и считывающую построчно данные. 
   При этом английские числительные должны заменяться на русские. Новый блок строк 
   должен записываться в новый текстовый файл.
"""

# Эмулятор не программного создания текстового файла
def file_gen():
   data = ['One - 1', 'Two - 2', 'Three - 3', 'Four - 4',
           'Five - 5', 'Six - 6', 'Seven - 7', 'Eight - 8']
   
   with open('ln5_4.txt', 'w') as file:
      for line in data:
         file.write(line + '\n')


def file_changer():
   rus = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре',
           5: 'Пять', 6: 'Шесть', 7: 'Семь', 8: 'Восемь'}

   new_data = []
   with open('ln5_4.txt', 'r') as file:
      for line in file:
         line = line.split()
         num = int(line[2])
         new_data.append(f'{rus[num]} - {num}')

   with open('ln5_4_new.txt', 'w') as n_file:
      for line in new_data:
         n_file.write(line + '\n')


file_gen()
file_changer()