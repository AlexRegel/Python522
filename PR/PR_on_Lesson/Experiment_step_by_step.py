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

k = "Франция"
count_ = 0
for element in country_lst:
    country_dict = element
    count_ += 1
    print("Type словаря:", type(country_dict))
    for key_dict, value_dict in country_dict.items():
        print(f"Проход: ключ словаря: {key_dict}, тип: {type(key_dict)}")
        print(f"Ключ иной словаря: {str(country_dict.keys())[12:-3]}, тип: {type(str(country_dict.keys()))}")
        if key_dict == str(country_dict.keys())[12:-3]:
            remote_dict_in_lst = country_lst.pop(count_ - 1)
            print(f"Из файла 'country.json' удалён словарь: {remote_dict_in_lst}")
print()
print("В итоге имеем словарь:", country_lst)
