"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. 
   Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 36969.
"""

# вариант 1
num = input('Введите число: ')
print(int(num) + int(num + num) + int(num + num + num))

# вариант 2
num = int(input('Введите число: '))
result = num + int(f'{num}{num}') + int(f'{num}{num}{num}') 
print(result)