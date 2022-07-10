"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора 
   класса (метод __init__()), который должен принимать данные (список списков) 
   для формирования матрицы.

   Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
   Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов 
   класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
"""

class Matrix:
    
    def __init__(self, mdict):
        self.mdict = mdict

    def __str__(self):
        return '\n'.join([''.join(f'{i:4d}' for i in l) for l in self.mdict]) + '\n'

    def __add__(self, other):
        if len(self.mdict) == len(other.mdict) and \
            len(self.mdict[0]) == len(other.mdict[0]):
            self.mdict = [[self.mdict[i][j] + other.mdict[i][j] 
                                for j in range(len(self.mdict[0]))] 
                                        for i in range(len(self.mdict))]

            return self.__str__()
        else:
            return 'Нельзя складывать матрицы разных размеров!'


matr1 = Matrix([[31, 32, 2], [37, 43, 23], [51, 86, -90]])
matr2 = Matrix([[3, 5, 32], [2, -43, 6], [-1, 64, -8]])
matr3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])

for mtx1 in (matr1, matr2, matr3):
    for mtx2 in (matr1, matr2, matr3):
        print('#' * 30)
        print(f'{mtx1}\n+\n{mtx2}\n=')
        print(mtx1.__add__(mtx2))


