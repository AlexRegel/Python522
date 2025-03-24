from math import sqrt, pi

# print("Вы выбрали треугольник")
#         a = float(input("Введите сторону a = "))
#         b = float(input("Введите сторону b = "))
#         c = float(input("Введите сторону c = "))
#         if a + b > c and a + c > b and b + c > a:
#             print(a + b > c and a + c > b and b + c > a)
#             p = (a + b + c) / 2  # p — полупериметр треугольника
#             S = sqrt(p * (p - a) * (p - b) * (p - c))  # воспользовались формулой Герона # sqrt()
#             print("Площадь треугольника составляет: ", round(S, 2))

# print("Вы выбрали круг")
# r = float(input("Введите радиус круга r = "))
# S = pi * r ** 2
# print("Площадь круга составляет: ", round(S, 2))
#
# print("Вы выбрали прямоугольник")
# a = float(input("Введите сторону a = "))
# b = float(input("Введите сторону b = "))
# S = a * b
# print("Площадь прямоугольника составляет: ", round(S))
#
#
# print("Вы выбрали трапецию")
# a = float(input("Введите оcнование a = "))
# b = float(input("Введите оcнование b = "))
# h = float(input("Введите высоту h = "))
#
# S = ((a + b) / 2) * h
# print("Площадь трапеции составляет: ", round(S))


lst1 = [2, 8, 12, - 5, -10]
lst2 = [12, -5, 2, -10, 8]

print(dict(map(lambda x, y: (x, y), lst1, lst2)))  # Словарь
print(list(map(lambda x, y: (x, y), lst1, lst2)))  # Список картежей
print(list(map(lambda x, y: [x, y], lst1, lst2)))  # Список списков
print()

# print(dict(map((lambda r: ("Окружность: ", pi * r ** 2)),
#                (lambda x, y: (x, y), lst1, lst2),
#                (lambda x, y: (x, y), lst1, lst2),
# )))  # Словарь

# a = float(input("Введите сторону a = "))
# r = float(input("Введите радиус r = "))

dct_figure = {"Окружность": (lambda r: pi * r ** 2)(float(input("Введите радиус r = "))),
              "Прямоугольник": (lambda a, b: a * b)(int(input("Введите сторону a = ")), int(input("Введите сторону b = "))),
              "Трапеция": (lambda a, b, h: ((a + b) / 2) * h)(7, 5, 3)}

print(dict(dct_figure))
print()
for figure, s in dct_figure.items():  # Распаковка словаря
    print(figure, ": ", s, sep="")

print()
print({"Окружность": (lambda r: pi * r ** 2)(2),
       "Прямоугольник": (lambda a, b: a * b)(10, 13),
       "Трапеция": (lambda a, b, h: ((a + b) / 2) * h)(7, 5, 3)})
