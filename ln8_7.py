"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». 
   Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу 
   проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните сложение 
   и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""

class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return (f'Сумма z1 и z2 равна\n' 
                f'{float(self.a + other.a)} + {float(self.b + other.b)} j')

    def __mul__(self, other):
        return (f'Произведение z1 и z2 равно\n' 
                f'{float(self.a * other.a - self.b * other.b)} + {float(self.b * other.a + self.a * other.b)} j')

    def __str__(self):
        return f'z = {float(self.a)} + {float(self.b)} j'


z1 = ComplexNum(5, -8)
z2 = ComplexNum(9, 3)

print(z1)
print(z1 + z2)
print(z1 * z2)