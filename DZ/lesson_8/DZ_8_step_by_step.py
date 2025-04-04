# DZ_8_step by step
import math

"""
DZ_8 Задача
Разработка программы для подсчета площадей фигур с помощью написания функций 

"""


# a_ = side_a
# b_ = side_b
# c_ = side_c
# def area_triangle(a_: float, b_: float, c_: float) -> (float or str):


def area_triangle(a_, b_, c_='1.52') -> (float or str):
    try:
        a_ = float(a_)
        b_ = float(b_)
        c_ = float(c_)
        if a_ + b_ > c_ and a_ + c_ > b_ and b_ + c_ > a_:
            p_ = (a_ + b_ + c_) / 2  # p — полупериметр треугольника
            s_ = math.sqrt(p_ * (p_ - a_) * (p_ - b_) * (p_ - c_))  # формула Герона
            area_ = round(s_, 2)  # Округление до 2- знаков
            return f"Площадь треугольника составляет: {area_}"
        elif a_ <= 0 or b_ <= 0 or c_ <= 0:
            return (
                "Значения сторон не могут быть отрицательными или нулевыми. "
            )
        else:
            return (
                "Одна сторона треугольника больше суммы двух других сторон. "
                "Такой треугольник не может существовать."
            )
    except ValueError:
        return (
            "Ошибка при вводе параметров сторон!!!\n"
            "Перезапустите программу и введите целое или натуральное число \n"
            # "с использованием разделителя \".\" (точки)."
        )


a = input("Введите сторону a = ")
b = input("Введите сторону b = ")
c = input("Введите сторону c = ")

# area = area_triangle(a, b, c)
print(area_triangle(a, b, c))
# print("Площадь треугольника составляет:\t\t\n ", area)


#
# try:
#     fig = int(input(
#         "Выберите фигуру для вычисления её площади.\nВведите - 1, если выбрали треугольник,"
#         "\nВведите - 2, если выбрали прямоугольник,\nВведите - 3, если выбрали круг. "
#         "\nВведите цифру: ")
#     )
#     if fig == 1:
#         print("Вы выбрали треугольник")
#
#
#     elif fig == 2:
#         print("Вы выбрали прямоугольник")
#         a = float(input("Введите сторону a = "))
#         b = float(input("Введите сторону b = "))
#         S = a * b
#         print("Площадь прямоугольника составляет: ", round(S, 2))
#     elif fig == 3:
#         print("Вы выбрали круг")
#         r = float(input("Введите радиус круга r = "))
#         S = math.pi * r ** 2
#         print("Площадь круга составляет: ", round(S, 2))
#     else:
#         print("Предлагается выбрать только одну из трёх цифр (1, 2 или 3)")
# except ValueError:
#     print("Ошибка!!! Пожалуйста перезапустите программу и введите только цифру.")
#     print("При вводе длин сторон укажите целое или натуральное число.")
