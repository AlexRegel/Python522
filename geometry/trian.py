# -- coding: utf8 --.
class Triangl:
    def __init__(self, a, b, c, ):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        return "Треугольник:", self.a + self.b + self.c


if __name__ == "__main__":
    t1 = Triangl(2, 2, 3)
    print(t1.get_perimeter())

# print(__name__)
