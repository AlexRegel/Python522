# DZ_27. Задание:
# На базе класса, написанного на занятии (class Clock):
# 1. Перегрузить операторы: '-', '*', '//', '%'
# 2. Перегрузить операторы: '>', '>=', '<', '<='

# Число секунд в одном дне: 24 * 60 * 60 = 86400

class Clock:
    __DAY = 86400

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        self.sec = sec % self.__DAY

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise AttributeError("Правый оператор должен быть типом данных Clock")
        return Clock(self.sec + other.sec)

    def __eq__(self, other):
        if not isinstance(other, Clock):
            raise AttributeError("Правый оператор должен быть типом данных Clock")
        # if self.sec == other.sec:
        #     return True
        # return False
        return self.sec == other.sec

    def __ne__(self, other):
        return not self.__eq__(other)

    def __sub__(self, other):  # Магический метод вычитания '-'
        if not isinstance(other, Clock):
            raise AttributeError("Правый оператор должен быть типом данных Clock")
        return Clock(self.sec - other.sec)

    def __mul__(self, other):  # Магический метод умножения '*'
        if not isinstance(other, Clock):
            raise AttributeError("Правый оператор должен быть типом данных Clock")
        return Clock(self.sec * other.sec)

    def __floordiv__(self, other):  # Магический метод целочисленного деления '//'
        if not isinstance(other, Clock):
            raise AttributeError("Правый оператор должен быть типом данных Clock")
        return Clock(self.sec // other.sec)

    def __mod__(self, other):  # Магический метод получения остатка от деления '%'
        if not isinstance(other, Clock):
            raise AttributeError("Правый оператор должен быть типом данных Clock")
        return Clock(self.sec % other.sec)

    def __lt__(self, other):  # Магический метод сравнения '<'
        if not isinstance(other, Clock):
            raise AttributeError("Правый оператор должен быть типом данных Clock")
        return self.sec < other.sec

    def __le__(self, other):  # Магический метод сравнения '<='
        if not isinstance(other, Clock):
            raise AttributeError("Правый оператор должен быть типом данных Clock")
        return self.sec <= other.sec

    def __gt__(self, other):  # Магический метод сравнения '>'
        if not isinstance(other, Clock):
            raise AttributeError("Правый оператор должен быть типом данных Clock")
        return self.sec > other.sec

    def __ge__(self, other):  # Магический метод сравнения '>='
        if not isinstance(other, Clock):
            raise AttributeError("Правый оператор должен быть типом данных Clock")
        return self.sec >= other.sec


# c1 = Clock(100)
# c2 = Clock(200)  # Clock(100)
# # c4 = Clock(300)
# # c3 = c1 + c2 + c4
# # c1 += c2
# print(c1.get_format_time())
# print(c2.get_format_time())
# # print(c4.get_format_time())
# # print(c3.get_format_time())
# # if c1 == c2:
# #     print("Время одинаковое")
# # else:
# #     print("Время разное")
# #
# if c1 != c2:
#     print("Время разное")
# else:
#     print("Время одинаковое")

# Проверка работоспособности перегрузки вычитания (subtraction)

c1 = Clock(300)
c2 = Clock(200)
cs1 = c1 - c2
print(cs1.get_format_time())
# Проверка работоспособности перегрузки умножения (multiplication)
c1 = Clock(300)
c2 = Clock(3)
cm1 = c1 * c2
print(cm1.get_format_time())
# Проверка работоспособности перегрузки целочисленного деления (integer division)
c1 = Clock(300)
c2 = Clock(65)
cid1 = c1 // c2
print(cid1.get_format_time())
# Проверка работоспособности перегрузки получения остатка от деления (the remainder of the division)
c1 = Clock(300)
c2 = Clock(140)
crd1 = c1 % c2
print(crd1.get_format_time())

# Проверка работоспособности перегрузки операторов '<', '<='
c1 = Clock(300)
c2 = Clock(300)
print(c1.get_format_time())
print(c2.get_format_time())

if c1 < c2:
    print("Время 'c1' < 'c2' True")
else:
    print("Время не соответствует условию - False")

if c1 <= c2:
    print("Время 'c1' <= 'c2' True")
else:
    print("Время не соответствует условию - False")

# Проверка работоспособности перегрузки операторов '>', '>='
c1 = Clock(400)
c2 = Clock(400)
print(c1.get_format_time())
print(c2.get_format_time())

if c1 > c2:
    print("Время 'c1' > 'c2' True")
else:
    print("Время не соответствует условию - False")

if c1 >= c2:
    print("Время 'c1' >= 'c2' True")
else:
    print("Время не соответствует условию - False")
