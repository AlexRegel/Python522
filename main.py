# -- coding: utf8 --.

# name = "admin"
# print("Hello", name)
# age = 20.2
# print(age)
#
# print(type(name))
# print(id(name))
# print(type(age))
# print(id(age))
# import locale

# a = b = c = 10
# a, b, c = 5, "Hello", 7.2
# print(a)
# print(b)
# print(c)

# name = "admin"
# print(name)

# import keyword
# print(keyword.kwlist)

# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# a = 5
# print(a)
# a = "Hel"
# print(a)

# a = 5
# b = 20
# print("a:", a)
# print("b:", b)
#
# c = a # 1
# a = b # 2
# b = c # 1
#
# print("a:", a)
# print("b:", b)

# print("строка \nсимволов")
# print('\tстрока \nсимволов')
# print('строка символов строка символов строка символов'строка символов'строка символов'строка символов'строка символов'строка символов'строка символов'строка символов'строка символов'строка символов'строка символов'строка символов'строка символов'строка символов'строка символов'строка символов'строка символов'строка символов строка символов строка символов'строка символов'строка символов'строка символов'строка символов'строка символов'строка символов'строка символов'строка символов'строка символов'строка символов'строка символов'строка символов'строка символов'строка символов'строка символов'строка символов'строка символов'строка символов'строка символов'')


# Урок 2

# a = 5
# b = 20
#
# print("a:", a)
# print("b:", b)
#
# a = a + b #3
# b = a - b #1
# a = a - b #2
#
# print("a:", a)
# print("b:", b)

# print("Документ \"tile.txt\" находится по пути \rD:\\person\\file.txt")

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", " + s2 + "!\t\t" # конкатенация: сложение строк
# print(s3)
# s4 = s3 * 3
# print(s4)

# print(6 + 2)
# print(6.2 + 2.4)
# print(6 - 2)
# print(6 * 2)
# print(7 / 2)
# print(6 / 2)
#
# print(7 // 2)
# print(6 // 2)
#
# print(6 ** 2)
# print(7 % 2)
# print("-------------------")
#
# a = 5
# b = 7
# c = 3
#
# print((5 + 7 + 3) / 3)

# number = 6 + 4 * 5 ** 2 + 7
# print(number)

# a = 5 # оператор "=" это  оператор присваивания
# a += 3 # a = a + 3
# print(a)
# a -= 3 # a = a - 3
# print(a) # 5
# a *= 4 # a = a * 4
# print(a) # 20

# num = 4321
# print("Исходное число:", num)
# a = num % 10
# print("a:", a)
# num = num // 10
# print("num:", num)
# b = num % 10
# print("b:", b)
# num = num // 10
# print("num:", num)
# c = num % 10
# print("c:", c)
# num = num // 10
# print("num:", num)
# d = num % 10
# print("d:", d)
# print("Обратное число:", a * 1000 + b * 100 + c * 10 + d)

# res = num % 10 * 1000
# num //= 10
# res += num % 10 * 100 # 200 res = res + num % 10 * 100
# num //= 10
# res += num % 10 * 10
# print("Обратное число:", res)

# num1 = "2"
# num2 = 3
# res = int(num1) + num2
# print(res)
# Либо
# res = num1 + str(num2)
# print(res)

# print(int(3.981))
# print(type(round(3.481)))
# print(type(round(3.481, 2))) # 2 - два символа после запятой
# print(round(3.699, 2)) # 2 - два символа после запятой с нулём, который не выводится

# num1 = "2.5"
# num2 = 10
# res = float(num1) + num2 # 2.5 + 10
# print(res)

# name = "Виктор"
# age = 20
# print("Меня зовут", name, ". мне", age, "лет.")
# print("Меня зовут " + name + ". мне " + str(age) + " лет.")
# print("Меня зовут ", name, ". мне", age, " лет.", sep="", end=" ")
# print("Hello Python")

# name = input("Введите имя: ")
# print("Hello,", name)

#
# num1 = int(input("Введите число 1: "))
# num2 = int(input("Введите число 2: "))
# num3 = int(input("Введите число 3: "))
# num4 = int(input("Введите число 4: "))
# sum_1 = num1 + num2
# sum_2 = num3 + num4
# res = sum_1 / sum_2
# print(round(res, 3))

# b1 = True
# b2 = False
# print(int(b1)) # 1
# print(int(b2)) # 0
# print(type(b1))
# print(type(b2))
#
# print(b1 + 5) # 1 + 5
# print(b2 + 5) # 0 + 5

# print(bool(" "))
# print(bool(0))
# print(bool(True))
# print(bool(False))
# print(bool(None))

#
# test = None
# test = 5
# print(test)
# print(type(test))
#
# print(5 == 5)
# print(2 + 5 != 3 + 4)  # 7 == 7
# print(8 >= 8)  #
# print(5 <= 5)  #
# print("hello" > "Hello")  # 104 > 72
#
# print("hello" == "hello")  #
# print("------------------")  #
# print(2 < 4 < 9)  # True: True => True
# print(2 > 4 < 9)  # Folse: True => True
# print(2 * 5 > 7 >= 2)
#
# print("строка символов строка символов строка символов строка символов строка символов \
#  строка символов строка символов строка символов строка символов строка символов строка символов строка символов \
#  строка символов строка символов"
#       "")


# print(5 - 3 == 2 and 1 + 3 == 4)  # 5 - 3 == 2 and 1 + 3 == 4
# print(5 - 3 == 2 and 1 + 3 < 4)  # True and False => False
# print(5 - 3 > 2 and 1 + 3 == 4)  # True and False => False
# print(5 - 3 > 2 and 1 + 3 < 4)  # True and False => False


# print(5 - 3 == 2 or 1 + 3 == 4)  # 5 - 3 == 2 and 1 + 3 == 4 => True
# print(5 - 3 == 2 or 1 + 3 < 4)  # True and False => True
# print(5 - 3 > 2 or 1 + 3 == 4)  # True and False => True
# print(5 - 3 > 2 or 1 + 3 < 4)  # True and False => False

# print(not 9 - 5)  # not True => False
# print(not 7 - 7)  # not False => True

# a = 5
# b = 10
# if a > b:
#     print(a, " > ", b)
# if b > a:
#     print(b, " > ", a)
# if b == a:
#     print(b, " == ", a)

# cnt = 15
# if cnt < 10:
#     cnt = cnt + 1
# else:
#     cnt = cnt - 1
# print(cnt)

# a = 60
# b = 40
# if a > b:
#     print(a, " > ", b)
# if b == a:  #
#     print(b, " == ", a)
# else:
#     print(b, " > ", a)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешён")
#     print("Приятного просмотра")
# else:
#     print("Доступ запрещён")

# a = input("Введите первую сторону: ")
# b = input("Введите вторую сторону: ")
# c = input("Введите третию сторону: ")
#
# if a == b == c:
#     print("Тругольник равносторонний")
# elif a == b or a == c or b == c:
#     print("Тругольник равнобедренный")
# else:
#     print("Тругольник разносторонний")

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5)
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("Понедельник")
#     if day == 2:
#         print("Вторник")
#     if day == 3:
#         print("Среда")
#     if day == 4:
#         print("Четверг")
#     if day == 5:
#         print("Пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("Суббота")
#     if day == 7:
#         print("Воскресенье")
# else:
#     print("Такого дня не существует")


# month = int(input("Введите месяц (цифрой): "))
# if (month >= 1) and (month <= 2) or (month == 12):  # (day >= 1) and (day <= 5)
#     print("Зима")
# if (month >= 3) and (month <= 5):
#     print("Весна")
# if (month >= 6) and (month <= 8):
#     print("Лето")
# if (month >= 9) and (month <= 11):
#     print("Лето")
# if (month < 1) or (month > 12):
#     print("Такого месяца не существует")

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", end=" ")
#     if n == 1:
#         print(n, "ворона")
#     if 2 <= n <= 4:
#         print(n, "вороны")
#     if 5 <= n <= 9 or n == 0:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода данных")


# n = int(input("Введите количество ворон (0 - 9): "))
# if 0 <= n <= 9:
#     print("На ветке", end=" ")
#     if n == 1:
#         print(n, "ворона")
#     elif 2 <= n <= 4:
#         print(n, "вороны")
#     else:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода данных")

#
# match выражение:
#     case шаблон_1:
#         действие_1
#     case шаблон_2:
#         действие_2
#     case _:
#         действие по умолчанию

# password = "qwerty"
#
# match password:
#     case 'admin':
#         print("Администратор")
#     case 'user':
#         print("Пользователь")
#     case _:
#         print("Пароль не верен")


# day = 'понедельник'
# time = 11
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 12 or 14 <= time <= 17:
#         print("рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("выходной день")
#     case _:
#         print("Такого дня недели не существует или не рабочее время")


# a, b = 10, 20
#
# print(a if a < b else b)
#
# a, b = 20, 35
# print("a == b" if a == b else "a > b" if a > b else "b > a")

#
# a = None
# print(a)
# print(type(a))


# a = 5
# b = 0
# print(a / b)

# try:    # попытаться выполнить
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
#     # print(type(n / m))
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки или Нельзя делить на ноль")
# else:  # когда в блоке try не возникло исклл
#     print("Всё нормально. Вы ввели числа", n, "и", m)
# finally:  # Выполняется в любом случае
#     print("Конец программы")

# try:
#     a = int(input("Введите значение 1: "))
#     b = int(input("Введите значение 2: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки или Нельзя делить на ноль")

#
# n = input("Введите значение 1: ")
# m = input("Введите значение 2: ")
# try:
#     n = int(n)  # 10
#     m = int(m)  #
# except ValueError:
#     n = str(n)  # ...
# finally:
#     print(n + m)

# Циклы

# while условие:
#     блок_инструкции

# i = 0   # счётчик
# while i < 5: # условие
#     print("i =", i)
#     i += 1 # изменение счётчика
#
# итерация - один шаг цикла

# i = 10   # счётчик
# while i > 0:
#     print("i =", i)
#     i -= 1

# i = 0   # счётчик
# while i <= 20:
#     if i % 2 == 0: #  чётные
#     # if i % 2 != 0: #  нечётные,  i % 2 == 1
#     # if i % 2:
#         print(i, end=" ")
#     i += 1

# i = 10 % 7  #
# print(i)
# print(10 % 7 == 3 % 7)

# n = int(input("Количество символов: "))
# # print("*" * n)
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1


# n = int(input("Количество символов: "))
# i = 0
# while i < n:
#     if i % 2 == 0:
#         print("+", end="")
#     else:
#         print("-", end="")
#     i += 1


# n = int(input("Количество символов: "))
# i = 0
# while n > 0:
#     print("*", end="")
#     n -= 1

# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# res = 0
# while a <= b:
#     if a % 2:
#         print(a, end=" ")
#         res += a
#     a += 1
# print("\nСумма: ", res)

# n = input("Введите целое число: ")  # 'пять'
#
# while type(n) is not int: # type(n) != int
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Чётное")
# else:
#     print("Нечётное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue # прирвёт текущую операцию цикла и перейдёт на следующую
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершён")


# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break  # Цикл работает пока пользователь не введёт отрицательное число


# Два способа:
# print('Документ "file.txt" находится\n\t по пути D:\\person\\file.txt')
# print("Документ \"file.txt\" находится по пути \rD:\\person\\file.txt")

# a = 3
# b = 8
# c = 12
# # Остались вопросы по занятию 2 по символу "\" и появляющимся в выводе скобкам:
# long_string = "Документ \"file.txt\" находится "\
#                "по пути: D:\\person\\file.txt", a, b, c, "вот так вот!!!"
# print(long_string)
#
# print("hello" > "heLlo")

# i = 0
# while i < 10:
#     if i == 5:
#         break  # до else не дойдёт
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)

# i = 0
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if j % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# for element in collection:
#     print(element)

# for i in "Hello!", "World":
#     print(i)

# range(start, stop, step=1)

# a = 10
# for i in range(0, a + 1, 1):  # range(0(низ), 8(верх), 2(шаг)):
#     print(i, end=" ")
#
# print()
#
# i = 0
# while i <= 10:
#     print(i, end=" ")
#     i += 1

# a = 10
# for i in range(0, a, 1):  # i=0(низ), i<10, i+=1, i>0, i-+1
#     print(i, end=" ")
#
# print()
#
# i = 1
# while i < 10:
#     print(i, end=" ")
#     i *= 2

# a = int(input("Введите целое число: "))
#
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(10, 100):
#     if i % 11 == 0:
#         print(i, end=" ")
#
# print()
#
# for i in range(11, 100, 11):
#     print(i, end=" ")
#
# print()
#
# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("Цикл закончен")

# for i in range(3):
#     print("+++")
#     for j in range(3):
#         print("--------")

# w = int(input("Введите ширину прямоугольника: ")) # 12
# h = int(input("Введите высоту прямоугольника: ")) # 4
#
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             [print("*", end="")]
#         else:
#             [print(" ", end="")]
#     print()

# letter = [i * 2 for i in "Hello"]
# print(letter)


# num = [i for i in range(30) if i % 2 == 0]
# print(num)
#
# for i in range(30):
#     if i%2 == 0:
#         print(i, end=", ")

# nums = [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
# print(nums)
# print(type(nums))
# print(nums[0])
# print(nums[1])
# print(nums[2])
# print(nums[10])
# print(nums[-1])
# print("Кол-во", len(nums))
# # print(nums[Len(nums)-1])
#
# nums[1] = 256
# nums[3] += 100
# print(nums)

# s = []
# print(s)
# print(type(s))
#
#
# t = list("Python")
# print(t)
# print(type(t))
#
# print(list(range(1, 18, 2)))

# a = [1, 3, 5, 7, 9]
# b = [11, 13, 15, 17]
# print(a + b)
# print(a * 3)

# a = [1, 3, 5, 7, 9]


# a = [0 for i in range(5)]
# print(a)


# a = [0 for _ in range(5)]
# print(a)

# a = [i for i in range(5)]
# print(a)

# n = 15
# a = [i ** 2 for i in range(2, n)]
# print(a)

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [int(input("-> ")) for i in range(int(input("Введите кол-во эл списка: ")))]
# print(a)

# lst = [9, 6, 3, 5]
# a = 0
# for i in range(len(lst)):  # 0 1 2 3
#     print(lst[i], end="\n")
#     if lst[i] <= 6:
#         a += lst[i]
#     print("i =", i, end="\n")
#     if i == len(lst)-1:
#         print("a =", a, end="\n")
#         print()
#     else:
#         print("a =", a, end="\n")
# print("a =", a, end=" ")
#
# print()
# print()
#
# lst = [9, 6, 3, 5]
# for v in lst:  # 9, 6, 3, 5
#     print(v, end=" ")


# n = list(range(21, 41))
# print(n)
# count = sum_ = 0  # sum -зарезервированная функция, поэтому добавляем подчёркивание
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         count += 1
#     else:
#         sum_ += n[i]
# print("Количество чётных элементов списка:", count)
# print("Сумма нечётных элементов списка", sum_)

# второй вариант (без индексов)
# n = list(range(21, 41))
# print(n)
# count = sum_ = 0  # sum -зарезервированная функция, поэтому добавляем подчёркивание
# for i in n:
#     if i % 2 == 0:
#         count += 1
#     else:
#         sum_ += i
#
# print("Количество чётных элементов списка:", count)
# print("Сумма нечётных элементов списка", sum_)


# a = [int(input("-> ")) for i in range(int(input("Введите кол-во эл списка: ")))]
# print(a)
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i], end=" ")
# print()
#
# for i in range(0, len(a), 2):
#     print(a[i], end=" ")

# a = [int(input("-> ")) for i in range(int(input("Введите кол-во эл списка: ")))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")
# c byltrcfvb nfrjq dfhbfyn yt hf,jnftn
# for i in a:
#     if i > i - 1:
#         print(i, end=" ")

# a = [9, 7, 8, 4, 2]
# print(a)
# a[0], a[1] = a[1], a[0]
# print(a)

# Срез

# список [start:stop:step]

# a = [9, 7, 8, 4, 2, 1, 3]
# print(a)
# print(a[1:4])
# print(a[5:])
# print(a[1:4:2])
# print(a[::-2])
# print()
# print(a[-1:0:-1])
# print(a[10:20])

# lst = list(range(1, 8))
# print(lst)

# a = [1, 2, 3, 4, 5, 6, 7]
# print(a)
# a[1:2] = [0, 0, 0, 0] # замена элементов в списке
# print(a)
# a[1:3] = [0, 0, 0, 0]
# print(a)
# # a[2] = [120, 24]
# # print(a)
# a[100:111] = [100, 102]
# print(a)
# print(a[9])
# print(len(a))

# Методы списка
# print(dir(list)) # dir - функция отображения набора методов
# print(dir(str)) # dir - функция отображения набора методов
# ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# s = [9, 7, 8, 4, 2, 1, 3]
# print(s)
# s.append(99)    # добавлячет элемент в конец списка
# print(s)
# s.extend([11, 12, 13])  # добавляем список элементов в конец списка
# print(s)
# s.insert(0, 100)  # Добавляет элемент (второй параметр) по зад. индексу (первый параметр)
# print(s)
# print()
# s.insert(-1, 5)
# print(s)

# s = []
# n = int(input("Кол-во элементов в списке: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     # s.append(x)
#     s.insert(0, x)  # [7, 8, 9]
# print(s)

# a = [5, 9, 2, 1, 4, 3]
# b = [4, 2, 1, 3, 7]
# c = []  # [2, 1, 4, 3]
#
# for i in a:  # 5
#     for j in b: # 4
#         if i in c: # Если i находится в списке c, продолжать следующей ите
#             continue
#         if i == j:  # 5 == 4
#             c.append(i)
#             break
# print(c)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
#
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33, 4, 2]
# c = []
#
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])  # если длины обоих списков одинаковы
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])  # если длины обоих списков одинаковы
#     for i in range(len(a), len(b)):
#         c.append(a[i])
#
# print(c)


# a = [1, 2, 3]
# b = [11, 22, 33, 4, 2]
# c = []
#
# if len(b) > len(a):
#     a, b = b, a
#
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])  # если длины обоих списков одинаковы
# for i in range(len(a), len(b)):
#     c.append(a[i])

# s = [9, 7, 8, 4, 2, 8, 1, 3]
# print(s)
# item = 18
# if item in s:
#     s.remove(8)  # Удаляет первое вхождение элемента по значению!
# print(s)
#
# # last = s.pop()  # удаляет последний элемент из списка
# # print(last)
# # print(s)
# #
# try:
#     second = s.pop(10)  # удаляет элемент по заданному индексу!
# except IndexError:
#     second = "Такого индекса нет"
# print(second)
# print(s)
#
# s.clear()   # Удаляет элементы их списка
# print(s)

# s = [9, 7, 8, 4, 2, 8, 1, 3]
# print(s)
#
# s[5:] = []
# print(s)
#
# del s[:]
# print(s)

# s = [9, 7, 8, 4, 2, 8, 1, 3, 8]
# print(s)
# # num = s.count(8)    # количество вхождений заданного элемента
# # print(num)
# ind = s.index(8, 3, 7)  # Ищет первое вхождение заданного элемента,
# # возвращает индекс, на котором нашёлся элемент, можно задать диапазон поиска.
# print(ind)

# a = 0b11
# b = 0b1011
# c = 0b100001
# print(a)    # 3 в десятичной системе
# print(b)    # 11 в десятичной системе
# print(c)    # 33 в десятичной системе

# m = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(m)
# for i in m:
#     if m.count(i) == 1:
#         print(i, end=" ")
# print()
# mas = [i for i in m if m.count(i) == 1]
# print(mas)
#
# a = [1, 2, 3]
# b = a.copy()
# print("a =", a, id(a))
# print("b =", b, id(b))
# b.append(20)
# print("a =", a)
# print("b =", b)
# a.append(100)
# print("a =", a, id(a))
# print("b =", b, id(b))


# m = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(m)
# # m.reverse()
# # print(m)
# m.sort(reverse=True)
# print(m)

# s = ["Виталий", "Сергей", "Александр", "Анна"]
# print(s)
# s.sort(key=len, reverse=True)
# print(s)

# m = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(m)
# m.sort(reverse=True) # Только со списками
# print(m)
# ...
# print()
# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# lst = sorted(s, reverse=True) # С разными типами данных работает (sorted)
# print("Lst:", lst)
# print(s)

# import random  # Генерация случайных чисел (модуль)

# print(random.random())
# print(random.randint(5, 10)) # Включает крайний (10)
# print(random.randrange(5, 10, 2)) # Не включает крайний (10)
# print(round(random.uniform(10.5, 25.2), 2)) # Не включает крайний (10)

# city_list = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
# s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# print(random.choice(city_list)) # Любой случайный элемент списка
# print(random.choice(s))
# print(random.choices(city_list, k=3)) # Любой случайный элемент в новый список
# print(random.choices(s, k=3))
# random.shuffle(city_list)    # Перетусовка
# print(city_list)

# import random  # Генерация случайных чисел (модуль)

# mas = [random.randint(50, 100) for i in range(5)]
# mas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# print(mas)
# print(len(mas))
# print(max(mas))
# print(min(mas))
# print(sum(mas))

# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# print(max(mas))
# a = max(mas)
# mas.remove(a)
# mas.insert(0, a)  # Добавляет элемент (второй параметр) по зад. индексу (первый параметр)
# print(mas)

# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
#
# min_ = min(mas)
# print("Min", min_)
#
# ind = mas.index(min_)
# print("Index min:", ind)
#
# del mas[:ind] # Удаление через срез
# print(mas)

# m = [
#     [1, 2, 3, 4], # 0
#     [5, 6, 7, 8], # 1
#     [9, 10, 11, 12] #  13, 14, 15, 16 # 2
# ]
# print(m)
# print(len(m))
# print(m[2][1])
#
# print("Вариант 1")
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
# print("Вариант 2")
# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end="\t")
#     print()

# m = ["Hello", "World", [44, [1, 2, 3], 55, ["Python"]]]
# print(m)
# print(m[1][2])
# print(m[2][1][1])
# print(m[2][3][0][3])

# import math
# import math as m
#
# print(m.sqrt(4))
# print(m.ceil(3.2)) # Округляем в большую сторону
# print(m.floor(3.8)) # в меньшую сторону

# from math import *
#
# print(sqrt(4))
# print(ceil(3.2)) # Округляем в большу сторону
# print(floor(3.8)) # в меньшую сторону

# from math import sqrt, ceil, floor

# print(sqrt(4)) # корень квадратный
# print(ceil(3.2)) # Округляем в большу сторону
# print(floor(3.8)) # в меньшую сторону

# print(list)

# import math
# print(dir(math))

# from math import pi
# # print(pi)
# radius = int(input("Введите радиус окружности: "))
# print("Длина окружности:", round(2 * radius * pi, 2))

# import time
# import locale

# print(time.time()) # c 1970 года Начало цифровой эпохи
# print(time.ctime()) # c 1970 года Начало цифровой эпохи
# print(time.ctime(739210084)) # По секундам определение времени
# res = time.localtime()
# print(res)
# print(res.tm_year, "-", res.tm_mon, "-", res.tm_mday, sep="")
# print(time.strftime("Today is %B %d, %Y"))
# print(time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime(739210084)))

# print(time.strftime("Today is %B %d, %Y"))
# locale.setlocale(locale.LC_ALL, "ru")
# print(time.strftime("Сегодня: %B %d, %Y"))
# a = 1_000_000
# print(a)

# start = time.time()
# print("Запуск программы")
# time.sleep(3)
# res = time.time() - start
# print("Программа выполнилась за", res, "сек.")

# Функции
# def hello(name, age):    # аргументы
#     print("Меня зовут:", name, "Мой возраст", age)
# #     Должно быть 2 пустых линии после определения функции
#
#
# hello("Irina", 20)  # параметры
# hello("Ivan", 21)


# def get_sum(a, b):  # Get_sum - не рекомендуется
#     print(a + b)
#
#
# x = 2 # лучше не писать а
# y = 5 # Лучше не писать b
# get_sum(x, y)
# get_sum("abc", "def")

# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
#
# symbol(9, "+", "-")
# symbol(7, "X", "0")


# def get_sum(a, b):  # Get_sum - не рекомендуется
#     print("Сумма:", end=" ")
#     c = a + b
#     return c
#     # print("Сумма:", end=" ")    # После return код будет недостижим и работать не нужно
#
#
# x = 2  # лучше не писать а
# y = 5  # Лучше не писать b
# res = get_sum(x, y)
# print(res)


# def maximum(one, two):  # Get_sum - не рекомендуется
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximum(9, 5))
# print(maximum(5, 15))

# def differ(a, b):
#     if a > b:
#         return a - b
#     elif a < b:
#         return a + b
#     else:
#         return "Значения равны"


# print(differ(9, 5))


# def cube(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))

# def change(lst):
#     end = lst.pop()
#     start = lst.pop(0)
#     lst.append(start)
#     lst.insert(0, end)
#     return lst   # lst end

#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))

# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst   # lst end
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))

# def one_big(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# if one_big(a, b):
#     print("Первое число больше второго")
# else:
#     print("Второе число больше первого")


# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if "a" <= ch <= "z":
#             has_lower = True
#         if "0" <= ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надёжный пароль")
# else:
#     print("Это ненадёжный пароль")


# def get_sum(a=5, b=1, c=0, d=1):  # Присвоение идёт с права на лево (a=5, b?, c=0, d=1)
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2, ))
# print(get_sum(1, 5, ))
# print(get_sum(1, 5, d=2, ))  # Последовательность перечисления не важна
# print(get_sum("C", "л", d="н", c="о"))  # Если в функции не указывать значения по умолчанию
# # подчёркивать не будет

# def set_param(count=20, symbol="-"):
#     print(symbol * count)
#
#
# set_param(10, "+")
# set_param(5, "*")
# set_param(15, "#")
# set_param(7)
# set_param()


# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Irina", 23)

# def display_info(name, age):
#     print("Hello", name)
#
#
# display_info("Irina", 23)
# display_info(23, "Irina")
# display_info(age=23, name="Irina")
# display_info("Igor", age=23, name="Irina")


# lt1 = "Hello"
# lt2 = "Hello"   # Одна ячейка, на которую ссыла.тся обе переменные
# print(lt1, id(lt1))
# print(lt2, id(lt2))
# print(lt1 == lt2)
# print(lt1 is lt2)
#
# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]    # Списки создают разные ячейки в памяти, поэтому - False
# print(lst1, id(lst1))
# print(lst2, id(lst2))
# print(lst1 == lst2)
# print(lst1 is lst2)


# lst1 = [1, 2, 3]
# print(lst1, id(lst1))
# lst1.append(4)  # Список это изменяемый тип данных
# print(lst1, id(lst1))
# lst1.pop(1)
# print(lst1, id(lst1))


# lt1 = "Hello"
# print(lt1, id(lt1))
# lt1 = lt1 + "!"
# print(lt1, id(lt1))

# Строка неизменяемый тип данных, т.е. если мы вводим новое значение, адрес меняется

# a = 5
# print(a, id(a))
# a = 7
# print(a, id(a))

# lt1 = "Hello"
# print(lt1, id(lt1))
# lt1 = lt1[5]    # Не реализуемо, т.к. вне диапазона
# print(lt1, id(lt1))
# lt1 = lt1[1:-1]
# print(lt1, id(lt1))


# Картеж (tuple)

# res = 10
# inner = 25
# def get_sum(a, b, c, d):
#     inner = 20
#     return a + b + c + d + res + inner
#
#
# print(get_sum(1, 5, 2, 7))
# # print(inner)    # Определена только внутри функции

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())
# lst[1] = 100
# print(lst)
# print(lst[1])
# # tpl[1] = 100
# print(tpl)

# a = ()
# print(a, type(a))
# b = tuple()
# print(b, type(b))

# a = 1, 2, 3, 4, 5, 6  # tuple
# print(a, type(a))

# b = tuple("Hello")
# print(b, type(b))
#
# print(b[1])
# print(b[1:3])

# s1 = tuple(input("->") for i in range(5))
# print(s1)

# from random import randint
#
# s1 = tuple(randint(50, 100) for i in range(5))
# print(s1)

# t1 = tuple("hello")
# t2 = tuple("world")
# print(t1)
# print(t2)
# t3 = t1 + t2
# # print(t3 * 2)
# print(t3)


# print(t3.count("l"))
# print(t3.index("l", 4, -2))

# print(dir(list))
# print(dir(tuple))

# v = "a"
# if v in t3:
#     print(t3.index(v))
# else:
#     print("Такого символа нет")
# print(t3.index("l", 4, -2))
# ...

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) == 1:
#             return tpl[tpl.index(el):]  # tpl[8:]    tpl[el:]
#         else:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1) + 1
#             return tpl[first:5]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# t = (10, "Python", True, [1, 2, 3], ["Hello", "world"])     # Можно изменять список
# print(t, id(t))
# t[4][0] = "new"
# print(t, id(t))
# print(len(t))
# t[4].append("hi")
# print(t, id(t))

# Распаковка картежей

# t = (1, 2, 3)  # , 4 - Количество элементов должно совпадать
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # Распаковка картежа
# # x, y, z = 1, 2, 3
# print(x, y, z)


# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married  # Если из функции возвращаяется > 1 значения, это картеж (всегда)
#
#
# user = get_user()
# print(user)
# first_name, year, married = user
# print(first_name, year, married)


# lst = [1, 2, 3, 4, 5, 6]    # Когда мы создали переменную, значения типа
# print(lst, type(lst))       # данных будет меняться в зависимости от того,
# tpl = tuple(lst)            # что мы туда будем присваивать
# print(tpl, type(tpl))
# lst2 = list(tpl)
# print(lst2, type(lst2))

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 3.326), ("Марсель", 1.6)))
# )
# print(countries, end="\n\n")
#
# for county in countries:
#     county_name, county_population, cities = county
#     print("\nСтрана: ", county_name, ", население: ", county_population, sep="")
#     for city in cities:
#         county_name, county_population = city
#         print("\tГород: ", county_name, ", население: ", county_population, sep="")

# print(county)

# 4647489674213456456
# Hello World
# tpl = tuple(input("Введите строку: "))
# print(tpl)
#
# lst = []
# for i in range(len(tpl)):
#     if tpl[i] not in lst:
#         lst.append(tpl[i])
#
# for i in range(len(lst)):
#     print("Количество", lst[i], "=", tpl.count(lst[i]))

# print(lst)


# Множество (set)
# Множество (set) - это неупорядоченный тип данных, без дубликатов данных

# s = {"red", "yellow", "green", "yellow", "green"}
# print(s, type(s))
# print(len(s))

# a = set("hello")
# print(a, type(a))

# s = {x * x for x in range(10)}
# print(s)

# lst = [1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 6]
# print(lst)
# num = set(lst)
# print(num)
# lst2 = list(num)
# print(lst2)

# t = {"red", "yellow", "green"}
# print("red" in t)
# print("blue" in t)
# for i in t:
#     print(i)


# lst = ['ab_1', 'ac_1', 'bc_1', 'bc_2']
# print({i for i in lst if 'a' in i})
# # print(['A' if i[0] == "a" else 'B' for i in lst])   # Тернарное выражение
# print(['A' + i[1:] if i[0] == "a" else 'B' + i[1:] for i in lst])
# # print({'A' + i[1:] if i[0] == "a" else 'B' + i[1:] for i in lst if i[1] == 'c'})
# print(tuple('A' + i[1:] if i[0] == "a" else 'B' + i[1:] for i in lst if i[1] == 'c'))

# a = {"red", "yellow", "green"}
# print(a)
# a.add("blue")
# print(a)
# # a.remove("yellow")
# # a.remove("black")    # KeyError
# color = "black"
# # if color in a:
# #     a.remove(color)
# # a.discard(color)
# # a.pop()
# a.clear()
# print(a)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a ^ b
# a ^= b
# print(a, c)
# c = a - b # {0}
# a -= b
# print(a) # {0}
# c = a.union(b)  # Вместо оперетора +
# c = a | b
# print(c)
# += -=
# a |= b
# print(a)
# print(b)
# c = a & b
# print(c)
# a &= b
# print(a) # {1, 2, 3}

# a = {0, 1, 2, 3, 4} # a не является подмножеством b
# b = {3, 2, 1}  # b подмножество a
# c1 = a >= b
# c = a <= b    # a не является подмножеством b
# print(c1)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = {6, 2}
# e = {8, 2}
# # d = a ^ b
# # d1 = a ^ b ^ c    # {0, 2, 4, 6}
# # d2 = a ^ b ^ c ^ e
# # print(d2)
# # Галочка '^' называется циркумфлекс
# d = a.symmetric_difference(b).symmetric_difference(c).symmetric_difference(e)
# print(d)

# a = {1, 2}
# b = {3}
# c = {4, 5}
# d = {3, 2, 6}
# e = {6}
# f = {7, 8}
# g = {9, 8}
# h = a | b | c | d | e | f | g
# print(h)
# print(len(h))
# # h = a.symmetric_difference(b).symmetric_difference(c).symmetric_difference(e)
# print(min(h))
# print(max(h))

# s1 = "Hello"
# s2 = "How are you"
# s3 = set(s1) & set(s2)  # строки преобразовались в set (множества)
# print(s3)
# for i in s3:
#     print(i, end=" ")

# s = frozenset([1, 2, 3, 4, 5, 6])
# print(s)
# s1 = frozenset({"hello", "world"})
# print(s1)
# s2 = frozenset("hello")
# print(s2)


# Словарь (dict)

# lst = ["one", "two"]
# d = {"first": "one", "second": "two"}
#
# print(lst[1])
# print(d["second"])

# d = {0: "text", "one": 45, (1, 2): "Кортеж", [5, 6, 7]: "Список"}    # Только неизменяемый
# print(d)    # Ключи не могут быть изменяемым типом данных
# d = {0: "text", "one": 45, (1, 2): "Кортеж", True: [5, 6, 7], "one": "один"}
# d = {0: "text", "one": 45, (1, 2): "Кортеж", True: [5, 6, 7], False: "один", 1: "Список"}
# print(d)


# d = {"first": "one", "second": "two"}  # В данном варианте создания в качестве ключа
# print(d)    # все неизменяемые типы данных могут быть использованы
# print(type(d))
#
# d = dict(first="one", second="two") # В данном варианте создания словаря
# print(d)    #  только строковые значения могут быть ключами
# print(type(d))

# lst = [
#     ["one", 1],
#     ["two", 2],
#     ["three", 3]
# ]
#
# print(lst)
# d = dict(lst)
# print(d)    #

# d = [i ** 2 for i in range(1, 7)]
# print(d)

# d = {i: i ** 2 for i in range(1, 7)}    # 1,2,3,4,5,6
# print(d)
#
# for i in d:
#     print("key =", i, "value =", d[i])

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# res = 1
# for key in d:
#     res *= d[key]
#
# print(res)


# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# print(d)
# del d['x2']
# print(d)

# d = dict()
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")
# print(d)

# d = {i: input("-> ") for i in range(1, 5)}
# print(d)
# dislike = int(input("Какой элемент исключить: "))
# del d[dislike]
# print(d)

# goods = {
#     "1": ['Core-i3-4330', 9, 4500],
#     "2": ['Core-i5-4670', 3, 8500],
#     "3": ['AMD FX-6300', 6, 3700],
#     "4": ['Pentium G3220', 8, 2100],
#     "5": ['Core-i5-4350', 5, 6500]
# }
#
# for i in goods:
#     print(i, ")", goods[i][0], " - ", goods[i][1], " по ", goods[i][2], "руб.", sep="")
#
# while True:
#     n = input("№: ")
#     if n == "0":
#         break
#     else:
#         if n in goods:
#             while True:
#                 try:
#                     count = int(input("Количество: "))
#                     goods[n][1] += count
#                     break
#                 except ValueError:
#                     print("Значение не корректно. Введите число")
#         else:
#             print("Такого ключа не существует")
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " по ", goods[i][2], "руб.", sep="")

# print(dir(dict))

# d = {1: "one", 2: "two", 3: "three"}
# print(d.keys())
# print(d.values())
# print(d.items())
#
# for i, j in d.items():
#     print(i, ":", j)

# d = {1: "one", 2: "two", 3: "three"}
# d2 = d.copy()
# print("D =", d)
# print("D2 =", d2)
#
# d2[2] = "four"
# print("D =", d)
# print("D2 =", d2)


# d = {1: "one", 2: "two", 3: "three"}
# print(d)
# # d.clear()
# item = d.pop(4, "Такого элемента не существует")
# print(d)
# print(item)

# Lesson 11

# d = {1: "one", 2: "two", 3: "three"}
# print(d)
# # d.clear()
# # item = d.pop(4, "Такого элемента не существует")
# item = d.popitem()
# print(d)
# print(item)

# d = {1: "one", 2: "two", 3: "three"}
# # value = d[6]
# value = d.get(6, "Такого ключа не существует")
# print(value)
# item = d.setdefault(4, "four")
# print(d)
# print(item)

# d = {1: "one", 2: "two", 3: "three"}
# # a = {10: "A", 20: "B"}  # , 2: "С"
# a = [(10, "A"), (20, "B"), (2, "C")]
# # c = d + a  # Error
# # c = d | a  # Конкатенация
# # print(c)
# d.update(a)
# print(d)

# d = {"name": 'Kelly', "age": 25, 'salary': 8000, 'city': 'New York'}
#
# new_d = dict()
# # new_d['name'] = d.pop('name')
# # new_d['salary'] = d.pop('salary')
# new_d['salary'], new_d['name'] = d.pop('salary'), d.pop('name')
# print(d)
# print(new_d)

# d = {"name": 'Kelly', "age": 25, 'salary': 8000, 'city': 'New York'}
#
# d['location'] = d.pop('city')  # Удалив key: value, мы перезаписали с новым ключём
# print(d)

# b_dict = {
#     'John': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
#     'Tom': {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
#     'Anne': {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
#     'Fiona': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}
# }

# Распакуем (по заданию) двумерный словарь:
# for name, nest_d in b_dict.items():  # Распаковка словаря с выводом имён пользователей.
#     print(name, ": ", sep="")   # , nest_d
#     for reg, sal in nest_d.items():  # Распаковка подсловаря с выводом регионов и объёма пр-ж.
#         print(reg, ": ", sal, sep="")

# for x, y in b_dict.items():  # Распаковка словаря с выводом имён пользователей.
#     print(x)
#     for i, j in y.items():  # Распаковка подсловаря с выводом регионов и объёма пр-ж.
#         print('\t', i, ": ", j, sep="")


# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# new_d = {key: key for key, value in d.items()}
# print(d)
# print(new_d)

# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# new_d = {key: value for key, value in d.items() if value <= 2}
# print(d)
# print(new_d)

# d = {i: i * 5 for i in [10, 20, 30, 40, 50]}
# print(d)
#
# s = "Hello"
# d1 = {key: key *3 for key in s}
# print(d1)

# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
#
# print(list(d.values()))
# print(list(d.keys()))
# print(list(d.items()))

# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
#
# d = dict()
# s = None
#
# for i in a:
#     if type(i) is str:
#         d[i] = []  # pass
#         s = i  # "one" ...
#     else:
#        d[s].append(i) # pass
#
# print(d)

# zip
# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# d = list(zip([1, 2, 3], ['one', 'two', 'three']))
# d = zip([1, 2, 3], ['one', 'two', 'three'])
# print(d)

# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# d = {v: k for k, v in zip(a, b)}
# print(d)


# one = {'name': 'Igor', 'surname': 'Pavlov', 'job': 'Consultant'}
# two = {'name': 'Irina', 'surname': 'Vetrova', 'job': 'Manager'}
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):  # 2 картежа
#     print(k1, "->", v1)
#     print(k2, "->", v2)

# s = [(1, 'a', 10), (2, 'b', 11), (3, 'c', 7)]
# a, b, c = zip(*s)  # Распакует на 3 картежа
# print(a)
# print(b)
# print(c)
# print(dir(dict))

# s = [(1, 'a'), (2, 'b'), (3, 'c')]
# a, b = zip(*s)
# print(a)
# print(b)


# letters = ['b', 'd', 'a', 'c']
# numbers = [4, 1, 3, 1]
# d = dict(zip(letters, numbers))
# print(d)
#
# data1 = list(zip(letters, numbers))
# print(data1)
# data1.sort()
# print(data1)
# d2 = dict(data1)
# print(d2)
#
# data2 = list(zip(numbers, letters))
# print(data2)
# data2.sort()
# print(data2)
# d3 = {v: k for k, v in data2}
# print(d3)

#
# letters = ['b', 'd', 'a', 'c']
# numbers = [4, 1, 3, 1]
#
# data = sorted(zip(letters, numbers))
# print(dict(data))

# one = {'один': 1, "два": 2}
# two = {'три': 1, "четыре": 2}
#
# print({**one, **two})  # {'один': 1, "два": 2, 'три': 1, "четыре": 2}
# print(one | two)
#
# for k, v in {**one, **two}.items():
#     print(k, "->", v)


# colors = ['red', 'green', 'blue']
# ind = 1
# for color in colors:
#     print(str(ind) + "-й цвет: " + color)
#     ind += 1
#
# print()
# for index, color in enumerate(colors, 1):  # enumerate(colors, start=10) - можно и так
#     print(str(index) + "-й цвет: " + color)


# d = {'один': 1, "два": 2, 'три': 1, "четыре": 2}
#
# for i, (k, v) in enumerate(d.items(), 1):
#     print(i, ") ", k, ": ", v, sep="")


# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)
#
# def func(*args):
#     return args
#
#
# print(func(5))
# print(func(1, 2, 3, 'adc'))


# def summa(*params):
#     res = 0
#     for n in params:
#         res += n
#     return res
#
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(summa(7, 8, 9))
#

# def to_dict(*args):
#     return {i: i for i in args}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict("grey", (2, 17), (3, 11), -4))


# def average(*args):
#     sr = sum(args) / len(args)
#     print(sr)
#     res = []
#     for num in args:
#         if num < sr:
#             res.append(num)
#     return res
#
#
# print(average(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(average(3, 6, 1, 9, 5))


# def func(a, b, *args):  # (*args, a) - в такой последовательности работать не будет
#     return a, b, args
#
#
# # print(func(5))
# print(func(1, 2, 3, 4, 5)
# Вылетела связь

# Всосстановлена связь
#
# def func1(*args):
#     print(args[])
#
# def func2(**kwargs):
#     print(kwargs["one"])


# Области видимости

# name = "Tom"  # Глобальная область видимости
#
#
# def hi():
#     global name
#     name = "Sam"
#     surname = "Jonson"  # Локальная область видимости
#     print("Hello", name)
#
#
# def bye():
#     print("Good bye", name)
#
#
# print(name)
# hi()
# bye()
# print(name)


# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()
# print(i)


# import builtins
#
# names = dir(builtins)
#
# for t in names:
#     print(t)


# max = 5
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(max(lst))


# x = 5
#
#
# def add_two(a):
#     x = 2
#
#     def add_some():
#         x = 3
#         print("x =", x)  # 4
#         return a + x  # 5
#
#     print("x в наружной функции =", x)
#     return add_some()  # 3  6
#
#
# print(add_two(3))  # 1  7
# print()


# Вложенные функции

# def outer(who):
#     def inner():
#         print("Hello", who)
#
#     inner()
#
#
# outer("World")


# def outer():
#     a = 6
#
#     def inner(b):
#         a = 4
#         print("Сумма", a + b)
#
#     print("a =", a)
#     inner(5)
#
#
# outer()

# x = 25

#
#
# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#         a = 35
#         print("a =", a)
#
#     inner()
#     t = a
#
#
# fn()
# c = x + t
# print(c)

# x = 5
#
# def fn1():
#     x = 25  # 55
#
#     def fn2():
#         # x = 33  # 55
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print("fn2.x =", x)     # 33 ->
#
#     fn2()
#     print("fn1.x =", x)     # 25
#
#
# fn1()


# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#         # print(a, b)
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))


# def rect_paral(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# # 2-й вариант Д/З - как глобальная
# # 3-й вариант Д/З - как нелокальная переменная
# print(rect_paral(2, 4, 6, ))
# print(rect_paral(5, 8, 2, ))
# print(rect_paral(1, 6, 8, ))


# Замыкание

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# a = outer(5)
# print(a(10))
#
# b = outer(6)
# print(b(10))
#
#
# print(outer(5)(10))


# def func1():
#     a = 1
#     b = "Line"
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + "!"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


# Задача

#
# def func(city):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
#
# res1 = func("Москва")
# res1()
# res1()
#
# res1()
# res2 = func("Сочи")
# res2()
# res2()
# res2()
# res1()
# res1()


# Анонимная функция

# def func(x, y):
#     res = x + y
#     return res
#
#
# print(func(1, 2))
#
# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)("a", "b"))
# print((lambda x, y: x + y)(1, 2))

# func1 = lambda x, y: x + y
#
# print(func1(1, 2))
# print(func1(5, 2))


# print((lambda a, b, c: a + b + c)(10, 20, 30))
# print((lambda a, b, c=3: a + b + c)(10, 20))
# print((lambda a, b=2, c=3: a + b + c)(10))
# print((lambda a=1, b=2, c=3: a + b + c)())

# print((lambda *args: sum(args))(1, 2, 3))

# print((lambda **kwargs: kwargs)(a=1, b=2, c=3))
# print((lambda **kwargs: sum(kwargs.values()))(a=1, b=2, c=3))

# c = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )  # Картеж В отличие от простой переменной картеж можно использовать для присвоения lambda
#
# for t in c:
#     print(t("abc__"))

# def outer(n):
#     def inner(x):
#         return x + n
#
#     return inner
#
#
# f = outer(42)
# print(f(3))
#
#
# def outer(n):
#     return lambda x: x + n
#
#
# f = outer(42)
# print(f(3))
#
# outer = lambda n: lambda x: x + n
# f = outer(42)
# print(f(3))
#
# f = (lambda n: lambda x: x + n)(42)
#
# print((lambda n: lambda x: x + n)(42)(3))
# res = (lambda n: lambda x: x + n)(42)(3)
# print(res)
#
# res = (lambda n: lambda x: "x > n" if x > n else "x < n")(42)(3)
# print(res)

# sum3(2)(4)(6) = 12
# res = (lambda n: lambda x: lambda d: x + n + d)(2)(4)(6)
# print(res)

# def func(i):
#     return i[1]
#
#
# d = {'b': 10, 'a': 15, 'c': 4}
# lst = list(d.items())
# print(lst)
# # lst.sort(reverse=True)
# # print(lst)
# lst.sort(key=func)  # lst.sort(key=lambda i: i[1])
# print(lst)
# d2 = dict(lst)
# print(d2)


# players = [
#     {'nam': "Антон", 'last name': "Бирюков", 'rating': 9},
#     {'nam': "Алексей", 'last name': "Бодня", 'rating': 10},
#     {'nam': "Фёдор", 'last name': "Сидоров", 'rating': 4},
#     {'nam': "Михаил", 'last name': "Семёнов", 'rating': 6},
# ]  # Список словарей
#
# res1 = sorted(players, key=lambda item: item["last name"])
# print(res1)
#
# res2 = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res2)
#
# res3 = sorted(players, key=lambda item: item['rating'])
# print(res3)

# lst = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
#
# print(lst[3](12, 2))

# d = {
#     1: lambda: print("Январь"),
#     2: lambda: print("Февраль"),
#     3: lambda: print("Март"),
#     4: lambda: print("Апрель"),
#     5: lambda: print("Май"),
#     6: lambda: print("Июнь"),
#     7: lambda: print("Июль"),
#     8: lambda: print("Август"),
#     9: lambda: print("Сентябрь"),
#     10: lambda: print("Октябрь"),
#     11: lambda: print("Ноябрь"),
#     12: lambda: print("Декабрь"),
# }
#
# d[3]()

# map()
# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, - 5, -10]
#
# print(list(map(mult, lst)))
#
# print(list(map(lambda t: t * 2, lst)))
#
# print(tuple(map(mult, lst)))
#
# print(set(map(mult, lst)))
#
# lst1 = [2, 8, 12, - 5, -10]
# lst2 = [12, -5, 2, -10, 8]
#
# print(dict(map(lambda x, y: (x, y), lst1, lst2)))  # Словарь
# print(list(map(lambda x, y: (x, y), lst1, lst2)))  # Список картежей
# print(list(map(lambda x, y: [x, y], lst1, lst2)))  # Список списков


# t = (2.88, -1.78, 100.55)
#
# print(tuple(map(lambda x: int(x), t)))
# print(tuple(map(int, t)))

# areas = [3.564789, 5.789456, 4.012456, 56.451266, 9.4567819, 32.45678912]
# print(list(map(round, areas, range(1, 7))))
# print(list(map(round, areas, range(1, 3))))
# print(list(map(round, areas, range(1, 10))))

# l1 = [1, 2, 3]
# l2 = [4, 5, 6, 7, 8]
#
# print(list(map(lambda x, y: x + y, l1, l2)))


# filter()

# t = ('abcd', 'qwe', 'zxcvb', 'def', 'hjk', '')  # Картеж
#
# # print(tuple(filter(lambda s: len(s) == 3, t)))
# print(tuple(filter(lambda s: len(s) == 3, t)))
# print(tuple(filter(lambda s: s + '3', t)))

# lst = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# print(list(filter(lambda s: s > 75, lst)))

# import random
#
# lst = [15, 37, 36, 26, 27, 28, 24, 3]
#
# lst1 = [random.randint(0, 40) for i in range(10)]
# print(lst1)
# print(list(filter(lambda s: s in range(10, 21), lst)))

# nums = [45, 55,60, 37, 100, 105, 220]
# print(list(filter(lambda x: x % 15 == 0, nums)))
# print(list(filter(lambda x: not x % 15, nums)))

# print(list(map(lambda x:  x ** 2, filter(lambda x: x % 2, range(10)))))
#
# print(list(filter(lambda x: x % 2, range(10))))
#
# print([x ** 2 for x in range(10) if x % 2])


# Декораторы

# def hello():
#     return "Hello, I am func 'hello'"
#
# def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())
#
#
# super_func(hello)


# def hello():
#     return "Hello, I am func 'hello'"
#
#
# text = hello
# print(text())


# def my_decorator(func):  # Декорирующая функция
#     def inner():
#         print("До кода")
#         func()
#         print("После кода")
#
#     return inner
#
#
# # @my_decorator   # декоратор
# def func_test():  # декорируемая функция
#     print("Hello, I am func 'func_test'")
#
#
# test = my_decorator(func_test)
# test()

# def my_decorator(func):
#     def inner():
#         print("До кода")
#         func()
#         print("После кода")
#
#     return inner
#
# @my_decorator
# def func_test():
#     print("Hello, I am func 'func_test'")
#
#
# func_test()

"""
# Lesson 14
"""
import json
# import json
# import pickle
# lst = [input("-> ") for i in range(5)]
# print(lst)
# num = list(map(int, lst))
# print(num)

# def circle(fn):
#     def wrap():
#         return "(" + fn() + ")"
#
#     return wrap
#
#
# def angle(fn):
#     def wrap():
#         return "<" + fn() + ">"
#
#     return wrap
#
#
# @circle
# @angle
# def expression():
#     return '5 + 2'
#
#
# print(expression())

# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count = count + 1
#         fn()
#         print("Вызов функции", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()


# def outer(fn):
#     def inner(arg1, arg2):
#         print("Данные:", arg1, arg2)
#         fn(arg1, arg2)
#
#     return inner
#
#
# @outer
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Ветрова")


# def outer(fn):
#     def inner(*args, **kwargs):
#         print("args:", args)
#         print("kwargs:", kwargs)
#         fn(*args, **kwargs)
#
#     return inner
#
#
# @outer
# def print_data(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, end="\n\n")
#
#
# print_data("Борис", "Елизавета", "Светлана", study="JavaScript")
# print_data("Владимир", "Екатерина", "Виктор")

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)


# def multiply(arg):
#     def my_decorator(func):
#         def wrap(*args, **kwargs):
#             print(args)   # *args - картеж, *kwargs - словарь
#             # return arg * func(*args, *kwargs)
#             return arg
#         return wrap
#     return my_decorator
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5, 2, 3))

# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) is not args[i]:
#                     raise TypeError("Неверный тип данных")  # return "Неверный тип данных"
#             # for k in kwargs:
#             #     if type(f_kwargs) is not kwargs[k]:
#             #         raise TypeError("Неверный тип данных")
#             return fn(*f_args, **f_kwargs)  # raise в отличие от return останавливает прграмму в ош
#
#         return wrap
#
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, "Hello"))
# print(typed_fn2("Hello", " World", "!"))
# # print(typed_fn2(3, 4, 5))
# print(typed_fn3("Hello", " World", z=5))
# # print(typed_fn3("Hello", " World", z="!"))


# Строки

# print(bin(18))  # 0b10010 - двоичная система счисления
# print(oct(18))  # 0o22 - восьмеричная система счисления
# print(hex(18))  # 0x12 - шестнадцатеричная система счисления
#
# print(0b10010)
# print(0o22)
# print(0x12)
# print(0x12 + 0b10010 + 4)


# q = "Pyt"
# w = "hot"
# e = q + w
# print(e)
# # print(e * 3)
# # print("y" in e)
# # print("a" in e)
# # print(e[1])
# # e[1] = "i"
# print(e[::-1])  # Разворот в противоположную сторону

# def change_char_to_str(s, old, new):
#     s2 = ""
#     i = 0
#     while i < len(s):
#         if s[i] == old:
#             s2 += new
#         else:
#             s2 += s[i]
#         i += 1
#
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# str2 = change_char_to_str(str1, "N", "P")
# print(str1)
# print(str2)

# Префиксы

# print(u"Привет")
# print("Привет")


# print("C:\\file.txt")
# print(r"C:\file.txt")  # r - снимает экранирование
# print(r"C:\file.txt\\"[:-1])  # Последний символ не может быть backslash, поэтому его можно вывести убрав
# # через срез, до -1-го символа
# print(r"C:\file.txt" + "\\")
# print("C:\\file.txt\\")
# # print(r"C:\file.txt\") # Ошибка r SyntaxError: unterminated string literal (detected at line 2675)

# Строки.  10.03.2025 г.
# f - строки

# name = "Дмитрий"
# age = 25
# print(f"Меня зовут {name}. Мне {age} лет.")

# x = 10
# y = 5
# print(f"{x=}, {y=}")
# print("x=", x, ", y=", y, sep="")
# print(f"{round(10/7, 2)}")
# print(f"{10/7:.3f}")
# num = 74
# print(f"{{{{{num}}}}}")  # Служебный символ фигурные скобки

# dir_name = "person"
# file_name = "file.txt"
# print(fr"home\{dir_name}\{file_name}")
# print("home\\" + dir_name + "\\" + file_name)


# s = """Многострочный
#  текст    много   много
# """
# print(s)
# st = ("Многострочный \n"
#       "текст")
# print(st)


# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     res = n ** 2
#     return res
#
#
# print(square(5))
# print(square.__doc__)
# # # max()
# # print(sum.__doc__)
# # print(min.__doc__)
# print(len.__doc__)


# from math import pi
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания.
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)

# print(ord('a'))    # Вывод кода символа
# print(ord('а'))
# print(ord('б'))


# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# Задачка
# st = "Test string for me "
# arr = [ord(x) for x in st]
# print("ASCII коды:", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое:", arr)
# arr += [x for x in input("-> ")[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(97))
# print(chr(35))
# print(chr(8364))

# a = 122
# b = 97
#
# if a > b:
#     for i in range(b, a + 1):
#         print(chr(i), end=" ")
# else:
#     for i in range(a, b + 1):
#         print(chr(i), end=" ")


# print("apple" > "Apple")
# print(ord("a"))
# print(ord("A"))


# from random import randint
#
# SHORT = 8
# LONG = 16
#
# MIN_ASCII = 33
# MAX_ASCII = 126
#
#
# def random_password():
#     rand_len = randint(SHORT, LONG)
#     result = ""
#     for i in range(rand_len):
#         result += chr(randint(MIN_ASCII, MAX_ASCII))
#     return result
#
#
# print("Случайный пароль:", random_password())


# print(dir(str))

# s = "hello, WORLD! I am learning Prthon."
# print(s.capitalize())  # Первый символ в верхнем регистре все остальные в нижнем
# print(s.lower())  # все символы в нижнем регистре
# print(s.upper())  # все символы в верхнем регистре
# print(s.swapcase())  # инвертирование регистра символов
# print(s.title())  # первая буква каждого слова в верхнем регистре
#
# print(s.count("h"))  # количество вхождений символов
# print(s.count("i"))

# print(s.lower().count("i"))
# print(s.count("h", 1, -4))  # подсчёт кол-ва вхождений символов в интервале

# print(s.find("Python"))  # возвращает первый индекс подстроки
# print(s.find("h", 1, -4))  # если вхождение не найдено, то возвращается "-1"
#
# print(s.index("Python"))  # возвращает первый индекс подстроки
# print(s.index("h"))  # если вхождение не найдено, возвращает исключение ValueError

# st = "один два"
# one = st[:st.find(" ")]
# two = st[st.find(" ") + 1:]
# # print(two)
# print(two + " " + one)

# print(s.rfind("h", 1, -4))  # возвращает индекс подстроки, если вхождение не найдено, возвращает "-1"
# print(s.rindex("h", 1, -4))  # возвращает индекс подстроки, если вхождение не найдено,
# # то возвращает исключение ValueError

# st = "I am learning Python. hello, WORLD!"
# print(st[:st.find('h')] + st[st.rfind('h') + 1:])

# s = "hello, WORLD! I am learning Prthon."
# print(s.startswith("he"))  # возвращает True, если строка начинается с заданной подстроки
# print(s.startswith("I am", 14))
# print(s.find("I am"))
#
# print(s.endswith("Python"))  # возвращает True, если строка заканчивается заданной подстрокой

# print('abc123'.isalnum())  # проверяет стостоит ли строка из букв и цифр
# print('abc%123'.isalnum())
# print('4'.isalnum())
#
# print("ABCsvb".isalpha())  # определяет, состоит ли строка из букв
# print("ABCsvb!".isalpha())
# print("8".isdigit())  # определяет, состоит ли строка из цифр

# print("abc".islower())  # определяет, состоит-ли строка из букв в нижнем регистре.
# print("Abc".islower())  # допускается наличие любых других символов
# print("@&abc".islower())
# print("".islower())
#
# print("ABC".isupper())  # пределяет, состоит-ли строка из букв в верхнем регистре

# print('py'.center(10))  # выравниваем строку по центру
# print('py'.center(10, "-"))
# print('py'.center(1))

# print("    py".lstrip())  # удалит пробелы слева
# print("py     ".rstrip())  # удалит пробелы справа
# print("   py     ".strip())  # удалит пробелы слева и справа
#
# print("https://.python.org".lstrip("htps:/"))
# print("https://.python.org".rstrip("org"))
# print("https://.python.org".strip("org."))


# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# print(str1.replace("Nython", "Python", 2))   # поиск и замена


# st = "-"
# seq = ("a", "b", "c")
# print(st.join(seq))
#
# # print("..".join([1, 99]))
# print("..".join(['1', '99']))
# print(":".join('a'))  # список в строку преобразует
# print(":".join('abc'))
#
# print("Строка разделенная пробелами".split())  # строку преобразовывает в список по символу разделителю
# print("www.python.org".split('.'))
# print("www.python.org.ru".split('.', 2))
#
# print("www.python.org".rsplit('.'))
# print("www.python.org.ru".rsplit('.', 2))


# # st = "Никонов Валерий Анатольевич"
# st = input("Введите ФИО: ").split()
# # st = st.split()
# print(st)
# print(f'{st[0]} {st[1][0]}. {st[2][0]}.')


# num = input("Введите числа через пробел: ").split()
# print(num)
# num = list(map(int, num))  # функция map() преобразует каждый элемент списка в указанный тип (здесь - int)
# print(num)
# print(sum(num))

# Регулярные выражения (Урок 16)
# Для начала импортируем модуль "re" - сокращение от Regular Express
import re

# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта. 6789"  # Строка


# reg = r"\."  # Шаблон (r"\.")[ан]
# print(re.findall(reg, s))  # Возвращает список, содержащий все совпадения
# print(re.search(reg, s))  # это расположение первого совпадения объекта
# # print(re.search(reg, s).span())  # небезопасный метод. могут быть исключения
# # print(re.search(reg, s).start())  # небезопасный метод. могут быть исключения
# # print(re.search(reg, s).end())  # небезопасный метод. могут быть исключения
# # print(re.search(reg, s).group())  # небезопасный метод. могут быть исключения
# print(re.match(reg, s))  # поиск совпадения только с начала строки
# print(re.split(reg, s))  # , 2 # Возвращает список в котором строка разбита по заданному шаблону
# print(re.sub(reg, "!", s, 1))  # поиск и замена

# print(dir(re))
# reg = r"[205]"  # квадратные скобки это любой один символ указывается
# reg = r"[6-9]"  #
# reg = r"[12][0-9][0-9][0-9]"  #
# reg = r"[А-яЁё]"  #

# s = "Hello World!"
# reg = r"[A-Za-z\]\[-]"  #
# reg = r"[^0-9]"  # циркумфлекс "^" - всё кроме цифр, т.е. Поиск всего кроме заданных элементов
# print(re.findall(reg, s))

# st = "Час в 24-часовом формате от 00 до 23. 2021-06-15T21:55. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09."
# reg = "[0-2][0-9]:[0-5][0-9]"
# print(re.findall(reg, st))


# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта. 6789. [Hel-lo] Wor_ld"  # Строка

# reg = r"[0-9].."
# reg = r"\d"  # все цифры 0- 9
# reg = r"\D"  # все кроме цифр
# reg = r"\s"  # пробельный символ
# reg = r"\S"  # все кроме пробелов
# reg = r"\w"  # русский английски буквы цифры и символ подчёркивания
# reg = r"\W"  # всё кроме символов в верхнем регистре и символов подчёркивания

# reg = r"\АЯ ищу"

# s = "Hello World!"
# reg = r"World!\Z"

# reg = r"Wor_ld\Z"
# reg = r"сов\B"

# reg = r"\w+"
# reg = r"\d+"
# reg = r"20*"
# print(re.findall(reg, s))

# Количество повторений
#  + - от 1 до бесконечности
#  * - от 0 до бесконечности
#  ? - от 0 до 1 повторения

# d = "Цифры: 7, +17, -24, 0013, 0.3"
# reg = r"[+-]?[\d.]+"  # ? - это может быть а может не быть
# print(re.findall(reg, d))

# d = "05-03-1987  # Дата рождения"
#
# print("Дата рождения:", re.sub(r"\s\s#.+", "", d))
#
# print(re.sub(r"-", ".", d))
#
# print("Дата рождения:", re.sub(r"\s\s#.+", "", re.sub(r"-", ".", d)))

# st = "author=Пушкин А.С.; title = Евгений Онегин; price =200, year= 1831"
# # reg = r"\w+\s*=\s*\w+\s*\w+\.?\w?\.?"
# reg = r"\w+\s*=[^;]*"
# print(re.findall(reg, st))
#
# reg1 = r"; "
# print(re.split(reg1, st))

# st = "12 сентября 2025 года"
# # reg = r"\d{4}"
# # reg = r"\d{2,4}"
# # reg = r"\d{4,}"  # от 4-х повторений
# # reg = r"\d{,4}"  # до 4-х повторений
# print(re.findall(reg, st))

# st = "+7 499 456-45-78, +74994564578, +7(499)456 45 78, 74994564578"
# reg = r"\+?7\d{10}"
# print(re.findall(reg, st))


# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта. 6789. [Hel-lo] Wor_ld 3450000000"  # Строка
# # reg = r"^\w+\s\w+"
# reg = r"\w+\s\w+$"
# print(re.findall(reg, s))


# def validare_login(login):
#     return re.findall(r"^[A-Za-z0-9_]{3,16}$", login)
#
#
# print(validare_login("Python_master"))
# print(validare_login("Pyt!!!"))


# text = "<body>Пример жадного совпадения соответствия регулярных выражений</body>"
# print(re.findall("<.*?>", text))
#
# #  *?, +?, ??
# # {m,n}?, {,n}?, {m,}?


# st = "Петр, Ольга и Виталий отлично учатся!"
# reg = r"Петр|Ольга|Виталий|Наталья"
# print(re.findall(reg, st))

# st = "int = 4, float = 4.0f, double = 8.0, int"
# # reg = r"\w+\s*=\s*\d[.\w+]*"
# # reg = r"int\s*=\s*\d[.\w+]*|float"
# # reg = r"(?:int|float)\s*=\s*\d[.\w+]*"  # чтобы скобки не были сохраняющими ?:
# reg = r"((int|float)\s*=\s*(\d[.\w+]*))"  # чтобы скобки не были сохраняющими ?:
# print(re.findall(reg, st))

# d = "Word2016, PS6, AI5"
# # reg = r"([A-Za-z]+)\d+"
# reg = r"[A-Za-z]+(\d+)"
# print(re.findall(reg, d))
# print(re.search(reg, d))


# st = "5 + 7*2 - 4"
# reg = r"\s*([+*-])\s*"
# print(re.split(reg, st))

# 17 урок

# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта. 6789. [Hel-lo] Wor_ld 3450000000"  # Строка
# reg = r"([0-9]+)+\s(\D+)"
# print(re.search(reg, s).group(1))
# m = re.search(reg, s)
# print(m[0])
# print(m[1])
# print(m[2])


# s = "Самолёт прилетает 10/23/2025. Будем рады вас видеть после 10/24/2025."
# reg = r"(\d{2})/(d{2})/(\d{4})"
# print(re.sub(reg,r"\2.\1.\3", s))


# s = "yandex.com and yandex.ru"
# reg = r"(([a-z0-9-]{2,}\.)+[a-z]{2,4})"
# print(re.sub(reg, r"http://\1", s))

# s = "28-08-2021" # 01 - 31
# reg = r"^(0[1-9]|[12][0-9]|3[01])-(19[0-9][0-9]|20[0-9][0-9])$"
# print(re.findall(reg, s))

# print(re.findall(r"\w+", "12 + й"))
# print(re.findall(r"\w+", "12 + й", flags=re.ASCII))

# text = "hello world"
# print(re.findall(r"\w\+", text))
# print(re.findall(r"\w\+", text, re.DEBUG))

# text = "hello world"
# reg = "l"
# print(re.findall(reg, text, re.IGNORECASE))

# text = """
# one
# two
# """

# print(re.findall(r"one.\w+", text))
# print(re.findall(r"one.\w+", text, re.DOTALL))

# print(re.findall(r"one$", text))
# print(re.findall(r"one$", text, re.MULTILINE))

# print(re.findall("""
# [a-z.-]+     # part 1
# @           # @
# [a-z.]+     # part 2
# """, "text@mail.ru", re.VERBOSE))

# text = """Python,
# python,
# PYTHON
# """
# reg = "(?im)^python"
# print(re.findall(reg, text))
#   Пока закончили с регулярными выражениями.

# Возвращаемся к функциям
# Рекурсия


# def elevator(n):  # 5
#     if n == 0:  # базовый случай
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevator(n - 1)  # 5 4 3 2 1 Стек область в памяти, визуально не видимая
#     print(n, end=" ")
#
#
# n1 = int(input("На каком этаже вы находитесь: "))
# elevator(n1)


# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))

# def sum_list(lst):  # [3, 5, 7, 9] {5, 7, 9] [7, 9] [9]
#     if len(lst) == 1:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0]  # 9
#     else:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0] + sum_list(lst[1:])  # 1 + 3 + 5 + 7 +
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# def to_str(n, base):  # 254, 16
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]  # F
#     else:
#         return to_str(n // base, base) + convert[n % base]  # to_str(254 // 16, 16) + 'E' +
#
#
# print(to_str(254, 10))  # Десятичная
# print(to_str(254, 16))  # Шестнадцатиричная


# names = ["Adam", ["Bob", ["Chet", "Cat"], "Barb", "Berb"], "Alex", ["Bea", "Bill"], "Ann"]
# print(len(names))
# print(names[0])
# print(isinstance(names[0], list))
# print(names[1])
# print(isinstance(names[1], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))

# names = ["Adam", ["Bob", ["Chet", "Cat"], "Barb", "Berb"], "Alex", ["Bea", "Bill"], "Ann"]
#
#
# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))


# Файлы

# # f = open("text.txt", "r")
# f = open(r"D:\dev_Py522_TOP\pythonProject\text.txt", "r")
# print(f)
# print(*f)  # Распаковка, т.е. просмотр содержимого
# # print(f.closed)
# f.close()
# print(f.closed)
# print(f.mode)
# print(f.name)
# print(f.encoding)


# # f = open("text.txt", "r")
# f = open("text.txt")
# print(f.read(3))  # Курсор на троечке
# print(f.read())
# f.close()


# f = open("xyz.txt", "w")
# f.write("This is line1.\nThis is line2.\nThis is line3.\n")
# f.close()

# f = open("xyz.txt")
# print(f.read())  # Полностью читает файл

# print(f.readline())  # Построчно
# print(f.readline(8))
# print(f.readline())
# print(f.readline())

# print(f.readlines(26))  # Список из строк
# print(f.readlines())  # Список из строк
# f.close()
# print(f.closed)

# count = 0
#
# f = open("xyz.txt")
# for line in f:
#     print(line)
#     count += 1
# f.close()
# print(count)


# f = open("xyz.txt")
# print(len(f.readlines()))
# f.close()


# f = open("test.txt", "w")
# f.write("Hello\nWorld\n")
# f.close()
#
# f = open("test.txt", "a")
# f.write("New text")
# f.close()

# lines = ["This is line1.", "This is line2.", "This is line3."]
# f = open("test1.txt", "a")
# # f.write("New text")
# f.writelines(lines)
# f.close()


# Занятие 18
# Д/з

# def negative_numbers(n):
#     if not n:
#         return 0
#     count = 0
#     if n[0] < 0:
#         count += 1
#     return count + negative_numbers(n[1:])
#
#
# lst = [-2, 3, 8, -11, -4, 6]
# print(negative_numbers(lst))


# file = "test2.txt"
# f = open(file, "w")
# f.write("Замена строки в текстовом файле;\n"
#         "изменить строку в списке;\n"
#         "записать список в файл;")
# f.close()
#
# f = open(file)
# data = f.readlines()
# print(data)
# data[1] = "Hello World!\n"
# print(data)
# f.close()
#
# f = open(file, "w")
# f.writelines(data)
# f.close()


# f = open("test2.txt", 'w')
# lst = [i for i in range(1, 100, 5)]
# print(lst)
# for index in lst:
#     f.write(str(index) + "\t")
# f.close()

# f = open("text.txt")
# print(f.read(3))
# print(f.tell())  # возвращает текущую позицию условного курсора в файле
# print(f.seek(1))  # перемещает условный курсор в заданную позицию
# print(f.read())
# print(f.tell())
# f.close()

# f = open("text.txt", "r+")
# print(f.write("I am learning Python"))
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())
# f.close()


# f = open("text.txt", "a+")
# print(f.read())
# f.close()


# with open("text.txt", "w") as f:
#     print(f.write("0123456789"))
# print(f.closed)
#
# with open("text.txt") as f:
#     print(f.read())

# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 5.47]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     return " ".join(lt)
#
#
# with open("res.txt", "w") as f:
#     f.write(get_line(lst))
#
# print("Файл записан")

# Здесь было с ошибкой:
# ----------------------------------------------
# with open("res.txt") as f:
#     nums = f.read()
#
# print(nums)

# lst = list(map(float, nums.split(" ")))
# print(lst)
# lst = list(map(float, nums.split()))
# print(lst)
# print(sum(lst))
# ----------------------------------------------
# Выяснили в чём ошибка, вариант без ошибки:
# ----------------------------------------------
# with open("res.txt") as f:
#     nums = f.read()
#
# print("Файл прочитан", nums)
# # nm = nums.split(", ")  # Добавили правильный разделитель: ", "
# # print("split:", nm)
#
# lst = list(map(float, nums.split(", ")))
# print("lst:", lst)
# print(type(lst[0]))
# print("Сумма:", sum(lst))
# ----------------------------------------------

# file_name = "long.txt"
#
# with open(file_name, "w") as f:
#     f.write("Файл — именованная область данных на носителе информации, "
#             "используемая как базовый объект взаимодействия с данными в"
#             " операционных системах.")
#
#
# def longest_world(file):
#     with open(file) as text:
#         lst = text.read().split()
#         print(lst)
#         max_length = len(max(lst, key=len))
#         print(max_length)
#         res = [word for word in lst if len(word) == max_length]
#
#         return res[0] if len(res) == 1 else res
#
#
# print(longest_world(file_name))

# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
# with open("one.txt", "w") as f:
#     f.write(text)
#
# with open("one.txt", "r") as fr, open("two.txt", "w") as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия -")
#         fw.write(line)

# Модули OS и OS.PATH

# import os

# print(os.getcwd())  # Путь к текущей директории
#
# print(os.listdir())  # список директорий и файлов
# print(os.listdir(".."))  #
# print(os.listdir(".venv"))  #

# # os.mkdir("person")  # создали папку (вложенные нельзя)
# os.rmdir("person")  # удалить папку

# os.makedirs("nested1/nested2/nested3")  # создаётся папка с промежуточными директориями
# os.remove("xyz.txt")

# os.rename("file_name", "file.name.txt")
# os.rename("file_name.txt", "new_file.txt")
# os.rename("new_file.txt", "")  # переименовывает файл
# может перемещать существующую директорию
# os.renames("two2.txt", "test/two2.txt") # переименовывает файл,
# может создавать директории, которых не существует

# for root, dirs, files in os.walk("nested1", topdown=False):
#     print("Root:", root)
#     print("\tDirs:", dirs)
#     print("\t\tFiles:", files)

# os.rmdir("nested1")


# def remove_empty_dirs(root_tree):
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f"Директория {root} удалена.")
#
#
# remove_empty_dirs("nested1")
# Результат:
# Директория nested1\nested2\folder2 удалена.
# Директория nested1\nested2\nested3\folder3 удалена.

# import os
# import os.path

# print(os.path.split(r"D:\dev_Py522_TOP\pythonProject\nested1\nested2\nested3\text3.txt"))
# print(os.path.join(r"D:\dev_Py522_TOP\pythonProject", "nested1", "nested2", "nested3", "text3.txt"))
# print(os.path.join("nested1", r"D:\dev_Py522_TOP\pythonProject", "nested2", "nested3", "text3.txt"))
# print(os.path.exists(r"D:\dev_Py522_TOP\pythonProject\nested1\nested2\nested3\text3.txt"))
# print(os.path.exists(r"D:\dev_Py522_TOP\pythonProject\nested2\nested3\text3.txt"))
# print(os.path.isfile(r"D:\dev_Py522_TOP\pythonProject\nested1\nested2\nested3\text3.txt"))
# print(os.path.isdir(r"D:\dev_Py522_TOP\pythonProject\nested1\nested2\nested3"))

# Lesson 19

# with open("text.txt", "w+") as f:
#     f.write("Hello")
#     f.seek(0)
#     data = f.read()  # "Hello"
#     data += "!"  # "Hello!"
#     f.seek(0)
#     f.write(data)

# import os
#
# file = "test2.txt"
# st_f = """Замена строки в текстовом файле;
# изменить строку в списке;
# записать список в файл;
# """
# f = open(file, "w")
# f.write(st_f)  # Запись содержимого строки "st_f" в файл "test_dz.txt"
# f.close()
#
# f = open(file, "r")
# read_line = f.readlines()
# f.close()
#
# pos1 = int(input("pos1 = "))
# pos2 = int(input("pos2 = "))
#
# if 0 <= pos1 < len(read_line) and 0 <= pos2 < len(read_line):
#     read_line[pos1], read_line[pos2] = read_line[pos2], read_line[pos1]
# else:
#     print("такой строки нет")
# print(read_line)
#
# f = open(file, "w")
# f.writelines(read_line)
# f.close()
#
# if os.path.exists(file):
#     f = open(file, "r")
#     read_line = f.readlines()
#     f.close()
# else:
#     print("Такого файла нет")

# print("Данные в локальном репозитории")

# Lesson 20

# print("Код, созданный на новом устройстве")

# import os

# # import os.path

# dirs = [r'Work\F1', r'Work\F2\F21']

# for d in dirs:
#     os.makedirs(d)

# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }

# for key, value in files.items():
#     for file in value:
#         file_path = os.path.join(key, file)
#         open(file_path, 'w').close()

# Work\w.txt
# Work\F1\f11.txt
# Work\F1\f12.txt
# Work\F1\f13.txt
# Work\F2\F21\f211.txt
# Work\F2\F21\f212.txt


# file_with_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F1\f13.txt', r'Work\F2\F21\f212.txt']
#
#
# # for file in file_with_text:
# #     with open(file, 'w') as f:
# #         f.write(f'Некоторый текст для файла {file}')
#
# def print_tree(topdown):
#     print(f"Обход Work {'сверху вниз' if topdown else 'снизу вверх'}")
#     for root, directory, file in os.walk("Work", topdown):
#         print(root)
#         print(directory)
#         print(file)
#     print("-" * 50)
#
#
# print_tree(False)
# print_tree(True)


# import os
# import time
#
# path = "main.py"
# print(os.path.getsize(path))  # размер файла
# print(os.path.getatime(path))  # время последнего доступа к файлу (в секундах)
# print(os.path.getmtime(path))  # время последнего измененияч)
# print(os.path.getctime(path))  # время создания файла
#
# size = os.path.getsize(path)
# a_time = os.path.getatime(path)
# m_time = os.path.getmtime(path)
# c_time = os.path.getctime(path)
#
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(a_time)))
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(m_time)))
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(c_time)))
# print(size)
# print(size // 1024)


# import os

# file_path = r"D:\dev_Py522_TOP\pythonProject\nested1\nested2\nested3\text3.txt"
#
# if os.path.exists(file_path):
#     directory, file = os.path.split(file_path)
#     a_time = os.path.getatime(file_path)
#     print(f"{file} ({directory}) - {a_time}")
# else:
#     print(f"Файл {file_path} не существует")


# dir_name = "Work"  # Присвоение имени каталога к переменной
#
# objs = os.listdir(dir_name)  # Отображение списка с содержимым каталога
# print(objs)
#
#
# for obj in objs:
#     p = os.path.join(dir_name, obj)  # Конкатенация относительного адреса (адрес от текущего рабочего каталога)
#     # print(p)  # Work\F1, Work\F2, Work\w.txt  - результат прохода цикла с результатами конкатенации адресов
#     if os.path.isfile(p):  # Использование метода "Существует-ли файл по указанному пути "
#         print(f"{obj} - file - {os.path.getsize(p)} bytes")
#     if os.path.isdir(p):
#         print(f"{obj} - dir")


#  Занятие 21
# import os
#
#
# def info_files(root, person):
#     for root, dirs, files in os.walk(root):
#         for file in files:
#             file_path = os.path.join(root, )
#             print(file_path)
#             file_size = os.path.getsize(file_path)
#             if file_size == 0:
#                 os.rename(file_path, os.path.join(person, file))
#                 print(f"Файл {file} перемещён из папки {root} в папку {person}")
#             else:
#                 print(f'{file_path} - {file_size} bytes')
#
#
# info_files("Work", "Work/empty_files")

# ООП

# class Point:
#     x = 1
#     y = 2
#
#
# p1 = Point()
# Point.x = 100
# print(p1.x)
# print(Point.x)
# print(id(p1))
# print(id(Point))
# p1.x = 100
# p1.y = 50
# print(p1.x, p1.y)
# print(p1.__dict__)  # dict settings
#
# p2 = Point()
# print(p2.x, p2.y)
# print(p2.__dict__)
# print(Point.__dict__)


# class Point:
#     x = 1
#     y = 2
#
#     def set_coord(self):  # self anyone
#         print(self.__dict__)
#
#
# p1 = Point()
# p1.x = 5
# p1.y = 10
# p1.set_coord()
# Point.set_coord(p1)
#
# p2 = Point()
# p2.set_coord()


# class Point:
#     x = 1
#     y = 2
#
#     def set_coord(self, x1, y1):  # self anyone
#         self.x = x1
#         self.y = y1
#
#
# p1 = Point()
# p1.set_coord(5, 10)
# Point.set_coord(p1, 10,20)
# print(p1.__dict__)
#
# p2 = Point()
# p2.set_coord(2, 7)
# print(p2.__dict__)


# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     sity = "sity"
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\n"
#               f"Страна: {self.country}\nГород: {self.sity}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthdey, phone, countre, city, address):
#         self.name = first_name
#         self.birthdey = birthdey
#         self.phone = phone
#         self.countre = countre
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):  # Установили новое имя
#         self.name = name
#
#     def get_name(self):  # получили имя
#         return self.name
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.11.1999", "45-46-98", "Россия", "Моска", "Чистопрудный")
# h1.print_info()
# h1.set_name("Юлия")
# h1.print_info()
# print(h1.get_name())


# class Person:
#     skill = 10  # Статические св-ва класса
#
#     def __init__(self, name, surname):  # Инициализатор класса (в других языках программирования - конструктор)
#         self.name = name  # Динамические св-ва класса
#         self.surname = surname
#
#     def __del__(self):
#         print("Удаление экземпляра\n\n")
#
#     def print_info(self):
#         print("Данные сотрудника:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника:", self.skill, "\n")


# p1 = Person("Виктор", "Резник")
# p1.print_info()
# p1.add_skill(3)
# # del p1
# p1 = 5
#
# p2 = Person("Анна", "Долгих")
# p2.print_info()
# p2.add_skill(2)


# class Person:
#     count = 0  # Статические св-ва класса
#
#     def __init__(self, name, surname):  # Инициализатор класса (в других языках программирования - конструктор)
#         self.name = name  # Динамические св-ва класса
#         self.surname = surname
#         Person.count += 1  # self.count
#
#     def print_info(self):
#         print("Данные сотрудника:", self.name, self.surname)
#
#
# p1 = Person("Виктор", "Резник")
# p1.print_info()
#
# p2 = Person("Анна", "Долгих")
# p2.print_info()
#
# print(p1.count)
# print(p2.count)
# print(Person.count)
#
# p3 = Person("Анна", "Долгих")
# print(p3.count)
# print(Person.count)

# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота:", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "Выключается!")
#         Robot.k -= 1
#
#         if Robot.k == 0:
#             print(self.name, "был последним")
#         else:
#             print("Работающих роботов:", Robot.k)
#
#     def say_hi(self):
#         print("Привет! Меня зовут:", self.name)
#
#
# droid1 = Robot("R2-D2")
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid2 = Robot("C-3PO")
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid3 = Robot("PC-3O")
# droid3.say_hi()
# print("Численность роботов:", Robot.k)
#
# print("\nЗдесь роботы могут проделать какую-то работу\n")
# print("Роботы закончили свою работу. Давайте их выключим.\n")
#
# del droid1, droid2, droid3
#
# print("Численность роботов:", Robot.k)


# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     sity = "sity"
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\n"
#               f"Страна: {self.country}\nГород: {self.sity}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthdey, phone, countre, city, address):
#         self.name = first_name
#         self.birthdey = birthdey
#         self.phone = phone
#         self.countre = countre
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):  # Установили новое имя
#         self.name = name
#
#     def get_name(self):  # получили имя
#         return self.name
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.11.1999", "45-46-98", "Россия", "Моска", "Чистопрудный")
# h1.print_info()
# h1.set_name("Юлия")
# h1.print_info()
# print(h1.get_name())

# 22 lesson

# class Point:
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             # if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(c):
#         if isinstance(c, int) or isinstance(c, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             # if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coord_x(self, x):
#         if Point.__check_value(x):
#             # if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
#             self.__x = x
#         else:
#             print("Координата x должна быть числом")
#
#     def get_coord(self):
#         return self.__x, self.__y
#
#
# p1 = Point(5.2, 10)  # "abc", 10
# # print(p1.x, p1.y)
#
# # p1.set_coord(5.2, 100)
# print(p1.get_coord())
# # p1.__x = 100
# # p1.__y = "abc"
# # print(p1.__x, p1.__y)
# print(p1.__dict__)
# # print(p1.__check_value(10))
# # Модификаторы доступа
# # Инкапсуляция это сво-во системы защищающее её от внешнего воздействия
# p1._Point__x = 111  # не рекомендуемый тип доступа - прямой, лучше через get-er и set-er
# # print(p1._Point__x)  # не рекомендуемый тип доступа - прямой, лучше через get-er и set-er
# # print(p1.__dict__)

# import math
#
#
# class Rectangle:
#     def __init__(self, length=1, width=1):
#         self.__length = length
#         self.__width = width
#
#     def __check_value(c):
#         if isinstance(c, int) or isinstance(c, float):
#             return True
#         return False
#
#     def get_width(self):
#         return self.__width
#
#     def get_length(self):
#         return self.__length
#
#     def set_length(self, length):
#         if Rectangle.__check_value(length):
#             self.__length = length
#
#     def set_width(self, width):
#         if Rectangle.__check_value(width):
#             self.__width = width
#
#     def get_area(self):
#         return self.__width * self.__length
#
#     def get_perimeter(self):
#         return 2 * (self.__width + self.__length)
#
#     def get_hipotenuse(self):
#         return round(math.sqrt((self.__length ** 2 + self.__width ** 2)), 2)
#
#     # def get_draw(self):
#     #     for _ in range(self.__length):
#     #         print("*" * self.__width)
#
#     def get_draw(self):
#         print(('*' * self.__width + '\n') * self.__length)
#
#
# r1 = Rectangle()
# r1.set_width(9)
# r1.set_length(3)
# print("Длина прям-ка:", r1.get_length())
# print("Ширина прям-ка:", r1.get_width())
# print("Площадь:", r1.get_area())
# print("Периметр", r1.get_perimeter())
# print("Гипотенуза", r1.get_hipotenuse())
# print(r1.get_draw())

# class Point:
#     __slots__ = ["x", "y", "z"]
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(5, 10)
# p1.z = 20
# print()
# # print(p1.__dict__)  # С объектом __slots__, __dict__ использовать невозможно: Errors
# print(p1.x, p1.y, p1.z)
# # print(p1.x, p1.y)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __set_coord_x(self, x):
#         print("Вызов __setCoord_X")
#         self.__x = x
#
#     def __get_coord_x(self):
#         print("Вызов __getCoord_X")
#         return self.__x
#
#     def __del_coord_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     coord_X = property(__get_coord_x, __set_coord_x, __del_coord_x)
#
#
# p1 = Point(5, 10)
# # p1.__set_coord_x(50)
# p1.coord_X = 20.5
# print(p1.coord_X)
# del p1.coord_X
# print(p1.__dict__)


# ------------------------------------------------------------------------
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(c):
#         if isinstance(c, int) or isinstance(c, float):
#             return True
#         return False
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.deleter
#     def x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     @x.setter
#     def x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координат x должны быть числом")
#     # coordX = property(__get_coord_x, __set_coord_x, __del_coord_x)
#
#
# p1 = Point(5, "10")
# # p1.x = 50
# print(p1.x)
# del p1.x
# print(p1.__dict__)
# ------------------------------------------------------------------------


# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.__old = old
#
#     @old.deleter
#     def old(self):
#         del self.__old
#
#
# p1 = Person("Irina", 26)
# print(p1.__dict__)
# p1.name = "Igor"
# p1.old = 31
# print()
# print(p1.__dict__)
# del p1.name
# print(p1.__dict__)


# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# print(Point.get_count())
# print(p1.get_count())


# def inc(x):
#     return x + 1
#
#
# def dec(x):
#     return x - 1
#
#
# print(inc(10), dec(10))
#
#
# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
# ch1 = Change()
# print(ch1.inc(10))
# print(Change.inc(10), Change.dec(10))

# Less 23


# class Numbers:
#     @staticmethod
#     def max(a, b, c, d, ):
#         mx = a
#         if b > mx:
#             mx = b
#         if c > mx:
#             mx = c
#         if d > mx:
#             mx = d
#         return mx
#
#     @staticmethod
#     def min(*args):
#         mn = args[0]
#         for i in args:
#             if i < mn:
#                 mn = i
#         return mn
#
#     def average(*args):
#         return sum(args) / len(args)
#
#     @staticmethod
#     def factorial(n):
#         fact = 1
#         for i in range(1, n + 1):
#             fact *= i
#         return fact
#
#
# print(Numbers.max(3, 5, 7, 9))
# print(Numbers.min(3, 5, 7, 9, 1))
# print(Numbers.average(3, 5, 7, 9, 1))
# print(Numbers.factorial(5))
# print()
# lst = [5, 8, 5, 7, 4]
# print(max(lst))


# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, string_date):
#         day, month, year = map(int, string_date.split("."))
#         date1 = cls(day, month, year)
#         return date1
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#
# # string_date = "23.10.2025"
# # day, month, year = map(int, string_date.split("."))
# # print(day, month, year)
# # print(string_date.split("."))
# # date = Date(day, month, year)
#
# date = Date.from_string("23.10.2025")
# print(date.string_to_db())
#
# date2 = Date.from_string("30.12.2024")
# print(date2.string_to_db())


# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, num, surname, percent, value):
#         self.num = num
#         self.surname = surname
#         self.percent = percent
#         self.value = value
#         print(f"Счёт #{self.num} принадлежащий {self.surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счёт #{self.num} принадлежащий {self.surname} был закрыт.")
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счёта: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счёта: {eur_val} {Account.suffix_eur}")
#
#     def print_info(self):
#         print("Информация о счёте:")
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")  # .1f - флоат(вещественные) .1% - процент
#         print("-" * 20)
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print("Проценты были успешно начислены")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f"{val} {Account.suffix} было успешно снято")
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#
# acc = Account("12345", "Долгих", 0.03, 1000)
# # acc.print_balance()
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# Account.set_eur_rate(2)
# Account.set_usd_rate(3)
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# acc.edit_owner("Дюма")
# acc.print_info()
# print()
#
# acc.add_percents()
# print()
#
# acc.withdraw_money(100)
# print()
#
# acc.add_money(3000)
# print()


# import re
#
#
# class UserDate:
#     def __init__(self, fio, old, ps, weight):
#         # self.verify_fio(fio)
#         # self.verify_old(old)
#         # self.verify_weight(weight)
#         # self.verify_ps(ps)
#
#         self.fio = fio  # self.__fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()  # ['Волков', 'Игорь', 'Николаевич']
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         letter = "".join(re.findall(r"[a-za-яё-]", fio, flags=re.IGNORECASE))  # Волков Игорь Николаевич
#         for s in f:
#             # print(s.strip(letter))
#             if len(s.strip(letter)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or old < 14 or old > 100:
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 100 лет")
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError("Вес должен быть вещественным числом от 20 кг и выше")
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()  # ['1234', '567890']
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Серия и номер паспорта должны быть числами")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, year):
#         self.verify_old(year)
#         self.__old = year
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, w):
#         self.verify_weight(w)
#         self.__weight = w
#
#
# p1 = UserDate("Волков Игорь Николаевич", 26, "1234 456789", 80.8)
# p1.fio = "Волков Игорь Викторович"
# p1.old = 32
# p1.password = "2574 987456"
# p1.weight = 70.9
# print(p1.__dict__)


# lesson_24


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self) -> str:  # -> int
#         return f"({self.__x}, {self.__y})"

#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#         print("Инициализатор класса Prop")
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         print("Переопределённый инициализатор Line")
#         # Prop.__init__(self, *args)
#         super().__init__(*args)
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#
#     def draw_rect(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()
# # print(line)
# print(line._width)


# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, c):
#         super().__init__(c)
#         self.__width = width
#         self.__height = height
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if not isinstance(w, int):
#             raise TypeError("Ширина должна быть числом")
#         elif not w > 0:
#             raise ValueError("Ширина должна быть положительным числом")
#         else:
#             self.__width = w
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if isinstance(h, int) and h > 0:
#             self.__height = h
#         else:
#             raise ValueError("Высота должна быть положительным числом")
#
#     def get_area(self):
#         print(f"Площадь {self.color} прямоугольника: ", end="")
#         return self.__width * self.__height
#
#
# rect = Rectangle(10, 20, "green")
# print(rect.width)
# print(rect.height)
# print(rect.color)
# rect.width = -8
# rect.color = "red"
# print(rect.get_area())


# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"Прямоугольник:\nШирина: {self.width}\nВысота {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         self.fon = background
#         super().__init__(width, height)
#
#     def show_rect(self):
#         Rect.show_rect(self)  # super().show_rect()
#         print("Фон:", self.fon)
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, r_width, r_type, r_color):
#         super().__init__(width, height)
#         self.r_width = r_width
#         self.r_type = r_type
#         self.r_color = r_color
#
#     def show_rect(self):
#         super().show_rect()
#         print(f"Ширина рамки: {self.r_width}\nТип рамки: {self.r_type}\nЦвет рамки: {self.r_color}")
#
#
# print(Rect.__dict__)
# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
# print()
# shape2 = RectBorder(600, 300, "1px", "solid", "blue")
# shape2.show_rect()

# lesson 25
# D_Z
# from math import sqrt
#
#
# class Pair:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def edit_a(self, a):
#         self.a = a
#
#     def edit_b(self, b):
#         self.b = b
#
#     def sum(self):
#         return self.a + self.b
#
#     def mult(self):
#         return self.a * self.b
#
#
# class RightTriangle(Pair):
#     def __init__(self, a, b):
#         super().__init__(a, b)
#         self.c = self.hypotenuse()
#
#     def hypotenuse(self):
#         hypot = round(sqrt(self.a ** 2 + self.b ** 2), 2)
#         print(f"Гипотенуза АВС: {hypot}")  # hypot:.2f  служебный символ ":"
#         return hypot
#
#     def print_info(self):
#         print(f"Прямоугольный треугольник АВС: ({self.a}, {self.b}, {self.c})")
#
#     def square(self):
#         s = 0.5 * self.mult()
#         print(f"Площадь ∆ ABC: {s}")
#
#     def edit_a(self, a):
#         super().edit_a(a)
#         self.c = self.hypotenuse()
#
#     def edit_b(self, b):
#         super().edit_a(b)
#         self.c = self.hypotenuse()
#
#
# tr = RightTriangle(5, 8)
# tr.print_info()
# tr.square()
# print()
#
# print(f"Сумма: {tr.sum()}")
# print(f"Произведение: {tr.mult()}")
# print()
#
# tr.edit_a(10)
# tr.edit_b(20)
# tr.square()
# print(tr)


# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str, self))
#
#
# v = Vector([1, 2, 3])
# print(v)
# print(type(v))

# # Перегрузка методов:
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_coord(self, x=None, y=None):
#         if y is None:
#             self.x = x
#         elif x is None:
#             self.y = y
#         else:
#             self.x = x
#             self.y = y
#
#
# p1 = Point(5, 7)
# print(p1.__dict__)
# p1.set_coord(20, 30)
# print(p1.__dict__)
# p1.set_coord(50)
# print(p1.__dict__)
# p1.set_coord(y=100)
# print(p1.__dict__)
# p1.set_coord(x=120)
# print(p1.__dict__)

# Абстрактные методы

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self) -> str:
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def draw(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод draw()")
#
#
# class Line(Prop):
#
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#
#     def draw(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Ellipse(Prop):
#
#     def draw(self):
#         print(f"Рисование эллипса: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(20, 20)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellipse(Point(70, 70), Point(90, 90)))
#
# for f in figs:
#     f.draw()


# from abc import ABC, abstractmethod
#
#
# class Chess(ABC):
#     def draw(self):
#         print("Нарисовал шахматную доску")
#
#     @abstractmethod
#     def move(self):
#         print("Метод move() в базовом классе")  # pass  # ПО умолчанию метод без реализации
#
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print("Ферзь перемещён на e2e4")
#
#
# # q = Chess()
# q = Queen()
# q.draw()
# q.move()

# from math import pi
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             if length is None:
#                 self.width = self.length = width
#             else:
#                 self.width = width
#                 self.length = length
#         else:
#             self.radius = radius
#
#     def calc_area(self):
#         raise NotImplementedError("В дочернем методе должен быть определён метод 'calc_area()'")
#
#
# class SqTable(Table):
#     def calc_area(self):
#         return self.width * self.length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(pi * self.radius ** 2, 2)
#
#
# t = SqTable(20, 10)
# print(t.__dict__)
# print(t.calc_area())
#
# t1 = SqTable(20)
# print(t1.__dict__)
# print(t1.calc_area())
#
# t2 = RoundTable(radius=20)
# print(t2.__dict__)
# print(t2.calc_area())


# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     suffix = "RUB"
#
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     @abstractmethod
#     def print_value(self):
#         print(self.value, end=" ")
#
#     def print_info(self):
#         self.print_value()
#         print(f" = {self.convert_to_rub():.2f} {Currency.suffix}")
#
#
# class Dollar(Currency):  # Имплементировать - реализовывать
#     rate_to_rub = 74.16
#     suffix = "USD"
#
#     def convert_to_rub(self):
#         return self.value * Dollar.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end="")
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = "EUR"
#
#     def convert_to_rub(self):
#         return self.value * Euro.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end="")
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
#
# print("*" * 50)
# for elem in d:
#     elem.print_info()
#
# print("*" * 50)
# for elem in e:
#     elem.print_info()

#

# for elem in d:
#     elem.print_value()
#     print(f" = {elem.convert_to_rub():.2f} RUB")
#
# for elem in e:
#     elem.print_value()
#     print(f" = {elem.convert_to_rub():.2f} RUB")


# Интерфейс

# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print("Child Class")
#
#     def func(self):
#         super().func()
#         print("Child")
#
#
# class GrandChild(Child):
#     def display2(self):
#         print("GrandChild Class")
#
#     def func(self):
#         super().func()
#         print("GrandChild")
#
#
# gc = GrandChild()
# gc.display1()
# gc.display2()

# Урок 26
# Вложенные классы

# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def outer_static_method():
#         print("Метод внешнего класса")
#
#     def outer_obj_method(self):
#         print("Метод внешнего экземпляра класса", self.name)
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print("Метод вложенного класса", MyOuter.age, self.obj.name)
#             MyOuter.outer_static_method()
#             self.obj.outer_obj_method()
#
#
# out = MyOuter("внешний")
# out.outer_obj_method()
# inner = out.MyInner('внутренний', out)
# print(out.name)
# print(inner.inner_name)
# inner.inner_method()


# class Color:
#     def __init__(self):
#         self.name = "Green"
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print("Name:", self.name)
#
#     class LightGreen:
#         def __init__(self):
#             self.name = "Light Green"
#
#         def display(self):
#             print("Name:", self.name)
#
#
# outer = Color()
# outer.show()
# # print(outer.name)
# # print(outer.lg.name)
# outer.lg.display()
# g = outer.lg
# g.display()

# class Employee:
#     def __init__(self):
#         self.name = "Employee"
#         # self.intern = self.Intern()
#         # self.head = self.Head()
#
#     def show(self):
#         print("Name:", self.name)
#
#     class Head:
#         def __init__(self):
#             self.name = "Александр"
#
#         def display(self):
#             print("Name:", self.name)
#
#
# class Intern:
#     def __init__(self):
#         self.name = "Дмитрий"
#
#     def display(self):
#         print("Name:", self.name)
#
#
# outer = Employee()
# outer.show()
#
# # d1 = outer.intern
# # d2 = outer.head
# # d1 = Employee().Intern()
# d2 = Employee().Head()
#
# # d1.display()
# d2.display()


# ---------------------------
# class Outer:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print("Наружный класс")
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass()
#
#         def show(self):
#             print("Промежуточный класс")
#
#         class InnerClass:
#
#             def show(self):
#                 print("Вложенный класс")
#
#
# outer = Outer()
# outer.show()
#
# inner1 = outer.inner
# inner1.show()
#
# inner2 = outer.inner.inner_inner
# inner2.show()
# ------------------------------

# class Computer:
#     def __init__(self):
#         self.name = "PC001"
#         self.os = self.OS()
#         self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return "Windows 10"
#
#     class CPU:
#         def make(self):
#             return "Intel"
#
#         def model(self):
#             return "Core-i9"
#
#
# comp = Computer()
# my_os = comp.os
# my_cpu = comp.cpu
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())

# class Base:
#     def __init__(self):
#         self.db = self.Inner()
#
#     def display(self):
#         print("In Base Class")
#
#     class Inner:
#         def display1(self):
#             print("Inner Of Base Class")
#
#
# class SubClass(Base):
#     def __init__(self):
#         print("In Subclass")
#         super().__init__()
#
#     class Inner(Base.Inner):
#         def display2(self):
#             print("Inner Of Subclass")
#
#
# a = SubClass()
# # a.display()
# # b = a.db
# b = SubClass.Inner()
# b.display1()
# b.display2()

# if 5 > 3:  # Подчёркивание
#     a = 8
#
# print(a)

# for i in range(10):
#     a = 10
#
# print(a)

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + " is sleeping")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + " is playing")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + " is barking")
#
#
# dog = Dog("Buddy")
# dog.sleep()
# dog.play()
# dog.bark()


# class A:
#     def __init__(self):
#         print("Инициализатор класса А")
#
# class AA:
#     def __init__(self):
#         print("Инициализатор класса А")
#
#
# class B(A):
#
#     def __init__(self):
#         print("Инициализатор класса B")
#
#
# class C(AA):
#     def __init__(self):
#         print("Инициализатор класса C")
#
#
#
# class D(B, C):
#     def __init__(self):
#         print("Инициализатор класса D")
#
#
# d = D()
# print(D.mro())  # выводит последовательность наследования
# # print(D.__mro__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Styles:
#     def __init__(self, color="red", width=1):
#         print("Инициализатор Styles")
#         self.color = color
#         self.width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, *args):
#         print("Инициализатор Pos")
#         self.sp = sp
#         self.ep = ep
#         Styles.__init__(self, *args)
#         super().__init__(*args)
#
#
# class Line(Pos, Styles):
#     def drow(self):
#         print(f"Рисование линии: {self.sp}, {self.ep}, {self.color}, {self.width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), "green", 5)
# l1.drow()


#  Миксины (концепция предоставления набора доп. методов)

# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename="log_file.txt"):
#         with open(filename, "a") as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=""):
#         super().log(message, filename="log.txt")
#
#
# subclass = MySubClass()
# subclass.display("Эта строка будет печататься и записываться в файл")


# class Goods:
#     def __init__(self, name, weight, price):
#         super().__init__()
#         print("Init Goods")
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Init MixinLog")
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def save_sell_log(self):
#         print(f"{self.id}: товар был продан в 15:20")
#
#
# class Notebook(Goods, MixinLog):
#     pass
#
#
# n = Notebook("HP", 1.5, 35000)
# n.print_info()
# n.save_sell_log()


# Занятие_27
# Перегрузка операторов

# Число секунд в одном дне: 24 * 60 * 60 = 86400

# a = 5 * 2
# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.__DAY
#
#     def det_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise AttributeError("Правый оператор должен быть типом данных Clock")
#         return Clock(self.sec + other.sec)
#
#     def __eq__(self, other):
#         if not isinstance(other, Clock):
#             raise AttributeError("Правый оператор должен быть типом данных Clock")
#         # if self.sec == other.sec:
#         #     return True
#         # return False
#         return self.sec == other.sec
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#
# c1 = Clock(100)
# c2 = Clock(200)  # Clock(100)
# # c4 = Clock(300)
# # c3 = c1 + c2 + c4
# # c1 += c2
# print(c1.det_format_time())
# print(c2.det_format_time())
# # print(c4.det_format_time())
# # print(c3.det_format_time())
# # if c1 == c2:
# #     print("Время одинаковое")
# # else:
# #     print("Время разное")
#
# if c1 != c2:
#     print("Время разное")
# else:
#     print("Время одинаковое")


# class Student:
#     def __init__(self, name, *marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):  # Перегрузка квадратных скобок на получение верных данных
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Неверный индекс")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть целым положительным числом")
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)  # 10 + 1 - 5 = 6
#             self.marks.extend([None] * off)  # [5, 5, 3, 4, 5, None, None, None, None, None, None]
#
#         self.marks[key] = value  # [5, 5, 3, 4, 5, None, None, None, None, None, 4]
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("Индекс должен быть целым числом")
#         del self.marks[key]
#
#
# s1 = Student("Сергей", 5, 5, 3, 4, 5)
# print(s1[2])
# # print(s1.marks[2])
# s1[10] = 4
# print(s1.marks)
# del s1[2]
# print(s1.marks)
#
# # lst = [5, 5, 3, 4, 5]
# # off = 10 + 1 - len(lst)
# # print([None] * off)
# # lst.extend([None] * off)
# # print(lst)
# # print(off)


# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.__DAY
#
#     def det_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#         if item == "hour":
#             return (self.sec // 3600) % 24
#         if item == "min":
#             return (self.sec // 60) % 60
#         if item == "sec":
#             return self.sec % 60
#         return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#         if not isinstance(value, int):
#             raise ValueError("Значение должно быть целым числом")
#
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#
#         if key == "hour":
#             self.sec = s + 60 * m + value * 3600
#         if key == "min":
#             self.sec = s + 60 * value + h * 3600
#         if key == "sec":
#             self.sec = value + 60 * m + h * 3600
#
#
# c1 = Clock(8000)
# print(c1.det_format_time())
# print(c1["hour"], c1["min"], c1["sec"])
# c1["hour"] = 10
# print(c1.det_format_time())
# c1["min"] = 62
# print(c1.det_format_time())
# c1["sec"] = 70
# print(c1.det_format_time())


# class Point:
#     def __init__(self, x):
#         self.x = x
#
#     # def __str__(self):
#     #     return f"{self.x}"
#
#     def __repr__(self):
#         return f"<{self.__class__}> {self.x}"
#
#
# p1 = Point([5, 4, 6])
# print(p1)


# from random import choice, randint
#
#
# class Cat:
#     def __init__(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol
#
#     def __str__(self):
#         if self.pol == "M":
#             return f"{self.name} is good boy!!!"
#         elif self.pol == "F":
#             return f"{self.name} is good girl!!!"
#         else:
#             return f"{self.name} is good kitty!!!"
#
#     def __repr__(self):
#         return f"Cat(name='{self.name}', age='{self.age}', pol='{self.pol}')"
#
#     def __add__(self, other):
#         if self.pol != other.pol:
#             return [Cat("No name", 0, choice(["M", "F"])) for _ in range(1, randint(2, 6))]  # range(1, 6)
#         else:
#             raise TypeError("Types are not supported")
#
#
# cat1 = Cat("Tom", 4, "M")
# cat2 = Cat("Elsa", 5, "F")
# # cat3 = Cat("Murzic", 3, "R")
# print(cat1)
# print(cat2)
# # print(cat3)
# print(cat1 + cat2)


# lesson_28
# class Point:
#     def __init__(self, *args):
#         self.__coord = args
#
#     def __len__(self):
#         return len(self.__coord)
#
#
# p = Point(1, 2, 3)
# print(len(p))

# import math

# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# p1 = Point(1, 2)
# print(p1.length)


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt1 = Point(1, 2)
# pt2 = Point2D(1, 2)
# print(pt1.__sizeof__())
# print(pt2.__sizeof__() + pt2.__dict__.__sizeof__())


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = ('z',)
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
# p = Point(1, 2)
# p3 = Point3D(10, 20, 30)
# # p3.z = 30
# print(p3.z)


# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return self.value + int(a)
#
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return len(self.value + str(a))
#
#
# t1 = Number(10)
# t2 = Text("Python")
# print(t1.total(35))
# print(t2.total(35))


# class Animal:
#     def __init__(self, name, age):
#         if not isinstance(age, (int, float)):
#             raise TypeError("int, float")
#         self.name = name
#         self.age = age
#
#
# class Cat(Animal):
#     def info(self):
#         print(f"Я кот. Меня зовут {self.name}. Мой возраст {self.age}")
#
#     def make_sound(self):
#         print(f"{self.name} мяукает")
#
#
# class Dog(Animal):
#     def info(self):
#         print(f"Я собака. Меня зовут {self.name}. Мой возраст {self.age}")
#
#     def make_sound(self):
#         print(f"{self.name} гавкает")
#
#
# cat = Cat("Пушок", 2.5)
# dog = Dog("Мухтар", 4)
#
# for animal in cat, dog:
#     animal.info()
#     animal.make_sound()


# Функторы
# class Counter:
#     def __init__(self):
#         self.__count = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__count += 1
#         print(self.__count)
#
#
# c1 = Counter()
# c1()
# c1()
# c1()


# def string_strip(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return string.strip(chars)
#
#     return wrap
#
#
# s1 = string_strip("?:!.; ")
# print(s1("  Hello World!   ...   "))
#
#
# class StringStrip:
#     def __init__(self, chars):
#         self.chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return args[0].strip(self.chars)
#
#
# s2 = StringStrip("?:!.; ")
# print(s1("  Hello World!   ...   "))

# -----------------------------------------------
# class MyDecorator:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, fn):
#         def wrap(*args, **kwargs):
#             res = fn(*args, **kwargs)
#             return f"Перед вызовом функции\n{self.name}\n{res}\nПосле вызова функции"
#
#         return wrap
#
#
# @MyDecorator("test2")
# def func(a, b):
#     return a * b  # print("taxt")
#
#
# # @MyDecorator
# # def func1(a, b, c):
# #     return a * b * c  # print("taxt")
#
#
# # func()
# print(func(2, 5))


# print(func1(2, 5, 3))

# -----------------------------------------------
# class Power:
#     def __init__(self, fn):
#         self.func = fn
#
#     def __call__(self, a, b):
#         return self.func(a, b) ** 2
#
#
# @Power
# def mult(a, b):
#     return a * b
#
#
# print(mult(2, 3))

# -----------------------------------------------$$$$$$$$$$$
# class Power:
#     def __init__(self, fn):
#         self.func = fn
#
#     def __call__(self, a, b):
#         return self.func(a, b) ** 2
#
#
# @Power
# def mult(a, b):
#     return a * b
#
#
# print(mult(2, 3))


# class MyDecorator:
#     def __init__(self, fn):
#         self.func = fn
#
#     def __call__(self, *args, **kwargs):
#         res = self.func(*args, **kwargs)
#         return f"Перед вызовом функции\n{res}\nПосле вызова функции"
#
#
# @MyDecorator
# def func(a, b):
#     return a * b
#
#
# @MyDecorator
# def func1(a, b, c):
#     return a * b * c
#
#
# print(func(2, 5))
# print(func1(2, 5, 2))


# -----------------------------------------------$$$$$$$$$$$
# Декорирование методов

# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f"{self.name}, {self.surname}")
#
#
# p1 = Person("Виталий", "Карасев")
# p1.info()


# Декораторы классов

# def decorator(cls):
#     class Wrapper(cls):
#         def sample(self, value):
#             return value * 2
#
#     return Wrapper
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print("Init ActualClass")
#
#     def method_in_class(self, value):
#         return value * 4
#
#
# obj = ActualClass()
# print(obj.method_in_class(4))
# print(obj.sample(4))


# Метаклассы

# a = 5
# print(type(a))
# print(type(int))

# class MyList(list):
#     def get_length(self):
#         return len(self)


# MyList = type(
#     'MyList',
#     (list,),
#     dict(get_length=lambda self: len(self))
# )
#
# lst = MyList()
# lst.append(5)
# lst.append(7)
# print(lst, lst.get_length())

# Объектно-ориентированное закончено


# Создание модулей


# import geometry.rect  # sq, trian
# import geometry.sq
# import geometry.trian

# from geometry import rect, sq, trian

# from geometry import *
#
#
# def ran():
#     r1 = rect.Rectangle(1, 2)
#     r2 = rect.Rectangle(3, 4)
#
#     s1 = sq.Square(10)
#     s2 = sq.Square(20)
#
#     t1 = trian.Triangl(1, 2, 3)
#     t2 = trian.Triangl(4, 5, 6)
#
#     shape = [r1, r2, s1, s2, t1, t2]
#
#     for g in shape:
#         print(g.get_perimeter())
#
#
# if __name__ == "__main__":
#     ran()

# from car.electro_car import ElectroCar
# # def ran():
# if __name__ == "__main__":
#     e_car = ElectroCar("Tesla", "T", 2018,
#                        99000, 100)
#     e_car.show_car()
#     e_car.description_battery()

# Упаковка (Сериализация) и распаковка (Десериализация) данных.

# import pickle
#
# filename = "basket.txt"
#
# shop = {
#     "фрукты": ["яблоко", "груша"],
#     "овощи": ("морковь", "лук"),
#     "бюджет": 1000
# }
#
# with open(filename, "wb") as fn:
#     pickle.dump(shop, fn)
#
# with open(filename, "rb") as fn:
#     shop_list = pickle.load(fn)
#
#
# print(shop_list)

# import pickle


# class Test:
#     num = 25
#     string = "Привет"
#     lst = [1, 2, 3]
#     dictionary = {"first": 1, "second": 2}
#
#     def __str__(self):
#         return f"Число: {Test.num}\nСтрока: {Test.string}\nСписок: {Test.lst}\nСловарь: {Test.dictionary}"
#
#
# obj = Test()
# # print(obj)
#
# obj1 = pickle.dumps(obj)
# print(f"Сериализация в строку:\n{obj1}\n")
#
# obj2 = pickle.loads(obj1)
# print(f"Десериализация из строки:\n{obj2}\n")

# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = "test"
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# print(item1)
# item2 = pickle.dumps(item1)
# print(item2)
# item3 = pickle.loads(item2)
# print(item3)
# print(item3.__dict__)

# import json
#
# data = {
#     'name': 'Olga',
#     'age': 35,
#     '20': None,
#     'True': False,
#     'hobbies': ('running', 'string'),
#     'children': [
#         {
#             'firstName': 'Alice',
#             'age': 6
#         }
#
#     ],
# }
#
# # with open('data_file.json', 'w') as fw:
# #     json.dump(data, fw)
# #
# # with open('data_file.json', 'r') as fw:
# #     data1 = json.load(fw)
# #
# # print(data1)
#
# json_string = json.dumps(data, sort_keys=True)  # False
# print(json_string)
# print(type(json_string))
# data2 = json.loads(json_string)
# print(data2)
# print(type(data2))

# x = {"name": "Виктор"}
#
# # print(json.dumps(x))
# # print(json.dumps(x, ensure_ascii=False))
# #
# # a =json.dumps(x)
# # print(json.loads(a))
#
# with open('data_file1.json', 'w') as  fw:
#     json.dump(x, fw, ensure_ascii=False)
#
# with open('data_file1.json', 'r') as  fw:
#     data2 = json.load(fw)
#
# print(data2)


# import json
# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'k', 'l', 'm', 'n']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#     # print(name)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#     # print(tel)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#
#     return person
#
#
# def write_json(person_dict):
#     try:
#         data = json.load(open("persons.json"))
#     except FileNotFoundError:
#         data = []
#
#     data.append(person_dict)
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(gen_person())
#
# # persons = []
# # for i in range(5):
# #     persons.append(gen_person())
# # print(persons)


# import json
# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'k', 'l', 'm', 'n']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#     # print(name)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#     # print(tel)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#
#     return person, tel
#
#
# def write_json(person_dict, num):  # {"name": "...",
#     try:
#         data = json.load(open("persons.json"))
#     except FileNotFoundError:
#         data = {}
#
#     data[num] = person_dict
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(gen_person()[0], gen_person()[1])


# Lesson 30 (30_04_2025)

# import json
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         # st = ''
#         # for i in self.marks:
#         #     st += str(i) + ", "
#         # return f"Студент: => {self.name}: {st[:-2]}"
#         st = ', '.join(map(str, self.marks))
#         return f"Студент: => {self.name}: {st}"
#
#     def add_mark(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_marks(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         return round(sum(self.marks) / len(self.marks), 2)
#
#     def dump_to_json(self):
#         data = {"name": self.name, "marks": self.marks}
#         with open(self.get_file_name(), "w") as f:
#             json.dump(data, f)
#
#     def get_file_name(self):
#         return self.name + ".json"
#
#     def load_from_file(self):
#         with open(self.get_file_name(), "r") as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         st = "\n".join(map(str, self.students))
#         return f"\nГруппа: {self.group}\n{st}"
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @staticmethod
#     def change_group(gr1, gr2, index):
#         return gr2.add_student(gr1.remove_student(index))
#
#     def get_file_name(self):
#         return self.group.lower().replace(" ", "-") + ".json"
#
#     def dump_to_json(self):
#         data = [{"name": student.name, 'marks': student.marks} for student in self.students]
#         with open(self.get_file_name(), "w") as f:
#             json.dump(data, f, indent=2)
#
#     def load_from_file(self):
#         with open(self.get_file_name(), "r") as f:
#             json.load(f)
#
#
# st1 = Student("Bodnya", [5, 4, 3, 4, 5, 3])
# # print(st1)
# # st1.add_mark(4)
# # print(st1)
# # st1.delete_mark(3)
# # print(st1)
# # st1.edit_marks(2, 4)
# # print(st1)
# # st1.average_mark()
# # print(st1)
#
# st2 = Student("Nikolaenko", [5, 4, 3, 4, 5, 3])
# st3 = Student("Birucov", [5, 4, 3, 4, 5, 3])
# # st1.dump_to_json()
# # st1.load_from_file()
# sts1 = [st1, st2]
# group1 = Group(sts1, "ГК Python")
# # # print(group1)
# # # print()
# # group1.add_student(st3)
# # # print(group1)
# # # print()
# # group1.remove_student(1)
# # # print(group1)
# sts2 = [st2]
# group2 = Group(sts2, "ГК WEB")
# # print(group1)
# # print(group2)
# Group.change_group(group1, group2, 0)
# print(group1)
# print(group2)
# group2.dump_to_json()
# group2.load_from_file()


# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# # print(response)
# # print(response.text)
# # print(type(response.text))
# # todos = json.loads(response.text)
# # print(todos)
# # print(type(todos[0]))
#
# todos_by_user = {}
#
# for todo in todos:
#     if todo["completed"]:
#         try:
#             todos_by_user[todo["userId"]] += 1
#         except KeyError:
#             todos_by_user[todo["userId"]] = 1
#
# print(todos_by_user)
#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)
#
# max_complete = top_users[0][1]
# print(max_complete)
#
# users = []
# for user, num_complete in top_users:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
#
# # users = ['11']
# print(users)
#
# max_users = " and ".join(users)
# print(max_users)
#
# # max_users = '11'
# e = "s" if len(users) > 1 else ""
# print(f"User{e} {max_users} completed {max_complete} TODOs")

# Lesson 31 (12_05_2025)

# # *************************************************************************************
# # -- coding: utf8 --.
# import json
#
#
# class CountryCapital:
#     @staticmethod
#     def load(file_name):
#         try:
#             data = json.load(open(file_name))  # , encoding="utf-8": в моём случае эта строка не вписывается в Load
#         except FileNotFoundError:
#             data = {}
#         finally:
#             return data
#
#     @staticmethod
#     def add_country(file_name):
#         new_country = input("Введите название страны: ").lower()
#         new_capital = input("Введите название столицы: ").lower()
#
#         # try:
#         #     data = json.load(open(file_name, encoding="utf-8"))
#         # except FileNotFoundError:
#         #     data = {}
#         data = CountryCapital.load(file_name)
#
#         data[new_country] = new_capital
#
#         with open(file_name, "w") as f:
#             json.dump(data, f, indent=2, ensure_ascii=False)
#
#     @staticmethod
#     def load_from_file(file_name):
#         with open(file_name) as f:
#             print({k.title(): v.title() for k, v in json.load(f).items()})
#
#     @staticmethod
#     def delete_country(file_name):
#         del_country = input("Введите название страны: ").lower()
#
#         # try:
#         #     data = json.load(open(file_name, encoding="utf-8"))
#         # except FileNotFoundError:
#         #     data = {}
#         data = CountryCapital.load(file_name)
#
#         if del_country in data:
#             del data[del_country]
#
#             with open(file_name, "w") as f:
#                 json.dump(data, f, indent=2, ensure_ascii=False)
#         else:
#             print("Такой страны в базе нет")
#
#     @staticmethod
#     def search_data(file_name):
#         country = input("Введите название страны: ").lower()
#
#         # try:
#         #     data = json.load(open(file_name, encoding="utf-8"))
#         # except FileNotFoundError:
#         #     data = {}
#         data = CountryCapital.load(file_name)
#
#         if country in data:
#             print(f"Страны {country.title()} столица {data[country].title()} есть в словаре")
#         else:
#             print(f"Страны {country.title()} нет в словаре")
#
#     @staticmethod
#     def edit_data(file_name):
#         country = input("Введите страну для корректировки: ").lower()
#         new_capital = input("Введите новое название столицы: ").lower()
#
#         # try:
#         #     data = json.load(open(file_name, encoding="utf-8"))
#         # except FileNotFoundError:
#         #     data = {}
#         data = CountryCapital.load(file_name)
#
#         if country in data:
#             data[country] = new_capital
#
#             with open(file_name, "w") as f:
#                 json.dump(data, f, indent=2, ensure_ascii=False)
#         else:
#             print("Такой страны в базе нет")
#
#
# file = "list_capital.json"
# while True:
#     index = input("Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n"
#                   "4 - редактирование данных\n5 - просмотр данных\n6 - завершение работы\n"
#                   "Ввод: ")
#     if index == "1":
#         CountryCapital.add_country(file)
#     elif index == "2":
#         CountryCapital.delete_country(file)
#     elif index == "3":
#         CountryCapital.search_data(file)
#     elif index == "4":
#         CountryCapital.edit_data(file)
#     elif index == "5":
#         CountryCapital.load_from_file(file)
#     elif index == "6":
#         break
#     else:
#         print("Введен некорректный номер")
#
#     print("*" * 50)
# # *************************************************************************************

# import csv

# with open("data.csv") as f:
#     file_reader = csv.reader(f, delimiter=";")
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {", ".join(row)}")
#         else:
#             print(f"\t{row[0]} - {row[1]}. Родился в {row[2]} году")
#         count += 1
#     print(f"Всего в файле {count} строки.")
#     # print(row)  # => csv
#     # print(file_reader)

# with open("data.csv") as f:
#     fields = ["Имя", "Профессия", "Год рождения"]
#     file_reader = csv.DictReader(f, delimiter=";", fieldnames=fields)
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {", ".join(row)}")
#         print(f"\t{row["Имя"]} - {row["Профессия"]}. Родился в {row["Год рождения"]} году")
#         # print(row)
#         count += 1
#     print(f"Всего в файле {count} строки.")

# import csv

# with open("student.csv", "w") as f:  # , encoding='utf-8'
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(["Женя", "9", "15"])
#     writer.writerow(["Саша", "5", "12"])
#     writer.writerow(["Маша", "11", "18"])


# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open("sw_data.csv", "w") as f:  # , encoding='utf-8'
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)
#
# with open("sw_data.csv", "r") as f:
#     print(f.read())


# import csv

# with open("stud.csv", "w") as f:
#     names = ["Имя", "Возраст"]
#     file_writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=names)
#     file_writer.writeheader()
#     file_writer.writerow({"Имя": "Саша", "Возраст": 6})
#     file_writer.writerow({"Имя": "Маша", "Возраст": 15})
#     file_writer.writerow({"Имя": "Вова", "Возраст": 14})

# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open("dict_writer.csv", "w") as f:
#     writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=data[0].keys())
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)

# print(data[0].keys())

# Для DZ_31:
# requests(https://jsonplaceholder.typicode.com/todos)

# import requests
#
# url = 'https://api.binance.com/api/v3/ticker/price'
#
# #{"symbol":"ETHUSDT","price":"2773.30000000"}
#
# respons = requests.get(url)
