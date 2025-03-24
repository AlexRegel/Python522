# DZ_10
print("Создание двумерного словаря произведено"
      " предварительно и закомментировано. Словарь распакован:")
"""
DZ_10 Задача (7.JPG)
Разработка программы для создания и изменения словаря.
отражающего данные объёма продаж пользователей по регионам.
"""

# # Создаём начальный список. Задаём кол-во имён (по умолч.- 4) и вводим имена пользователей:
# lst_users = [input(f"Имя {i+1}: ") for i in range(4)]  # int(input("Введите кол-во имён: n = "))
# print("Создан список имён пользователей: lst_users =", lst_users, end="\n")
# lst_region = [input(f"Регион {i+1}: ") for i in range(4)]  # int(input("Введите кол-во регионов: n = "))
# print("Создан список регионов: lst_region =", lst_region, end="\n")
# print("Создание начального двумерного словаря.")
# b_dict = {}
# for name in lst_users:    # lst = ["John", "Tom", "Anne", "Fiona"]
#     print(f"Ввод начального объём продаж пользователя {name} по регионам:")
#     b_dict[name] = {ir: int(input(f"В регионе {ir}: ")) for ir in lst_region}   # ["N", "S", "E", "W"]
# print()
# print("Создан словарь: \n", b_dict, end="\n\n")

# Итак, создан словарь (введены данные по задаче):
b_dict = {
    'John': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
    'Tom': {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
    'Anne': {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
    'Fiona': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}
}

# Распакуем (по заданию) двумерный словарь:
for name, nest_d in b_dict.items():  # Распаковка словаря с выводом имён пользователей.
    print(name, ": ", sep="")   # , nest_d
    for reg, sal in nest_d.items():  # Распаковка подсловаря с выводом регионов и объёма пр-ж.
        print(reg, ": ", sal, sep="")

# Запрос к базе словаря с получением результата
# по объёму продаж пользователя "user_name" в регионе region
user_name = input("Имя: ")
try:
    if b_dict[user_name]:
        pass  # print("Найдено Имя:", user_name)
    region = input("Регион: ")
    try:
        if b_dict[user_name][region]:
            print(b_dict[user_name][region])  # Объём продаж
        try:
            sales = int(input("Новое значение: "))
            b_dict[user_name][region] = sales  # Присвоение нового значения продаж
            print(b_dict[user_name])
        except ValueError:
            print("Значение не корректно. Перезапустите ПО и введите целое число.")
    except KeyError:
        print(f"Региона \"{region}\" в словаре не найдено.")
except KeyError:
    print(f"Имя пользователя {user_name} в словаре отсутствует.")

