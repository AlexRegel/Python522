# DZ_21. Задание: Реализуйте класс "Автомобиль". Необходимо хранить в полях класса:
# название модели, год выпуска, производитель, мощность двигателя, цвет машины, цену.
# Требуется реализовать методы класса для ввода данных, вывода данных, реализуйте
# доступ к отдельным полям через методы класса.

# Перечень выражений для удобства создания класса и его методов и свойств:
# car, model, year_release, manufacturer, engine_power, car_color, price
# Реализация класса:
class Car:

    def __init__(self, model, year_release, manufacturer, engine_power,
                 car_color, price):
        self.model = model
        self.year_release = year_release
        self.manufacturer = manufacturer
        self.engine_power = engine_power
        self.car_color = car_color
        self.price = price

    def print_info(self):
        print(" Данные автомобиля ".center(40, "*"))
        print(f"Модель: {self.model}\nГод выпуска: {self.year_release}\nПроизводитель: {self.manufacturer}\n"
              f"Мощность двигателя: {self.engine_power}\nЦвет машины: {self.car_color}\nЦена: {self.price}")
        print("=" * 40)

    def set_model(self, model):  # установили модель
        self.model = model

    def get_model(self):  # получили модель
        return self.model

    def set_year_release(self, year_release):  # установили год выпуска
        self.year_release = year_release

    def get_year_release(self):  # получили год выпуска
        return self.year_release

    def set_manufacturer(self, manufacturer):  # установили производителя
        self.manufacturer = manufacturer

    def get_manufacturer(self):  # получили производителя
        return self.manufacturer

    def set_engine_power(self, engine_power):  # установили мощность двигателя
        self.engine_power = engine_power

    def get_engine_power(self):  # получили мощность двигателя
        return self.engine_power

    def set_car_color(self, car_color):  # установили цвет машины
        self.car_color = car_color

    def get_car_color(self):  # получили цвет машины
        return self.car_color

    def set_price(self, price):  # установили цену
        self.price = price

    def get_price(self):  # получили цену
        return self.price


c1 = Car("X7 M50i", "2021", "BMW", "530 л.с.",
         "white", "10790000")

# Выводим исходные свойства экземпляра класса c1:
c1.print_info()
print(c1.get_model())  # Запрос марки авто., как отдельного свойства из базового списка свойств

# Переопределяем некоторые свойства экземпляра класса c1:
c1.set_model("X7 xDrive40i")
c1.set_engine_power("340 л.с.")
c1.set_price("8540000")
print()
print("Выводим данные с учётом некоторых изменённых свойств:")
c1.print_info()
print("Итак, были изменены 3 свойства, относительно базового набора:")
print(c1.get_model())
print(c1.get_engine_power())
print(c1.get_price())
print()
# Выводим те-же данные другим способом, т.е. через сам класс "car",
# используя его методы, с указанием экземпляра класса (c1):
Car.print_info(c1)
print(Car.get_model(c1))
print(Car.get_engine_power(c1))
print(Car.get_price(c1))
