"""
4. Пользователь вводит целое положительное число. 
   Найдите самую большую цифру в числе. Для решения используйте цикл 
   while и арифметические операции.
"""

# вариант 1
num = int(input('Введите число: '))
max_num = 0

while num >= 1:
    d = num % 10
    num //= 10
    if d > max_num:
        max_num = d 

print(max_num)

# вариант 2
num = int(input('Введите число: '))

line = str(num)
num_list = list(map(int, line))
max_num = max(num_list)

print(max_num)
