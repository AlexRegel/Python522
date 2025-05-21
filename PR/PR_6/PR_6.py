# -- coding: utf8 --.
import json

# employees = dict()
# employees[(1, "Alice")] = {"position": "Manager", "skills": {"leadership", "communication"}}
# employees[(2, "Bob")] = {"position": "Developer", "skills": {"python", "databases"}}
#
# for (id, name), info in employees.items():
#     print(f"Сотрудник {id}: {name}")
#     print(f"id-type {type(id)}:name-type {type(name)}")
#     print(f"Должность: {info['position']}")
#     print(f"type(info['position']): {type(info['position'])}, type('position') {type('position')}")
#     print(f"Навыки: {', '.join(info['skills'])}")
#     print(f"skills-type: {type(', '.join(info['skills']))}")
#
# print(employees)
# print(type(employees))
w = """=============================================================================="""

"""
Задача 1:
Уровень 1: Базовый
Задача: создайте кортеж из нескольких строк, затем напишите программу, которая:

Определяет количество элементов в кортеже.
Проверяет, содержится ли в кортеже заданная строка (вводится пользователем).
Выводит первый и последний элемент кортежа."""

# tuple_1 = ("Определяет количество элементов в кортеже.",
#            "Проверяет, содержится ли в кортеже заданная строка (вводится пользователем).",
#            "Выводит первый и последний элемент кортежа."
#            )
#
# a_ = "Определяет количество элементов в кортеже."
# a = len(tuple_1)
# print("Длина кортежа:", a)
#
# b = "Проверяет, содержится ли в кортеже заданная строка (вводится пользователем)."
# b_ = input("Введите строку: ")
# s_n = b_ in tuple_1
# print("Содержится.") if s_n else print("Данная строка в кортеже отсутствует.")
#
# c_ = "Выводит первый и последний элемент кортежа."
# first_element = tuple_1[0]
# last_element = tuple_1[-1]
# print("Первый элемент кортежа 'tuple_1':", first_element)
# print("Последний элемент кортежа 'tuple_1':", last_element)

w1 = """=============================================================================="""

"""
Задача 2:
Уровень 2: Средний

Задача: напишите программу, которая позволяет пользователю управлять списком 
своих любимых жанров с использованием словаря. Каждый жанр должен быть ключом,
а значением — кортеж с двумя элементами: годом,
когда жанр стал любимым, и кратким описанием жанра."""

genres_dict = {"Боевые искусства": (1995, "Фильмы про восточные боевые искусства"),
               "Астрофизика": (2003, "док. Фильмы про вселенную")}

# sr = json.dumps(genres_dict, indent=2)  # ensure_ascii=False,
# genres_d = json.loads(sr)
# print(genres_d)
# # a =json.dumps(x)
# # print(json.loads(a))

# Срезы списка
d = [
    {
        "Россия": "Москва"
    },
    {
        "Франция": "Париж"
    },
    {
        "Эстония": "Таллин"
    },
    {
        "Египет": "Каир"
    },
    {
        "Израиль": "Иерусалим"
    },
    {
        "Япония": "Токио"
    }
]
print(d[2])
print(d[4]["Израиль"])

w2 = """=============================================================================="""

"""
Задача 3:
Уровень 3: Продвинутый

Задача: напишите программу, которая использует словарь для управления списком сотрудников и их должностей.
Пользователь может добавлять новых сотрудников, удалять их по имени и просматривать список всех сотрудников с 
должностями."""

employees = dict()
employees[(1, "Alice")] = {"position": "Manager", "skills": {"leadership", "communication"}}
employees[(2, "Bob")] = {"position": "Developer", "skills": {"python", "databases"}}

for (id, name), info in employees.items():
    print(f"Сотрудник {id}: {name}")
    print(f"id-type {type(id)}:name-type {type(name)}")
    print(f"Должность: {info['position']}")
    print(f"type(info['position']): {type(info['position'])}, type('position') {type('position')}")
    print(f"Навыки: {', '.join(info['skills'])}")
    print(f"skills-type: {type(', '.join(info['skills']))}")

print(employees)
print(type(employees))
print()
print(employees.values())
print()
for key, values in employees.items():
    print(key, values)
