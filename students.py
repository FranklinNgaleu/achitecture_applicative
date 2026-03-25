class Student:
    def __init__(self, name, grade1, grade2, grade3):
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3

    def average(self):
        return (self.grade1 + self.grade2 + self.grade3) / 3


class SchoolClass:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

school_class = SchoolClass()
school_class.add_student(Student('J', 10, 12, 13))
school_class.add_student(Student('A', 8, 2, 17))
school_class.add_student(Student('V', 9, 14, 14))