# -- coding: utf8 --.
# country_lst = []
# # if country_lst == []:
# #     s = 5
# #     print(s)
# # else:
# #     print(False)
# index_ = 1  # None
# country_lst.append(2)
# s = True  # 7
# print(country_lst) if country_lst and not (index_ is None) else print(False)  # not in None
# print(s) if country_lst and not (index_ is None) else print(False)  # not in None
#
# # Negative is element:
# # if val != None:
# # if not (val is None):
# # if val is not None:

country_lst = [
    {"Россия": "Москва"}, {"Франция": "Париж"}, {"Франция": "Париж"},
    {"Эстония": "Таллин"}, {"Япония": "Токио"}]
print(len(country_lst))
print("Базовый словарь:", country_lst)
print()
# k = "Франция"
# count_ = 0
# for element in country_lst:
#     country_dict = element
#     count_ += 1
#     print("Type словаря:", type(country_dict))
#     for key_dict in country_dict.keys():
#         print(f"Проход: ключ словаря: {key_dict}, тип: {type(key_dict)}")
#         print(f"Ключ извне словаря: {k}, тип: {type(k)}")  # str(country_dict.keys())[12:-3]
#         if key_dict == k:
#             remote_dict_in_lst = country_lst.pop(count_ - 1)
#             print(f"Из файла 'country.json' удалён словарь: {remote_dict_in_lst}")
# print()
# print("В итоге имеем словарь:", country_lst)
key_ = {"Франция": "Париж"}

print(True, "Отсутствует в коллекции") if key_ not in country_lst else print(False,
                                                                             "Присутствует в коллекции")  # not in None
print()
print()

# unpack_lst_country = *country_lst
# print(unpack_lst_country)

print(*country_lst)
print(country_lst)

# class Experiment:
#     # def __init__(self, ext):  # : list
#     #     self.ext = ext
#
#     def unpack_lst(self, lst):
#         ert = Experiment(*lst)
#         print(ert)
#
#
# e = Experiment(country_lst)
# print(e.unpack_lst(country_lst))
# # Experiment.unpack_lst(country_lst)

country_lst = [
    {"Россия": "Москва"}, {"Франция": "Париж"}, {"Франция": "Париж"},
    {"Эстония": "Таллин"}, {"Япония": "Токио"}]

for i, t in enumerate(country_lst, 1):
    print(i, t)

numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(first)  # 1
print(middle)  # [2, 3, 4]
print(last)  # 5
*mi, las = numbers
print(mi)
