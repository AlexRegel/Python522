# -- coding: utf8 --.

data_control_dict = {1: 1, 3: 2, 5: 3, 7: 4, 9: 5, 11: 6, 13: 7, 15: 8, 17: 9, 19: 10, 21: 11}
side_3 = None
side_2 = None
side_1 = 13
items = 0

if side_2 is None:
    if side_1 in data_control_dict:  # .keys()
        for key, value in data_control_dict.items():
            print(f"Ключ: {key}, Значение: {value}")
            if side_1 == key:
                side_2 = value  # self.side_2 = side_2  # Стороны треугольника
        print(side_2, type(side_2))
        print(True)
        items = data_control_dict.items()
        print(items)
    else:
        print(False)

print(side_2, type(side_2))
