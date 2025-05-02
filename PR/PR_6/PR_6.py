# # -- coding: utf8 --.


data_control_dict = {1: 1, 3: 2, 5: 3, 7: 4, 9: 5, 11: 6, 13: 7, 15: 8, 17: 9, 19: 10, 21: 11}

side_2 = None
side_1 = 13

if side_2 is None:
    if side_1 in data_control_dict.keys():
        print(True)
    else:
        print(False)

for i, j in data_control_dict.items():
    side_2 = j if side_1 == i else ...
print()

person = {'name': 'Иван', 'age': 30, 'city': 'Москва'}

for key in person:
    print(f"Ключ: {key}")

# for key in person.keys():
#      add(f"Ключ: {1}")   ????????????
print()

list_to_tuple = tuple([8, 9, 10])
print(list_to_tuple)
