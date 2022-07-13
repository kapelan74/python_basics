"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. 
   Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве 
   делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class ZeroDivErr(Exception):
    err_text = 'Ошибка деления на ноль.'

    def __str__(self):
        return self.err_text


class DivNums(float):
    def __truediv__(self, other):
        if other == 0:
            raise ZeroDivErr

        return DivNums(float(self) / float(other))


while True:
    try:
        num1 = DivNums(input("Введите делимое: "))
        num2 = DivNums(input("Введите делитель: "))
        print(num1 / num2)
    except ZeroDivErr as err:
        print(err)
    except ValueError:
        print('Ошибка ввода данных.')
        break


    
