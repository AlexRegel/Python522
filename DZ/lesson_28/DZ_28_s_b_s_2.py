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
# Периметр: 11.5

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

    #     def print_value(self):
    #         super().print_value()
    def print_info(self):
        print(
            f"Прямоугольник".center(Rectangle.hw, "="), "\n",  # __width: 19
            f"Длина: {self.length}\nШирина: {self.width}\n"  # вывод информации о длине, ширине 
            f"Цвет: {self.color}\nПлощадь: {self.get_area()}\n"  # цвете, площади
            f"Периметр: {self.get_perimeter()}"  # и периметре прямоугольника
        )
        Rectangle.get_draw(self)
        print("=" * Rectangle.hw)


class Triangl(Shape):  # Дочерний класс - треугольник. Подразумеваем - равнобедренный треугольник
    hw = len("Треугольник") + 6  # Общая ширина заголовка с разметкой (header width) для "print_info"
    h = None  # создадим свойство (переменная) высоты при условии равнобедренности треугольника
    temper_var = []  # создали спец. список для вырисовывания треугольника
    temper_dict = {}  # создали спец. словарь для вырисовывания треугольника
    rel_lst_1 = []  # соотносительные списки "relative list" (для контроля ввода данных)
    rel_lst_2 = []

    def __init__(self, side_1: int, side_2: int, side_3=None, c=None):  # c - color
        if c is None:
            super().__init__()
        else:
            super().__init__(c)
        # соотношение side_1/side2: 1, 1 | 3, 2 | 5, 3 | 7, 4 | 9, 5 | 11, 6 | 13, 7 | 15, 8 | 17, 9
        self.side_1 = side_1 if isinstance(side_1, int) else print(
            "Сторона 1: Установите целое число!")  # Основание треугольника
        self.side_2 = side_2 if isinstance(side_2, int) else print("Сторона 2: Установите целое число!")  #
        if side_3 is None:  # Условие для равнобедренного треугольника
            self.side_3 = self.side_2 = side_2  # Одна из сторон равнобедренного треугольника
        else:
            self.side_3 = side_3
            print("Внимание: треугольник не равнобедренный") if (self.side_2 != self.side_3) else ...
        for i in range(1, self.side_1 + 3, 2):
            Triangl.rel_lst_1.append(i)
        for i in range(1, self.side_2 + 2):
            Triangl.rel_lst_2.append(i)
        for key in range(len(Triangl.rel_lst_1)):  # for key in range(len(Triangl.rel_lst_1)):
            for value in range(len(Triangl.rel_lst_2)):
                if value == key:
                    Triangl.temper_dict[Triangl.rel_lst_1[key]] = Triangl.rel_lst_2[value]  # Triangl.rel_lst_1[key]

    def get_perimeter(self):
        return self.side_1 + self.side_2 + self.side_3

    def get_area(self):
        Triangl.h = sqrt(self.side_2 ** 2 - (self.side_1 / 2) ** 2)  # 0.5 *
        # print(Triangl.h)
        return round((self.side_1 * Triangl.h) / 2, 2)

    # соотношение side_1/side2: 9, 5 | 11, 6 | 13, 7 | 15, 8 | 17, 9
    def get_draw(self):  # Рисование
        # pass
        # temper_dict[] =
        for i in range(1, self.side_1 + 1, 2):
            Triangl.temper_var.append(i)
        for i in range(0, self.side_2 + 1):
            if i <= len(Triangl.temper_var) - 1:
                print(f"{"*" * Triangl.temper_var[i]}".center(self.side_1, " "), end="\n")  # width: 11
            # else:
            # print(f"{"*" * Triangl.temper_var[i]}".center(11, " "), end="\n")
            # print("*" * self.width)

    # @property
    # def color(self):
    #     return self.__color
    #
    # @color.setter
    # def color(self, c):
    #     self.__color = c

    # Для вырисовывания линий:
    def print_info(self):
        pass  # print(f" Данные ".center(40, "*"))
        print(Triangl.rel_lst_1)
        print("=" * 40)
        print(Triangl.rel_lst_2)
        print("=" * 40)
        print(Triangl.temper_dict)


# Реализация методов треугольника
tri = Triangl(3, 2)  # соотношение side_1/side2: 9, 5 | 11, 6 | 15, 8 | 13, 7
print(tri.get_perimeter())
print(tri.get_area())
tri.get_draw()
tri.print_info()

# # Реализация методов прямоугольника
# rect = Rectangle(3, 7, "green")  # , "green"
# print(rect.length)
# # rect.set_color = "yellow"  # цвет можно также присвоить через сеттер ("yellow") или оставить по умолчанию ("red")
# print(rect.color)
# print(rect.get_area())
# rect.print_info()
# # rect.get_draw()

# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimeter(self):
#         return 4 * self.a
