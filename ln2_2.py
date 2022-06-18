"""
2. Для списка реализовать обмен значений соседних элементов. 
   Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д. 
   При нечётном количестве элементов последний сохранить на своём месте. 
   Для заполнения списка элементов нужно использовать функцию input().
"""

def values_exchange(elements):
   elem_list = elements.split(' ')
   elem_count = len(elem_list)
   enum = 0
   for elem in range(0, int(elem_count/2)):
      elem_list[enum], elem_list[enum + 1] = elem_list[enum + 1], elem_list[enum]
      enum += 2

   print(elem_list)


values_exchange(input('Введите список элементов через пробел:'))


