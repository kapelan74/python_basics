"""
4. Представлен список чисел. Определите элементы списка, не имеющие повторений. 
   Сформируйте итоговый массив чисел, соответствующих требованию. Элементы 
   выведите в порядке их следования в исходном списке. Для выполнения задания 
   обязательно используйте генератор.
"""

def main(num_list):
   return [num for num in num_list if num_list.count(num) == 1]


print(main([2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]))
