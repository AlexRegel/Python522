# -- coding: utf8 --.
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_perimeter(self):
        return "Прямоугольник:", 2 * (self.w + self.h)


__author__ = "admin"
if __name__ == "__main__":
    print(f"Module {__name__} (author: {__author__})")

# print(__name__)
#
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
