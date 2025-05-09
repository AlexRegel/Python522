# 1-й вариант Д/З: Расчёт площади прямоугольного параллелепипеда
# с рёбрами a, b, c. Вариант с урока.
def rect_paral_1(a, b, c):
    def inner(i, j):
        return i * j

    s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
    return s


print(rect_paral_1(2, 4, 6, ))
print(rect_paral_1(5, 8, 2, ))
print(rect_paral_1(1, 6, 8, ))
print()


# # 2-й вариант Д/З - с использованием глобальных переменных

def rect_paral_2():  # Для этой функции определены глобальные переменные
    global a, b, c

    def inner(i, j):
        return i * j

    s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
    return s


a = 2
b = 4
c = 6
print(rect_paral_2())
a = 5
b = 8
c = 2
print(rect_paral_2())
a = 1
b = 6
c = 8
print(rect_paral_2())
print()


# 3-й вариант Д/З - с использованием нелокальных переменных


def rect_paral_3(a, b, c):  # Для этой функции используется работа с нелокальными переменными
    sh = 0  # Задан счётчик обращений к функции inner()

    def inner():  # i, j присваиваютса занчения a, b, c в зависисмости от обращения
        nonlocal sh
        sh += 1
        # print("Использование inner", sh)
        if sh == 1:
            i = a
            j = b
            return i * j
        elif sh == 2:
            i = a
            j = c
            return i * j
        else:  # sh == 3:
            i = b
            j = c
            return i * j

    s = 2 * (inner() + inner() + inner())
    return s


print(rect_paral_3(2, 4, 6))
print(rect_paral_3(5, 8, 2))
print(rect_paral_3(1, 6, 8))
print()


# Hfp,jh pflfybz


def rect_paral_1(a, b, c):
    global s

    def inner(i, j):
        return i * j

    s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
    return s


s = 0
print(rect_paral_1(2, 4, 6, ))
print(rect_paral_1(5, 8, 2, ))
print(rect_paral_1(1, 6, 8, ))
print()


def rect_paral_1(a, b, c):
    s = 0

    def inner(i, j):
        nonlocal s
        s += i * j

    inner(a, b)
    inner(a, c)
    inner(b, c)

    return 2 * s


s = 0
print(rect_paral_1(2, 4, 6, ))
print(rect_paral_1(5, 8, 2, ))
print(rect_paral_1(1, 6, 8, ))
print()
