class Clock:
    __DAY = 86400

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        self.sec = sec % self.__DAY

    def det_format_time(self):
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


c1 = Clock(100)
c2 = Clock(200)  # Clock(100)
# c4 = Clock(300)
# c3 = c1 + c2 + c4
# c1 += c2
print(c1.det_format_time())
print(c2.det_format_time())
# print(c4.det_format_time())
# print(c3.det_format_time())
# if c1 == c2:
#     print("Время одинаковое")
# else:
#     print("Время разное")

if c1 != c2:
    print("Время разное")
else:
    print("Время одинаковое")
