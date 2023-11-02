class Subject:
    def __init__(self, name, teacher):
        self.name = name  # Название предмета
        self.teacher = teacher  # Учитель предмета

    def get_info(self):
        return f"Предмет: {self.name}, Преподаватель: {self.teacher}"


class Student:
    def __init__(self, name, age):
        self.name = name  # Имя ученика
        self.age = age  # Возраст ученика
        self.diary = Diary()  # У каждого ученика есть свой дневник

    def add_subject(self, subject):
        self.diary.add_subject(subject)

    def view_diary(self):
        return self.diary.get_subjects()


class Diary:
    def __init__(self):
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def get_subjects(self):
        subject_info = ""
        for subject in self.subjects:
            subject_info += subject.get_info() + "\n"
        return subject_info


# Создание объектов предметов
math = Subject("Математика", "Бурова")
english = Subject("Английский", "Ринатова")
physics= Subject("Физика","Хайдаров")

# Создание объектов учеников
student1 = Student("Альбина", 18)
student2 = Student("Алсу", 17)

# Добавление предметов в дневник учеников
student1.add_subject(math)
student1.add_subject(english)

student2.add_subject(english)
student2.add_subject(physics)

# Вывод информации о дневнике учеников
print("Дневник ученика 1:")
print(student1.view_diary())

print("Дневник ученика 2:")
print(student2.view_diary())
