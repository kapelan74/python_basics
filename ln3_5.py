"""
5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. 
   При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить 
   ввод чисел, разделённых пробелом и снова нажать Enter. Сумма вновь введённых 
   чисел будет добавляться к уже подсчитанной сумме.
   Но если вместо числа вводится специальный символ, выполнение программы завершается. 
   Если специальный символ введён после нескольких чисел, то вначале нужно добавить 
   сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""

def add_of_numbers(nums):
    try:
        nums_list = list(map(int, nums))
        return sum(nums_list)
    except ValueError:
        print('Введены не корректные данные.')
        return 0


def main():
    result = 0
    nums = []
    while 'q' not in nums:
        nums = input('Введите строку чисел, разделенных пробелом (q - выход): ').split(' ')
        if 'q' in nums and len(nums) == 1:
            print('Выхожу из программы.')
            break
        elif 'q' in nums and len(nums) > 1:
            nums.remove('q')
            result += add_of_numbers(nums)
            print(f'Сумма: {result} Выхожу из программы.')
            break
        else:
            result += add_of_numbers(nums)
            print(f'Сумма: {result}')


main()