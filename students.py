from collections.abc import Iterable, Iterator

class Student:
    def __init__(self, name, grade1, grade2, grade3):
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3

    def average(self):
        return (self.grade1 + self.grade2 + self.grade3) / 3
    
    def __str__(self):
        return f"{self.name} - avg: {self.average():.2f}"
    
class SchoolClassIterator(Iterator):
    def __init__(self, students):
        self._students = sorted(students, key=lambda s: s.grade1, reverse=True)
        self._index = 0

    def __next__(self):
        if self._index >= len(self._students):
            raise StopIteration
        student = self._students[self._index]
        self._index += 1
        return student


class SchoolClass(Iterable):
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def __iter__(self):
        return SchoolClassIterator(self.students)
    
    def rank_matter_1(self):
        return sorted(self.students, key=lambda s: s.grade1, reverse=True)
    
    def rank_matter_2(self):
        return sorted(self.students, key=lambda s: s.grade2, reverse=True)

    def rank_matter_3(self):
        return sorted(self.students, key=lambda s: s.grade3, reverse=True)


if __name__ == "__main__":
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))

    print("Classement matière 1 :")
    for student in school_class.rank_matter_1():
        print(student)
    
    print("\nClassement matière 2 :")
    for student in school_class.rank_matter_2():
        print(student)

    print("\nClassement matière 3 :")
    for student in school_class.rank_matter_3():
        print(student)

    print("Parcours via l'itérateur (matière 1 décroissante) :")
    for student in school_class:
        print(student)