# DZ_28. Задание:
# Создать класс Shape и три дочерних класса: Square, Rectangle, Triangle.
# Родительский класс должен иметь абстрактные методы нахождения периметра, площади,
# рисования фигуры и вывода информации.
# С помощью полиморфизма реализуйте вывод информации о дочерних фигурах.
#
# ===Квадрат===
# Сторона: 3
# Цвет: red
# Площадь: 9
# Периметр; 12
# ***
# ***
# ***
# ===Прямоугольник===
# Длина: 3
# Ширина: 7
# Цвет: green
# Площадь: 21
# Периметр: 20
# *******
# *******
# *******
# ===Треугольник===
# Сторона 1: 11
# Сторона 2: 6
# Сторона 3: 6
# Цвет: yellow
# Площадь: 13.19
# Периметр: 11.5 ???

from abc import ABC, abstractmethod
from math import sqrt


class Shape(ABC):  # Figure
    def __init__(self, color="red"):
        self.color = color
        # self.value = value

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_draw(self):  # Для вырисовывания линий
        pass

    # @abstractmethod
    # def color(self):
    #     return self.color

    # @abstractmethod
    def set_color(self, c):
        self.color = c

    @abstractmethod
    def print_info(self):
        pass
        # print(f" Данные ".center(40, "*"))
        # print("=" * 40)


class Rectangle(Shape):  # Дочерний класс - прямоугольник
    hw = len("Прямоугольник") + 6  # Общая ширина заголовка с разметкой (header width) для "print_info"

    def __init__(self, length, width, c=None):  # c - color
        if c is None:
            super().__init__()
        else:
            super().__init__(c)
        self.width = width
        self.length = length

    @property
    def set_color(self):  # Геттер цвета прямоугольника (PyCharm 2024.1.4 подсвечивает, но работоспособен)
        return self.color

    @set_color.setter
    def set_color(self, c):  # Сеттер цвета прямоугольника
        self.color = c

    def get_area(self):  # Площадь
        return self.width * self.length

    def get_perimeter(self):  # Периметр
        return 2 * (self.width + self.length)

    def get_draw(self):  # Рисование
        for _ in range(self.length):
            print("*" * self.width)
        print()

    #     def print_value(self):
    #         super().print_value()
    def print_info(self):
        print(
            f"Прямоугольник".center(Rectangle.hw, "="), "\n",  # __width: 19
            f"Длина: {self.length}\nШирина: {self.width}\n"  # вывод информации о длине, ширине 
            f"Цвет: {self.color}\nПлощадь: {self.get_area()}\n"  # цвете, площади
            f"Периметр: {self.get_perimeter()}", sep=""  # и периметре прямоугольника
        )
        Rectangle.get_draw(self)
        # print("=" * Rectangle.hw)


class Triangle(Shape):  # Дочерний класс - треугольник. Подразумеваем - равнобедренный треугольник
    hw = len("Треугольник") + 6  # Общая ширина заголовка с разметкой (header width) для "print_info"
    h = None  # создадим свойство (переменная) высоты при условии равнобедренности треугольника
    temper_var = []  # создали спец. список для вырисовывания треугольника
    temper_dict = {}  # создали спец. словарь для контроля вырисовывания треугольника
    rel_lst_1 = []  # соотносительные списки "relative list" (для контроля ввода данных)
    rel_lst_2 = []  # b получения спец словаря
    data_control_dict = {1: 1, 3: 2, 5: 3, 7: 4, 9: 5, 11: 6, 13: 7, 15: 8, 17: 9, 19: 10, 21: 11}

    def __init__(self, side_1: int, side_2=None, side_3=None, c=None):  # c - color
        if c is None:
            super().__init__()
        else:
            super().__init__(c)
        # соотношение side_1/side2: 1, 1 | 3, 2 | 5, 3 | 7, 4 | 9, 5 | 11, 6 | 13, 7 | 15, 8 | 17, 9
        if Triangle.data_control_dict and (side_1 not in Triangle.data_control_dict.keys()):
            raise AttributeError("Неверный тип данных: Для рисования треугольника сторона 1 вводится из прогрессии.")
        elif side_1 in Triangle.data_control_dict.keys():  # Основание треугольника
            self.side_1 = side_1 if isinstance(side_1, int) else 1
        else:
            self.side_1 = side_1 if isinstance(side_1, int) else print("Сторона 1: Учесть прогрессию."
                                                                       " Для рисования треугольника вводится число!")
        # self.side_1 = side_1
        if side_2 is None:
            if self.side_1 in Triangle.data_control_dict.keys():
                for i, j in Triangle.data_control_dict.items():
                    if self.side_1 == i:
                        self.side_2 = j  # self.side_2 = side_2  # Стороны треугольника
        else:
            self.side_2 = side_2
        # print("Сторона 2: Установите целое число!")  #
        if side_3 is None:  # Условие для равнобедренного треугольника
            self.side_3 = self.side_2  # Одна из сторон равнобедренного треугольника
        if side_3 is not None:
            raise AttributeError("Неверный тип данных: Для равнобедренного треугольника сторона 3 не вводится")
        # print("Внимание: Треугольник подразумевается равнобедренный. Сторона 3 не вводится.") if (
        #             self.side_2 != self.side_3) else ...
        # Заполнение словаря для контроля входных данных сторон тре-ка для последующего вырисовывания треугольника
        for i in range(1, self.side_1 + 3, 2):
            Triangle.rel_lst_1.append(i)
        for i in range(1, self.side_2 + 2):
            Triangle.rel_lst_2.append(i)
        for key in range(len(Triangle.rel_lst_1)):
            for value in range(len(Triangle.rel_lst_2)):
                if value == key:
                    Triangle.temper_dict[Triangle.rel_lst_1[key]] = Triangle.rel_lst_2[value]
        for key, value in Triangle.temper_dict.items():
            if key == side_1:
                self.side_2 = value

    @property
    def set_color(self):
        return self.color

    @set_color.setter
    def set_color(self, c):
        self.color = c

    def get_perimeter(self):
        return self.side_1 + self.side_2 + self.side_3

    def get_area(self):
        Triangle.h = sqrt(self.side_2 ** 2 - (self.side_1 / 2) ** 2)  # 0.5 *
        return round((self.side_1 * Triangle.h) / 2, 2)

    # соотношение side_1/side2:  1, 1 | 3, 2 | 5, 3 | 7, 4 | 9, 5 | 11, 6 | 13, 7 | 15, 8 | 17, 9
    def get_draw(self):  # Вырисовывание фигуры
        for i in range(1, self.side_1 + 1, 2):
            Triangle.temper_var.append(i)
        for i in range(0, self.side_2 + 1):
            if i <= len(Triangle.temper_var) - 1:
                print(f"{"*" * Triangle.temper_var[i]}".center(self.side_1, " "), end="\n")  # width: 11
        print()

    def print_info(self):
        print(
            f"Треугольник".center(Triangle.hw, "="), "\n",
            f"Сторона 1: {self.side_1}\nСторона 2: {self.side_2}\nСторона 3: {self.side_3}\n"
            f"Цвет: {self.color}\nПлощадь: {self.get_area()}\n"
            f"Периметр: {self.get_perimeter()}", sep=""
        )
        Triangle.get_draw(self)
        # print(f"У треугольника Сторона 1: {self.side_1},\tсторона 2: {self.side_2}")

        # print("=" * Triangle.hw, end="\n\n")
        # print()
        # print(Triangle.rel_lst_1)
        # print("=" * 40)
        # print(Triangle.rel_lst_2)
        # print("=" * 40)
        # print(Triangle.temper_dict)


class Square(Shape):
    hw = len("Квадрат") + 6  # Общая ширина заголовка с разметкой (header width) для "print_info"

    def __init__(self, side, c=None):
        if c is None:
            super().__init__()
        else:
            super().__init__(c)
        self.side = side

    @property
    def set_color(self):
        return self.color

    @set_color.setter
    def set_color(self, c):
        self.color = c

    def get_perimeter(self):
        return self.side * 4

    def get_area(self):
        return self.side ** 2

    # соотношение side_1/side2:  1, 1 | 3, 2 | 5, 3 | 7, 4 | 9, 5 | 11, 6 | 13, 7 | 15, 8 | 17, 9
    def get_draw(self):  # Вырисовывание квадрата
        for _ in range(self.side):
            print("*" * self.side)
        print()

    def print_info(self):
        print(
            f"Квадрат".center(Square.hw, "="), "\n",  # __width: 19
            f"Сторона: {self.side}\nЦвет: {self.color}\nПлощадь: {self.get_area()}\n"
            f"Периметр: {self.get_perimeter()}", sep=""
        )
        Square.get_draw(self)


# Реализация методов квадрата
sq = Square(3, "red")
# sq.set_color = "yellow"
# print(sq.color)
# print(sq.get_area())
# print(sq.get_perimeter())
# sq.get_draw()
# sq.print_info()

# Реализация методов прямоугольника
rect = Rectangle(3, 7, "green")  # , "green"
# print(rect.length)
# rect.set_color = "yellow"  # цвет можно также присвоить через сеттер ("yellow") или оставить по умолчанию ("red")
# print(rect.color)
# print(rect.get_area())
# rect.print_info()
# rect.get_draw()

# Реализация методов треугольника
# соотношение side_1/side2, во избежании ошибок при вырисовывании вводится строго в соответствии со словарём:
# data_control_dict {1: 1, 3: 2, 5: 3, 7: 4, 9: 5, 11: 6, 13: 7, 15: 8, 17: 9, 19: 10, 21: 11},
# где ключ key == side_1, а значение value = side_2
# Таким образом, side_1 вводить из словаря "data_control_dict",
# либо,с side_2, из этой прогрессии. Тогда закомментировать строки кода с 126 по 132:
tri = Triangle(11, c="yellow")  # side_2 - можно не вводить, если в рамках прогрессии "data_control_dict"
# print(tri.get_perimeter())
# print(tri.get_area())
# tri.set_color = "blue"
# tri.print_info()
# tri.get_draw()

shape = [sq, rect, tri]
for g in shape:
    g.print_info()
