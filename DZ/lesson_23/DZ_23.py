# DZ_23. Задание: Для класса Account (с урока) написать два варианта get и set методов.
# Первый вариант через декоратор @property
# Второй через get_...(), set_...()

class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = "RUB"
    suffix_usd = "USD"
    suffix_eur = "EUR"

    def __init__(self, num, surname, percent, value):
        self.__num = num
        self.__surname = surname
        self.__persent = percent
        self.__value = value
        print(f"Счет #{self.__num} принадлежащий {self.__surname} был открыт.")
        print("*" * 50)

    # def __del__(self):
    #     print("*" * 50)
    #     print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт.")

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    def convert_to_usd(self):
        usd_val = Account.convert(self.__value, Account.rate_usd)
        print(f"Состояние счета: {usd_val} {Account.suffix_usd}")

    def convert_to_eur(self):
        eur_val = Account.convert(self.__value, Account.rate_eur)
        print(f"Состояние счета: {eur_val} {Account.suffix_eur}")

    # -------------------------------------------------------------------------------------
    # Первый вариант get и set методов (через декоратор @property):
    @property  # Декоратор метода get (edit_num)
    def edit_num(self):  # "геттер"(get), возвращающий результат - новый номер счёта
        return self.__num

    @edit_num.setter  # Декоратор метода set (edit_num)
    def edit_num(self, num):  # "сеттер"(set), устанавливающий новый номер счёта
        self.__num = num

    @property  # Декоратор метода get (edit_owner)
    def edit_owner(self):  # "геттер"(get), возвращающий результат - фамилию владельца
        return self.__surname

    @edit_owner.setter  # Декоратор метода set (edit_owner)
    def edit_owner(self, surname):  # "сеттер"(set), устанавливающий новую фамилию
        self.__surname = surname

    @property  # Декоратор метода get (edit_owner)
    def adit_percents(self):  # "геттер"(get), возвращающий результат - изменённый процент
        return f"Проценты: {self.__persent:.0%}"

    @adit_percents.setter  # Декоратор метода set (adit_percents, %)
    def adit_percents(self, persent):  # "сеттер"(set), устанавливающий новый процент начисления
        self.__persent = persent

    @property  # Декоратор метода get (edit_value)
    def edit_value(self):  # "геттер"(get), возвращающий результат - состояние счёта
        return f"Новый баланс: {self.__value} {Account.suffix}"

    @edit_value.setter  # Декоратор метода set (edit_value)
    def edit_value(self, value):  # "сеттер"(set), устанавливающий новое значение состояния счёта
        self.__value = value

    # -------------------------------------------------------------------------------------
    # Второй вариант get и set методов (через get_...(), set_...()):

    def get_edit_num(self):  # "геттер"(get), возвращающий результат - новый номер счёта
        return self.__num

    def set_edit_num(self, num):  # "сеттер"(set), устанавливающий новый номер счёта
        self.__num = num

    def get_edit_owner(self):  # "геттер"(get), возвращающий - фамилию владельца
        return self.__surname

    def set_edit_owner(self, surname):  # "сеттер"(set), устанавливающий новую фамилию владельца
        self.__surname = surname

    def get_edit_percents(self):  # "геттер"(get), возвращающий - изменённый процент начисления
        return f"Проценты: {self.__persent:.0%}"

    def set_edit_percents(self, persent):  # "сеттер"(set), устанавливающий новый процент начисления
        self.__persent = persent

    def get_edit_value(self):  # "геттер"(get), возвращающий новый баланс (состояние) счёта
        return f"Новый баланс: {self.__value} {Account.suffix}"

    def set_edit_value(self, value):  # "сеттер"(set), устанавливающий новое значение состояния счёта
        self.__value = value

    # Завершение области get и set методов.
    # -------------------------------------------------------------------------------------

    def add_percents(self):
        self.__value += self.__value * self.__persent
        print("Проценты были успешно начислены!")
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.__value:
            print(f"К сожалению у вас нет {val} {Account.suffix}")
        else:
            self.__value -= val
            print(f"{val} {Account.suffix} было успешно снято!")
        self.print_balance()

    def add_money(self, val):
        self.__value += val
        print(f"{val} {Account.suffix} было успешно добавлено!")
        self.print_balance()

    def print_balance(self):
        print(f"Текущий баланс {self.__value} {Account.suffix}")

    def print_info(self):
        print("Информация о счете:")
        print("-" * 20)
        print(f"#{self.__num}")
        print(f"Владелец: {self.__surname}")
        self.print_balance()
        print(f"Проценты: {self.__persent:.0%}")
        print("-" * 20)


acc = Account("12345", "Долгих", 0.03, 1000)
# acc.print_balance()
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
print()

Account.set_usd_rate(2)
Account.set_eur_rate(3)
acc.convert_to_usd()
acc.convert_to_eur()
print()

# Реализация первого способа "геттеров" и "сеттеров" через декоратор @property
acc.edit_owner = "Дюма"
print("Изменился владелец счёта:\n", acc.edit_owner)
acc.print_info()
print()

acc.adit_percents = 0.05
print("Изменился процент начисления:\n", acc.adit_percents)
acc.print_info()
print()

acc.edit_num = "67890"
print("Изменился номер счёта:\n", acc.edit_num)
acc.print_info()
print()

acc.edit_value = 1500
print("Изменился баланс счёта:\n", acc.edit_value)
acc.print_info()
print()

# Реализация второго способа "геттеров" и "сеттеров" через get_...(), set_...()
acc.set_edit_num("37291")
acc.set_edit_owner("Сурожский")
acc.set_edit_percents(0.04)
acc.set_edit_value(2500)
print()
print("Выводим данные с учётом изменённых свойств с использованием второго варианта:")
acc.print_info()
print("Вывод изменённых свойств с использованием второго варианта:")
print(acc.get_edit_num())
print(acc.get_edit_owner())
print(acc.get_edit_percents())
print(acc.get_edit_value())
print()

acc.add_percents()
print()

acc.withdraw_money(100)
print()

acc.withdraw_money(3000)
print()

acc.add_money(5000)
print()

acc.withdraw_money(3000)
print()
