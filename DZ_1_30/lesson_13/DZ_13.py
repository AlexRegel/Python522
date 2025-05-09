from math import pi
"""
Создать лямбда-выражения для нахождения площадей фигур
"""
# Вариант через переменную словаря с функцией lambda, с последующей распаковкой
dct_figure = {"Окружность": (lambda r: pi * r ** 2)(2),
              "Прямоугольник": (lambda a, b: a * b)(10, 13),
              "Трапеция": (lambda a, b, h: ((a + b) / 2) * h)(7, 5, 3)}

print(dct_figure)
print()
for figure, s in dct_figure.items():  # Распаковка словаря
    print(figure, ": ", s, sep="")

print()
# Вариант непосредственного вывода словаря с функцией lambda
print(
    {"Окружность": (lambda r: pi * r ** 2)(2),
     "Прямоугольник": (lambda a, b: a * b)(10, 13),
     "Трапеция": (lambda a, b, h: ((a + b) / 2) * h)(7, 5, 3)}
)
