"""
2. Создать текстовый файл (не программно), сохранить в нём несколько 
   строк, выполнить подсчёт строк и слов в каждой строке.
"""

import random

# Эмулятор не программного создания текстового файла
def file_gen():
   data = ['Python', 'can', 'be', 'easy', 'to', 'pick', 'up', 'whether', 
           'you', 'are', 'a', 'first', 'time', 'programmer', 'or', 'you', 
           'are','experienced', 'with', 'other', 'languages']
   
   with open('ln5_2.txt', 'w') as file:
      for _ in range(random.randrange(5, 15)):
         line = ' '.join([random.choice(data) for _ in range(random.randrange(1, 5))])
         file.write(line + '\n')


def text_counter():

   with open('ln5_2.txt', 'r') as file:
      line_count = 0
      word_count = 0
      for num, line in enumerate(file):
         words = len(line.split())
         print(f'Количество слов в строке {num + 1} = {words}')
         line_count += 1
         word_count += words

      print(f'Всего строк: {line_count}\nВсего слов: {word_count}')


file_gen()
text_counter()