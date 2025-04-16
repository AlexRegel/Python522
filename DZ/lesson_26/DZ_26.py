class Student:
    def __init__(self, name):
        self.name = name
        self.nb = self.Notebook  # "HP", "i7", 16

    def print_info(self):
        print(f"{self.name} =>", end=" ")

    class Notebook:
        def __init__(self, note_name, cpu, ram):
            self.note_name = note_name
            self.cpu = cpu
            self.ram = ram

        def print_info(self):
            print(f"{self.note_name}, {self.cpu}, {self.ram}")


s = Student("Roman")
s.print_info()
d = s.nb("HP", "i7", 16)
d.note_name = "Intel"
d.cpu = "i7"
d.ram = 16
d.print_info()
