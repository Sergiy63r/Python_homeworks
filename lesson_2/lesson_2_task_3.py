from math import ceil


def square(a, b):
    return ceil(a*b)


a = float(input('Введите первую сторону квадрата: '))
b = float(input('Введите вторую сторону квадрата: '))


print(f'Площадь квадрата округленная в большую сторону - {square(a,b)}')
