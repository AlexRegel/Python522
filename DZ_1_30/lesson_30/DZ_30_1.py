# -- coding: utf8 --.
# DZ_30. Задание:
# Есть некоторый словарь, который хранит название страны и столиц.
# Название стран используется в качестве ключа, название столицы в качестве значения.
# Необходимо реализовать: добавление, удаление, поиск, редактирование и просмотр данных.
# (Используя упаковку и распаковку данных)
# ******************************

import json


class Country:  # Класс создания и хранения списка словарей стран и их столиц
    country_lst = []  # создали пустой список для хранения словарей
    country_dict = dict()  # создали пустой словарь для стран и столиц. Словарь - это 1 элемент списка.
    remote_dict_in_lst = dict()  # создали пустой словарь для присвоения удаляемого элемента списка
    search_dict_in_lst = dict()  # создали пустой словарь для присвоения элемента списка при поиске
    file_name = 'country.json'  # Country.file_name

    @staticmethod
    def load(file_name):
        try:  # , encoding="utf-8": в моём случае эта строка не вписывается в Load
            with open(Country.file_name) as fr:
                Country.country_lst = json.load(fr)
        except FileNotFoundError:
            Country.country_lst = []
        finally:
            return Country.country_lst

    # Country.country_lst = Country.load()
    @staticmethod
    def add_data(country_tuple):  # add, country_tuple
        # try:
        #     with open(Country.file_name) as fr:  # ', 'r'' - при чтении файла это не обязательный параметр
        #         Country.country_lst = json.load(fr)
        # except FileNotFoundError:
        #     Country.country_lst = []

        Country.country_lst = Country.load(Country.file_name)  # Использование стат. функции load() -5 строк кода

        Country.country_dict[country_tuple[0]] = country_tuple[1]  # Заполнение словаря как 1-го элемента списка
        Country.country_lst.append(Country.country_dict)  # Добавление словаря в список
        # print(Country.country_lst)
        with open(Country.file_name, 'w') as fw:
            json.dump(Country.country_lst, fw, ensure_ascii=False, indent=2)
        print("Файл сохранён.")
        print(f"*".center(30, "*"))
        Country.country_dict.clear()  # Важно произвести очистку словаря, для исключения накопления в нём коллекции
        Country.country_lst.clear()
        del country_tuple

    @staticmethod
    def remove_data(index_=None, key_=None):  # remove
        # try:
        #     with open('country.json', 'r') as fr:
        #         Country.country_lst = json.load(fr)
        # except FileNotFoundError:
        #     Country.country_lst = []
        Country.country_lst = Country.load(Country.file_name)  # Использование стат. функции load() -5 строк кода

        if Country.country_lst and not (index_ is None):
            remote_dict_in_lst = Country.country_lst.pop(index_)
            print(f"Из файла {Country.file_name} удалён словарь: {remote_dict_in_lst}")
        elif Country.country_lst and not (key_ is None):
            count_ = 0  # Чтобы индексы не перебирать, перегружая код, создали счётчик, в качестве индекса
            for element in Country.country_lst:
                Country.country_dict = element
                count_ += 1
                for key_dict in Country.country_dict.keys():
                    if key_dict == key_:
                        Country.remote_dict_in_lst.clear()
                        Country.remote_dict_in_lst = Country.country_lst.pop(count_ - 1)
                        # print(f"Из файла 'country.json' удалён словарь: {Country.remote_dict_in_lst}")
        elif not Country.country_lst:
            print("Нельзя удалить элемент из пустого списка (файл отсутствовал).")
        else:
            print("Необходимо указать индекс или ключ (явно, напр.: key_='Франция'), для поиска удаляемого элемента.")
        print(f"В итоге, из файла 'country.json' удалён словарь: {Country.remote_dict_in_lst}")
        print("Список после удаления элемента:", Country.country_lst)
        with open('country.json', 'w') as fw:
            json.dump(Country.country_lst, fw, ensure_ascii=False, indent=2)
        print("Файл сохранён.")
        print(f"*".center(30, "*"))
        Country.country_dict.clear()  # Важно произвести очистку словаря, для исключения накопления в нём коллекции
        Country.country_lst.clear()

    @staticmethod
    def search_data(key_=None, index_=None):  # search
        try:
            with open('country.json', 'r') as fr:
                Country.country_lst = json.load(fr)
        except FileNotFoundError:
            Country.country_lst = []

        if Country.country_lst and not (index_ is None):  # index_ - Индекс списка словарей (полученный из файла)
            Country.search_dict_in_lst = Country.country_lst[index_]  # type - dict
            print(type(Country.search_dict_in_lst))
            print(f"В файле 'country.json' найден словарь: {Country.country_dict}")
        elif Country.country_lst and not (key_ is None):  # key_ - Страна, т.е. ключ словаря, взятого из списка файла
            count_ = 0  # Чтобы индексы не перебирать, перегружая код, создали счётчик, в качестве индекса lst
            for element in Country.country_lst:
                Country.country_dict = element  # Присвоение пустому словарю элемента списка (словаря) при переборе к.
                count_ += 1
                if key_ in Country.country_dict:
                    for key_dict, value_dict in Country.country_dict.items():
                        if key_dict == key_:
                            print(Country.country_dict)
                            Country.search_dict_in_lst.clear()
                            Country.search_dict_in_lst = Country.country_dict
                            print(f"Найдена страна: {key_dict}, и её столица: {value_dict}")
                if key_ not in Country.country_dict and len(
                        Country.country_lst) == count_ and not Country.search_dict_in_lst:
                    print("Искомая информация в файле не найдена.")
        elif not Country.country_lst:
            print("Поиск не выполнен. Файл отсутствует.")
        else:
            print("Необходимо указать индекс или ключ (явно, напр.: key_='Франция'), для поиска элемента.")
        print(f"*".center(30, "*"))
        Country.country_dict.clear()  # Важно произвести очистку словаря, для исключения накопления в нём коллекции
        Country.country_lst.clear()

    @staticmethod
    def edit_data(country_=None, new_capital_=None):  # new_capital - значение для ввода новой столицы
        try:
            with open('country.json', 'r') as fr:
                Country.country_lst = json.load(fr)
        except FileNotFoundError:
            Country.country_lst = []

        if Country.country_lst and not (country_ is None):  # country_ - Страна, т.е. ключ словаря, взятого из файла
            count_ = 0  # Чтобы индексы не перебирать, перегружая код, создали счётчик, в качестве индекса lst
            for element in Country.country_lst:
                Country.country_dict = element  # Присвоение пустому словарю элемента списка (словаря) при переборе к.
                count_ += 1
                if country_ in Country.country_dict:
                    for key_dict, value_dict in Country.country_dict.items():
                        if key_dict == country_:
                            Country.country_dict[country_] = new_capital_
                            print(Country.country_dict)
                            print(f"Для страны: {key_dict}, новое наименование столицы: {new_capital_}")
                            Country.search_dict_in_lst.clear()  # print(f"Ключ: {key}, Значение: {value}")
                            Country.search_dict_in_lst = Country.country_dict
                if country_ not in Country.country_dict and len(
                        Country.country_lst) == count_ and not Country.search_dict_in_lst:
                    print("Искомая информация в файле не найдена.")
        elif not Country.country_lst:
            print("Поиск не выполнен. Файл отсутствует.")
        else:
            print("Необходимо указать индекс или ключ (явно, напр.: key_='Франция'), для поиска элемента.")
        # print("Отредактированный список для файла:", Country.country_lst)
        with open('country.json', 'w') as fw:
            json.dump(Country.country_lst, fw, ensure_ascii=False, indent=2)
        print("Файл сохранён.")
        print(f"*".center(30, "*"))
        Country.country_dict.clear()  # Важно произвести очистку словаря, для исключения накопления в нём коллекции
        Country.country_lst.clear()

    r5 = """Временная разделяющая активная строка-переменная"""

    @staticmethod
    def view_data():  # new_capital - значение для ввода новой столицы
        try:
            with open('country.json', 'r') as fr:
                Country.country_lst = json.load(fr)
        except FileNotFoundError:
            Country.country_lst = []
        print(f"*".center(30, "*"))
        if Country.country_lst:
            print("Содержимое файла прочитано: \n", Country.country_lst)
        print(f"*".center(30, "*"))


# Проверка работоспособности методов:
# # r = Country.set_capital("Россия", "Москва")
# # r1 = Country.set_capital("USA", "вАШИНГТОН")
# # r2 = Country.set_capital("Польша", "ВАРШАВА")
# # r3 = Country.set_capital("Китай", "ПЕКИН")
# # print(r)
# # print(r1)
# # print(r2)
# # print(r3)

# Country.add_data(("Эстония", "Таллин"))  # ("Россия", "Москва"), ("Франция", "Париж")
"""разделитель"""
# # Country.add_data(("Китай", "Пекин"))
# # Country.add_data(("Польша", "Варшава"))
# # Country.add_data(("США", "Вашингтон"))
#
# t = [("Россия", "Москва"), ("Китай", "Пекин"), ("Польша", "Варшава"), ("США", "Вашингтон")]
#
# for i in range(len(t)):
#     s = type(t[i])
#     print(s)
#     Country.add_data(t[i])
"""разделитель"""
# Country.remove_data(key_="Эстония")
"""разделитель"""
# Country.search_data(key_="Франция")  # key_="Япония"
# Country.remove_data(index_=-1)
"""разделитель"""
# Country.edit_data("Россия", "Санкт-петербург")
"""разделитель"""
# Country.view_data()

# Код предложения выбора вариантов пользователю:

try:
    while True:
        action = int(input(  # номер действия
            "Выбор действия (введите целое число в интервале от 1 до 6):\n1 - добавление данных"
            "\n2 - удаление данных\n3 - поиск данных\n4 - редактирование данных (только столицы)"
            "\n5 - просмотр данных\n6 - завершение работы\nВведите цифру: "))
        if action == 1:
            country = input(
                "Введите название страны (с заглавной буквы): ")
            capital = input("Введите название столицы страны (с заглавной буквы): ")
            country_tuple_ = (country.capitalize(), capital.capitalize())  # Например: ("Эстония", "Таллин")
            Country.add_data(country_tuple_)
        if action == 2:
            country = input("Введите название страны для удаления: ")
            Country.remove_data(key_=country.capitalize())
        if action == 3:
            country = input("Введите название страны для поиска: ")
            Country.search_data(key_=country.capitalize())
            # items = countre_capital_dict.items() - возвращает объект с парами (ключ, значение)
        if action == 4:
            country = input("Введите название страны, столицу которой требуется отредактировать: ")
            new_capital = input("Введите новое (изменённое) наименование столицы: ")
            Country.edit_data(country.capitalize(), new_capital.capitalize())
        if action == 5:
            Country.view_data()
        if action == 6:
            print("\tЗавершение работы программы.")
            print(f"*".center(40, "*"))
            break  # Цикл работает пока пользователь не введёт 6.
        if action < 1 or 6 < action:
            print("Предлагается выбрать только одну из цифр в интервале от 1-го до 6-ти")
except ValueError:
    print("Ошибка!!! Пожалуйста перезапустите программу и введите только цифру.")

#  Заметки

# из занятия взять на вооружение неповторияемость try / except

# Создать метод:
# @staticmethod
# def load(file_name):
#     try:
#         data = json.load(open(file_name))  # , encoding="utf-8": в моём случае эта строка не вписывается в Load
#     except FileNotFoundError:
#         data = {}
#     finally:
#         return data
#
# # Во все другие методы, где требуется этот код, вставить следующее выражение:
#         data = CountryCapital.load(file_name)

# 2-й подход, рассматривался на уроке:
# *************************************************************************************
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
# *************************************************************************************
