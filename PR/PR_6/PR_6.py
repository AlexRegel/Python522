# -- coding: utf8 --.

# class Triangle(Shape):  # Дочерний класс - треугольник. Подразумеваем - равнобедренный треугольник
#     hw = len("Треугольник") + 6  # Общая ширина заголовка с разметкой (header width) для "print_info"
#     h = None  # создадим свойство (переменная) высоты при условии равнобедренности треугольника
#     temper_var = []  # создали спец. список для вырисовывания треугольника
#     temper_dict = {}  # создали спец. словарь для контроля вырисовывания треугольника
#     rel_lst_1 = []  # соотносительные списки "relative list" (для контроля ввода данных)
#     rel_lst_2 = []  # b получения спец словаря
#     data_control_dict = {1: 1, 3: 2, 5: 3, 7: 4, 9: 5, 11: 6, 13: 7, 15: 8, 17: 9, 19: 10, 21: 11}
#
#
#     def __init__(self, side_1: int, side_2=None, side_3=None, c=None):  # c - color
#         if c is None:
#             super().__init__()
#         else:
#             super().__init__(c)
#         # соотношение side_1/side2: 1, 1 | 3, 2 | 5, 3 | 7, 4 | 9, 5 | 11, 6 | 13, 7 | 15, 8 | 17, 9
#         self.side_1 = side_1 if isinstance(side_1, int) else ...  # Основание треугольника
#         # print("Сторона 1: Установите целое число!")
#         # if side_2 is None:
#         # if self.side_1 in Triangle.data_control_dict.keys():
#         #     for i, j in Triangle.data_control_dict.items():
#         #         self.side_2 = j if self.side_1 == i else ...  # self.side_2 = side_2  # Стороны треугольника
#         # else:
#         self.side_2 = side_2
#         # print("Сторона 2: Установите целое число!")  #
#         if side_3 is None:  # Условие для равнобедренного треугольника
#             self.side_3 = self.side_2  # Одна из сторон равнобедренного треугольника
#         if side_3 is not None:
#             raise AttributeError("Неверный тип данных: Для равнобедренного треугольника сторона 3 не вводится")
#         # print("Внимание: Треугольник подразумевается равнобедренный. Сторона 3 не вводится.") if (
#         #             self.side_2 != self.side_3) else ...
#         # Заполнение словаря для контроля входных данных сторон тре-ка для последующего вырисовывания треугольника
#         for i in range(1, self.side_1 + 3, 2):
#             Triangle.rel_lst_1.append(i)
#         for i in range(1, self.side_2 + 2):
#             Triangle.rel_lst_2.append(i)
#         for key in range(len(Triangle.rel_lst_1)):
#             for value in range(len(Triangle.rel_lst_2)):
#                 if value == key:
#                     Triangle.temper_dict[Triangle.rel_lst_1[key]] = Triangle.rel_lst_2[value]
#         for key, value in Triangle.temper_dict.items():
#             if key == side_1:
#                 self.side_2 = value

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


