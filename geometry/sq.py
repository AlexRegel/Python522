# -- coding: utf8 --.
# Строка 5735 в 'main': Импорт модуля (from geometry import rect, sq, trian)
class Square:
    def __init__(self, a):
        self.a = a

    def get_perimeter(self):
        return 'Квадрат:', 4 * self.a


# if __name__ == :
s1 = Square(10)
s2 = Square(20)

# print(s1.get_perimeter())
# print(s2.get_perimeter())

# print(__name__)
