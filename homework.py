# 1.Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# number = int(input('Введите день недели: '))
# if number == 1:
#     print('нет')
# elif number == 2:
#     print('нет')
# elif number == 3:
#     print('нет')
# elif number == 4:
#     print('нет')
# elif number == 5:
#     print('нет')
# elif number == 6:
#     print('да')
# elif number == 7:
#     print('да')
# else:
#     print('ошибка')

# 2.Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             print(f'Для значения {x}, {y}, {z} истинность выражения является --> 'f'{not(bool(x) or bool(y) or bool(z)) == (not(bool(x)) and not(bool(y)) and not(bool(z)))}')

# 3.Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4 -> 1
# x=-34; y=-30 -> 3

# number_x = int(input('Введите координаты X: '))
# number_y = int(input('Введите координаты Y: '))

# if number_x != 0 and number_x > 0 and number_y != 0 and number_y > 0:
#     print('1')
# elif number_x != 0 and number_x < 0 and number_y != 0 and number_y > 0:
#     print('2')
# elif number_x != 0 and number_x < 0 and number_y != 0 and number_y < 0:
#     print('3')
# elif number_x != 0 and number_x > 0 and number_y != 0 and number_y < 0:
#     print('4')

# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# quarter = int(input('Введите номер четверти: '))

# if quarter == 1:
#     print(f'Диапазон возможных координат точек в {quarter} четверти - > x > 0 и y > 0')
# elif quarter == 2:
#     print(f'Диапазон возможных координат точек в {quarter} четверти - > 3x < 0 и y > 0')
# elif quarter == 3:
#     print(f'Диапазон возможных координат точек в {quarter} четверти - > x < 0 и y < 0')
# elif quarter == 4:
#     print(f'Диапазон возможных координат точек в {quarter} четверти - > x > 0 и y < 0')
# else:
#     print('Такой четверти нет')

# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве (НЕОБЯЗАТЕЛЬНО, ПО ЖЕЛАНИЮ: найти растояние в 3D пространстве)
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

# import math

# x1 = float(input("Введите x1: "))
# y1 = float(input("Введите y1: "))
# x2 = float(input("Введите x2: "))
# y2 = float(input("Введите y2: "))

# formula = math.sqrt((x2-x1)**2+(y2-y1)**2)
# print(f'Расстояние в 2D пространстве между точками А({x1}, {y1}) и В({x2}, {y2}) -> {formula}')