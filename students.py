from collections.abc import Iterable, Iterator

def add_matter_4(cls):
    original_init = cls.__init__

    def new_init(self, name, grade1, grade2, grade3, grade4):
        original_init(self, name, grade1, grade2, grade3)
        self.grade4 = grade4

    def new_average(self):
        return (self.grade1 + self.grade2 + self.grade3 + self.grade4) / 4

    cls.__init__ = new_init
    cls.average = new_average
    return cls

def add_iter_matter_4(cls):
    def iter_matter_4(self):
        return SchoolClassIteratorMatter4(self.students)

    cls.iter_matter_4 = iter_matter_4
    return cls


@add_matter_4
class Student:
    def __init__(self, name, grade1, grade2, grade3):
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3

    def average(self):
        return (self.grade1 + self.grade2 + self.grade3) / 3
    
    def __str__(self):
        return (
            f"{self.name} - "
            f"m1:{self.grade1} "
            f"m2:{self.grade2} "
            f"m3:{self.grade3} "
            f"m4:{self.grade4} "
            f"avg:{self.average():.2f}"
        )
    
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
    
class SchoolClassIteratorMatter2(Iterator):
    def __init__(self, students):
        self._students = sorted(students, key=lambda s: s.grade2, reverse=True)
        self._index = 0

    def __next__(self):
        if self._index >= len(self._students):
            raise StopIteration
        student = self._students[self._index]
        self._index += 1
        return student


class SchoolClassIteratorMatter3(Iterator):
    def __init__(self, students):
        self._students = sorted(students, key=lambda s: s.grade3, reverse=True)
        self._index = 0

    def __next__(self):
        if self._index >= len(self._students):
            raise StopIteration
        student = self._students[self._index]
        self._index += 1
        return student

class SchoolClassIteratorMatter4(Iterator):
    def __init__(self, students):
        self._students = sorted(students, key=lambda s: s.grade4, reverse=True)
        self._index = 0

    def __next__(self):
        if self._index >= len(self._students):
            raise StopIteration
        student = self._students[self._index]
        self._index += 1
        return student

@add_iter_matter_4
class SchoolClass(Iterable):

    _instance = None

    def __init__(self):
        if not hasattr(self, "students"):
            self.students = []

    def add_student(self, student):
        self.students.append(student)

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __iter__(self):
        return SchoolClassIterator(self.students)
    
    def iter_matter_2(self):
        return SchoolClassIteratorMatter2(self.students)

    def iter_matter_3(self):
        return SchoolClassIteratorMatter3(self.students)
    
    def rank_matter_1(self):
        return sorted(self.students, key=lambda s: s.grade1, reverse=True)
    
    def rank_matter_2(self):
        return sorted(self.students, key=lambda s: s.grade2, reverse=True)

    def rank_matter_3(self):
        return sorted(self.students, key=lambda s: s.grade3, reverse=True)


if __name__ == "__main__":
    school_class = SchoolClass()
    same_school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13, 15))
    school_class.add_student(Student('A', 8, 2, 17, 11))
    school_class.add_student(Student('V', 9, 14, 14, 16))

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
    
    print("\nParcours via l'itérateur (matière 2 décroissante) :")
    for student in school_class.iter_matter_2():
        print(student)
    
    print("\nParcours via l'itérateur (matière 3 décroissante) :")
    for student in school_class.iter_matter_3():
        print(student)

    print("\nVérification matière 4 :")
    for student in school_class.students:
        print(f"{student.name} -> m4:{student.grade4}")

    print("\nParcours via l'itérateur (matière 4 décroissante) :")
    for student in school_class.iter_matter_4():
        print(student)

    print("\nSingleton :")
    print(school_class is same_school_class)
