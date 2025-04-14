# DZ_24. Задание:
# Создать класс "Pair" (пара чисел) со свойствами: числа А и В,
# -и методами: изменение чисел, вычисление их произведения и суммы.
#
# Определить производный класс "Right Triangle" (прямоугольный треугольник)
# со свойствами: катеты A и B - и методами: вычисление гипотенузы и площади
# треугольника, вывод информации о фигуре на экран.
#
# Продемонстрировать работу класса-наследника и всех его методов.
#
# Гипотенуза ∆ ABC: 9.43
# Прямоугольный треугольник ∆ ABC: (5, 8, 9.43)
# Площадь ∆ ABC: 20.0

# Сумма: 13
# Произведение: 40
# ... .

# print(chr(8710))
# print(ord("∆"))


class Pair:  # Родительский класс
    def __init__(self, a=5, b=8):  # Инициализация чисел a=5, b=8
        if not isinstance((a and b), (int or float)):
            raise TypeError("Параметры 'a' и 'b' должны быть числами")
        self._a = a
        self._b = b

    def __check_value(c):
        if isinstance(c, int) or isinstance(c, float):
            return True
        return False

    # Создадим геттеры и сеттеры для изменения параметров (используя декораторы)
    @property
    def edit_a(self):  # "геттер"(get), возвращающий элемент a
        return self._a

    @edit_a.setter
    def edit_a(self, a):  # "сеттер"(set), устанавливающий новое значение a
        self._a = a if Pair.__check_value(a) else print("Параметр 'a' должен быть числом")

    @property
    def edit_b(self):  # "геттер"(get), возвращающий элемент b
        return self._b

    @edit_b.setter  # Декоратор метода set (edit_b)
    def edit_b(self, b):  # "сеттер"(set), устанавливающий новое значение элемента b
        self._b = b if Pair.__check_value(b) else print("Параметр 'b' должен быть числом")

    # Методы нахождения суммы и произведения чисел
    def sum_ab(self):
        print(f"Сумма a({self._a}) и b({self._b}): {self._a + self._b}")

    def prod_ab(self):
        print(f"Произведение (a({self._a}), b({self._b})): {self._a * self._b}")


# Производный класс (класс-наследник) со свойствами прямоугольного треугольника:
class RightTriangle(Pair):

    def __init__(self, a=5, b=8, c=9.43):  # c=9.43 (по умолчанию)
        print('Параметр "c" вводить не требуется') if c != 9.43 else None
        self._c = c  # инициализируем параметр гипотенузы, для дальнейших манипуляций и использования в методах
        super().__init__(a, b)

    def hypotenuse(self):
        if not isinstance((self._a and self._b), (int or float)):
            raise TypeError("Параметры 'a' и 'b' должны быть числами")
        self._c = round(((self._a ** 2 + self._b ** 2) ** 0.5), 2)
        print(f"Гипотенуза ∆ ABC: {self._c}")

    def r_triangle(self):
        print(f"Прямоугольный треугольник ∆ ABC: ({self._a}, {self._b}, {self._c})")

    def area(self):
        print(f"Площадь ∆ ABC: {(self._a * self._b) / 2}")


# Проверка работоспособности класса-наследника (RightTriangle) родительского класса (Pair), их методов:
print("Класс-наследник 'RightTriangle()' и его методы:\n")
rt = RightTriangle()
rt.hypotenuse()
rt.r_triangle()
rt.area()
print()
print("Родительский класс (Pair), его методы:\n")
pe = Pair()  # По умолчанию в родительском методе a=5, b=8
pe.sum_ab()
pe.prod_ab()
pe.edit_a = 18
pe.edit_b = 22
print("a =", pe.edit_a)
print("b =", pe.edit_b)
pe.sum_ab()
pe.prod_ab()
print()
print("Класс-наследник 'RightTriangle()' и его методы (повторно):\n")
rt = RightTriangle()  # Также можно ввести параметры катетов, напр. a=12, b=15
rt.edit_a = 14
rt.edit_b = 20
print("a =", rt.edit_a)
print("b =", rt.edit_b)
rt.sum_ab()
rt.prod_ab()
rt.hypotenuse()
rt.r_triangle()
rt.area()
print()
rt.edit_a = 16
rt.hypotenuse()
rt.edit_b = 28
rt.hypotenuse()
rt.sum_ab()
rt.prod_ab()
rt.area()
