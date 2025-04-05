# DZ_22. Задание: Создать класс для преобразования килограмм в фунты.
# 12 кг => 26.46 фунтов
# 41 кг => 90.405 фунтов
# Килограммы задаются только числами

# Информация для конвертирования единиц массы:
# В 1 фунте 0.4535923745 килограмм
# 1 kg = 2.2046226 фунта lb (lb - английский фунт), если округлить до 3-х знаков (round(2.2046226, 3)) =>
# => ratio_lb = 2.205 коэффициент, как множитель

class Converter:  # объявляем класс для преобразования единиц массы (из кг в фунты)

    def __init__(self, mkg=12):  # mkg - переменная массы в килограммах
        self.__mkg = mkg

    def __check_value(c):
        if isinstance(c, int) or isinstance(c, float):
            return True
        return False

    @property
    def mkg(self):  # "геттер"(get), возвращающий результат (get - получить) - массу в фунтах.
        ratio_lb = 2.205  # коэффициент(множитель) пересчёта в фунты
        res = f"{self.__mkg} кг => {round(self.__mkg * ratio_lb, 3)} фунтов"
        return res

    @mkg.setter
    def mkg(self, mkg):  # "сеттер"(set), устанавливающий вводимое значение с проверкой типа данных
        if Converter.__check_value(mkg):
            self.__mkg = mkg
        else:
            print("Килограммы задаются только числами")


c1 = Converter()
# print(c1.__dict__)
print(c1.mkg)
c1.mkg = 41
print(c1.mkg)
c1.mkg = "41"
# print(c1.__dict__)

