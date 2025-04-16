# DZ_25. Задание:
# Создать иерархию классов: Human (Человек), Student (Студент),
# Teacher (Преподаватель) и Graduate (Дипломник).
# Создать список группы представителей данной иерархии, вывести информацию
# о каждом участнике.

# Батодалаев Даши 16 ГК Web_011 5
# Загидуллин Линар 32 РПО PD_011 5
# Шугани Сергей 15 ЗПО PD_011 5 Защита персональных данных
# Даньшин Андрей 38 Астрофизика 110
# Маркин Даниил 17 ГК Python_011 5
# Башкиров Алексей 45 Разработка приложений 20


from abc import ABC, abstractmethod


class Human(ABC):  # Родительский класс "Человек" (от класса абстрактных методов)
    def __init__(self, fio, age):  # Инициализируем переменные:
        self.fio = fio  # ФИО
        self.age = age  # возраст

    @abstractmethod
    def print_info(self):
        print(f"{self.fio} {self.age}", end=" ")  # Реализация Абстрактного метода в родительском классе
        # pass


class Student(Human):  # класс-наследник "Студент"
    def __init__(self, fio, age, dir_study, group, rating):
        super().__init__(fio, age)
        self.dir_study = dir_study  # направление обучения (direction_of_study)
        self.group = group  # группа
        self.rating = rating  # рейтинг или средний балл

    # @abstractmethod
    def print_info(self):
        super().print_info()
        print(f"{self.dir_study} {self.group} {self.rating}", end=" ")


class Teacher(Human):  # класс-наследник "Преподаватель"
    def __init__(self, fio, age, discipline, skill):
        super().__init__(fio, age)
        self.discipline = discipline  # дисциплина, предмет или преподаваемая наука
        self.skill = skill  # навык (умение, мастерство) в своей дисциплине

    def print_info(self):
        super().print_info()
        print(f"{self.discipline} {self.skill}", end=" ")


class Graduate(Student):  # класс-наследник "Дипломник"
    def __init__(self, fio, age, group, dir_study, rating, thesis_topic):
        super().__init__(fio, age, group, dir_study, rating)
        self.thesis_topic = thesis_topic  # тема дипломной работы (thesis topic)

    def print_info(self):
        super().print_info()
        print(f"{self.thesis_topic}", end=" ")


s1 = Student("Батодалаев Даши", 16, "ГК", "Web_011", 5)
s2 = Student("Загидуллин Линар", 32, "РПО", "PD_011", 5)
g = Graduate("Шугани Сергей", 15, "РПО", "RD_011", 5, 'Защита персональных данных')
t1 = Teacher("Даньшин Андрей", 38, "Астрофизика", 110)
s3 = Student("Маркин Даниил", 17, "ГК", "Python_011", 5)
t2 = Teacher("Башкиров Алексей", 45, "Разработка приложений", 20)

person = list()
person.append(s1)
person.append(s2)
person.append(g)
person.append(t1)
person.append(s3)
person.append(t2)

for p in person:
    p.print_info()
    print()
