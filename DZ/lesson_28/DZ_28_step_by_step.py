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
        # print(f"Площадь {self.color} прямоугольника: ", end="")
        return self.width * self.length

    def get_perimeter(self):  # Периметр
        return 2 * (self.width + self.length)

    # def get_draw(self):  # Рисование
    #     print(('*' * self.width + '\n') * self.length)

    def get_draw(self):
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
        print("=" * 40)


rect = Rectangle(3, 7)  # , "green"
print(rect.length)
rect.set_color = "yellow"  # цвет можно также присвоить через сеттер ("yellow") или оставить по умолчанию ("red")
# rect.set_color("yellow")
print(rect.color)
rect.width = 8
print(rect.width)
# rect.color = "red"
print(rect.get_area())

rect.print_info()
# rect.get_draw()

# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimeter(self):
#         return 4 * self.a
#
#
# class Triangl:
#     def __init__(self, a, b, c, ):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimeter(self):
#         return self.a + self.b + self.c
#
#     @abstractmethod
#     def get_area(self):
#         pass
#
#     @abstractmethod
#     def get_draw(self):
#         pass
#
#     # @property
#     # def color(self):
#     #     return self.__color
#     #
#     # @color.setter
#     # def color(self, c):
#     #     self.__color = c
#
#     # Для вырисовывания линий:
#     def print_info(self):
#         print(f" Данные ".center(40, "*"))
#         print("=" * 40)
