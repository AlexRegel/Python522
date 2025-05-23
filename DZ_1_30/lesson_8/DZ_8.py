# DZ_8
from math import pi
"""
DZ_8 Задача
Разработка программы для подсчета площадей фигур с помощью написания функций. 
"""
try:
    fig = int(input(
        "Выберите фигуру для вычисления её площади.\nВведите - 1, если прямоугольник;"
        "\nВведите - 2, если треугольник;\nВведите - 3, если выбрали круг."
        "\nВведите цифру: ")
    )
    if fig == 1:
        print("Вы выбрали прямоугольник")

        def rectangle_area(a_, b_):  # Создание функции для прямоугольника
            try:
                a_ = float(a_)
                b_ = float(b_)
                if a_ > 0 and b_ > 0:
                    s_ = a_ * b_
                    return f"Площадь прямоугольника составляет: {round(s_, 2)}"
                else:  # a_ <= 0 or b_ <= 0
                    return (
                        "Значение сторон не может быть отрицательным или нулевыми."
                    )
            except ValueError:
                return (
                    "Ошибка при вводе параметров прямоугольника!!!\n"
                    "Перезапустите программу и введите целое или натуральное число."
                )

        print(rectangle_area(input("Введите сторону a = "),
                             input("Введите сторону b = ")))
    elif fig == 2:
        print("Вы выбрали треугольник")

        def area_triangle(a_='1', h_='1'):  # Создание функции для треугольника
            try:  # Исключение на случай неверного ввода данных
                a_ = float(a_)  # основание треугольника
                h_ = float(h_)  # его высота
                if a_ > 0 and h_ > 0:
                    s_ = 0.5 * a_ * h_
                    return f"Площадь треугольника составляет: {round(s_, 2)}"
                else:  # a_ <= 0 or h_ <= 0
                    return (
                        "Значения высоты или основания не могут быть \n"
                        "отрицательными или нулевыми."
                    )
            except ValueError:
                return (
                    "Ошибка при вводе параметров треугольника!!!\n"
                    "Перезапустите программу и введите целое или натуральное число."
                )

        print(area_triangle(input("Введите основание a = "),
                            input("Введите высоту h = ")))
    elif fig == 3:
        print("Вы выбрали круг")

        def area_circle(r_):
            try:
                r_ = float(r_)  # радиус круга
                if r_ > 0:
                    s_ = pi * r_ ** 2   # math.
                    return f"Площадь круга составляет: {round(s_, 2)}"
                else:  # (r_ <= 0)
                    return (
                        "Значение радиуса не может быть "
                        "отрицательным или нулевым."
                    )
            except ValueError:
                return (
                    "Ошибка при вводе радиуса!!!\n"
                    "Перезапустите программу и введите целое или натуральное число."
                )
        print(area_circle(input("Введите радиус круга r = ")))
    else:
        print("Предлагается выбрать только одну из трёх цифр (1, 2 или 3)")
except ValueError:
    print("Ошибка!!! Пожалуйста перезапустите программу и введите только одну цифру.")

