import json

# data_control_dict = {1: 1, 3: 2, 5: 3, 7: 4, 9: 5, 11: 6, 13: 7, 15: 8, 17: 9, 19: 10, 21: 11}
#
# side_2 = None
# side_1 = 13
#
# if side_2 is None:
#     if side_1 in data_control_dict.values():  # .keys()
#         print(True)
#     else:
#         print(False)
#
# for i, j in data_control_dict.items():
#     side_2 = j if side_1 == i else ...
# print()

person = {'name': 'Иван', 'age': 30, 'city': 'Москва'}


# for key, value in person.items():
#     print(f"Ключ: {key}")
#     print(f"Значение: {value}")
#     if key == 'age':
#         person[key] = 35
#
# # person.keys('name').capitalize()
#
# # .capitalize()
# print()
# print(f"Новое значение: {person['age']}")
# print()
# print(len(person))
# person['name'] = 'Сергей'
# person['country'] = 'Россия'
# print(len(person))
# print(person)
#
# # for key in person.keys():
# #      add(f"Ключ: {1}")   ????????????
# print()
#
# list_to_tuple = tuple([8, 9, 10])
# print(list_to_tuple)
#
# print(type(str(person.keys()).capitalize()))
# print(str(person.values()).capitalize())
# print(person.values())
# print(type(person.values()))
#
# e = 'москва'
# r = e.capitalize()
# print(r)

def add_data(country):  # add
    try:
        with open('person.json', 'r') as fr:  # , encoding='utf-8'
            country_dict_lst = json.load(fr)
    except FileNotFoundError:
        country_dict_lst = []
        print(type(country_dict_lst))

    # data = [{"name": student.name, 'marks': student.marks} for student in self.students]
    print(type(country_dict_lst))
    country_dict_lst.append(country)
    with open('person.json', 'w') as fw:  # , encoding='utf-8'
        json.dump(country_dict_lst, fw, ensure_ascii=False, indent=4)
    stack = json.dumps(country_dict_lst, ensure_ascii=False, indent=4)
    # print(stack)
    print(json.loads(stack))


# comment = r'\u041d\u0435 \u0443\u043a\u0430\u0437\u0430\u043d\u043e'
# print(type(comment))
# print(comment)
# print(comment.encode('ascii').decode('unicode-escape'))

# person = {'name': 'Иван', 'age': 30, 'city': 'Москва'}
person2 = {'name': 'Сергей', 'age': 25, 'city': 'Питер'}
add_data(person)
add_data(person2)
