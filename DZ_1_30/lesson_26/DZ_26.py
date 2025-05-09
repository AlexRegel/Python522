class Student:  # Наружный класс
    def __init__(self, name=None):  # -> str
        self.name = name
        self.nb = self.Notebook  # "HP", "i7", 16

    def print_info(self):
        print(f"{self.name} =>", end=" ")

    class Notebook:  # Внутренний класс
        def __init__(self, note_name, cpu, ram):
            self.note_name = note_name
            self.cpu = cpu
            self.ram = ram

        def print_info(self):
            print(f"{self.note_name}, {self.cpu}, {self.ram}")


s = Student("Roman")  # "Roman"
s.print_info()
n = s.nb("HP", "i7", 16)  # Можно также присвоить при инициализации (default)
# n.note_name = "ASUS"  # Альтернативный вариант присвоения параметров ноутбука
# n.cpu = "i9"
# n.ram = 16
n.print_info()

s = Student("Vladimir")
s.print_info()  # Запустить последовательно 's.print_info()' и 'n.print_info()'
n.print_info()
# print()
