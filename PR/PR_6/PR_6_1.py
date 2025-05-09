# -- coding: utf8 --.
import json

# country_dict_lst = []  # создали пустой список для хранения словарей
# country_dict = dict()  # создали пустой словарь для стран и столиц

country_dict = {'Россия': 'Москва'}
country_dict_lst = [
    {'Россия': 'Москва'}, {'USA': 'Вашингтон'},
    {'Польша': 'Варшава'}, {'Китай': 'Пекин'}, {'Россия': 'Москва'}
]

print(country_dict_lst.count(country_dict))  # возвращает количество вхождений элемента item в список
print(country_dict)
print(len(country_dict))
print(country_dict_lst)
print("Длина начального списка:", len(country_dict_lst))
print(f"0-вой элемента словаря 'country_dict_lst': {country_dict_lst[0]}")
print()

# if country_dict not in country_dict_lst:
#     print(True)
# else:
#     print(False)
# print()
# a = [1, 2, 3, 4, 2, 8, 4, 2, 7, 6, 1, 2]
# print(a)
# if 2 in a:
#     print(True)
# else:
#     print(False)
# print(a.count(2))
#
# if len(country_dict) == 0:
#     country_dict[cou_] = cap_
# else:
#     while len(country_dict) == 0:
#         country_dict.pop()
#
count = 0  # Счётчик для ликвидации вхождений > 1
# criterion = {}
for index in range(len(country_dict_lst)):
    print(country_dict_lst[index])
    if country_dict_lst.count(country_dict_lst[index]) > 1:
        count += 1
        print(f"Прибавили, count = {count}")
        if count > 1:
            criterion = country_dict_lst.pop(index)
            print(f"Удалили из списка словарь {criterion}, его тип: {type(criterion)}, dlina: {len(criterion)}")  # criterion
            print("Итоговый список теперь выглядит так:: ", country_dict_lst)
            print("Его тип правильный, т.е.: ", type(country_dict_lst), ", длина: ", len(country_dict_lst), sep="")
            if criterion != country_dict:
                country_dict_lst.append(country_dict)
print()
print()
print(country_dict_lst.count(country_dict))
print()
print("0-й элемент:", country_dict_lst.count(country_dict_lst[0]))
print("1-й элемент:", country_dict_lst.count(country_dict_lst[1]))
print("2-й элемент:", country_dict_lst.count(country_dict_lst[2]))
print("3-й элемент:", country_dict_lst.count(country_dict_lst[3]))
# print("4-й элемент:", country_dict_lst.count(country_dict_lst[4]))
print()

# Подобный код с рабочего файла, что вырезал (не потребовался):
# def __init__(self, country_, capital_):  # Country - страна, Capital - столица
#     self.country_ = country_
#     self.capital_ = capital_

# def __check_value(c):
#     if isinstance(c, str):
#         return True
#     return False
#
# @staticmethod
# def set_capital(country_, capital_):  # Метод получения и проверки новых значений страны и столицы
#     cou_ = country_ if Country.__check_value(country_) else print(f"Параметр {country_} должен быть строкой")
#     cap_ = capital_.capitalize() if Country.__check_value(capital_) else print(
#         f"Параметр {capital_} должен быть строкой")
#     if len(Country.country_dict) == 0:
#         Country.country_dict[cou_] = cap_
#     else:
#         while len(Country.country_dict) == 0:
#             Country.country_dict.pop()
#     Country.country_dict_lst.append(Country.country_dict)
#
#     count = 0
#     # criterion = {}
#     for index in range(len(Country.country_dict_lst) - 1):
#         if Country.country_dict_lst.count(Country.country_dict) > 1:
#             count += 1
#             if count > 1:
#                 criterion = Country.country_dict_lst.pop(index)
#                 print(criterion, type(criterion))
#     # if criterion not in Country.country_dict_lst:
#     #     Country.country_dict_lst.append(Country.country_dict)
#     if Country.country_dict not in Country.country_dict_lst:
#         Country.country_dict_lst.append(Country.country_dict)
#     return Country.country_dict_lst
