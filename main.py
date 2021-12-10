class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(self, Student) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}  \nСредняя оценка за дз: {medium(self.grades)} \n'
        courses_in_progress = ", ".join(self.courses_in_progress)
        finished_courses = ",".join(self.finished_courses)
        re = f'Курсы в процессе изучения: {courses_in_progress} \nЗавершённые курсы: {finished_courses}'
        return res + re

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Студента нет')
            return
        return medium(self.grades) < medium(other.grades)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}  \nСредняя оценка за лекции: {medium(self.grades)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Лектора нет')
            return
        return medium(self.grades) < medium(other.grades)

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res

def medium(rate):
    sum = 0
    l = 0

    if len(rate) == 0:
        return 0

    for numbers in rate.values():
        l += len(numbers)

        for figure in numbers:
            sum += figure
    return round(sum/l, 2)

def medium_student(students, course):
    sum = 0
    l = 0

    for t in students:
        if course in t.courses_in_progress:
            for numbers in t.grades.values():
                l += len(numbers)

                for figure in numbers:
                    sum += figure

    return round(sum/l, 2)


def medium_lecturer(lecturers, course):
    sum = 0
    l = 0

    for t in lecturers:
        if course in t.courses_attached:
            for numbers in t.grades.values():
                l += len(numbers)

                for figure in numbers:
                    sum += figure

    return round(sum/l, 2)

# 1 студент
best_student = Student('Вова', 'Вовочкин', 'мужчина')
best_student.courses_in_progress += ['Python']
best_student.add_courses('Введение в программирование')

# 2 студент
low_student = Student('Лиза', 'Пупкина', 'женщина')
low_student.courses_in_progress += ['Python']
low_student.add_courses('Java')

# 1 эксперт
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

# 2 эксперт
low_reviewer = Reviewer('Some', 'So')
low_reviewer.courses_attached += ['Python']

# 1 лектор
best_lecturer = Lecturer('Buddy', 'Bud')
best_lecturer.courses_attached += ['Python']

# 2 лектор
low_lecturer = Lecturer('Bud', 'So')
low_lecturer.courses_attached += ['Python']

# студенты оценивают лекторов
best_student.rate_lecturer(best_lecturer, 'Python', 8)
best_student.rate_lecturer(low_lecturer, 'Python', 4)
low_student.rate_lecturer(best_lecturer, 'Python', 9)
low_student.rate_lecturer(low_lecturer, 'Python', 6)

# эксперты оценивают д/з
cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(low_student, 'Python', 4)
low_reviewer.rate_hw(best_student, 'Python', 10)
low_reviewer.rate_hw(low_student, 'Python', 6)

# Выводим данные
print(best_student)
print(low_student)

print(best_lecturer)
print(low_lecturer)

print(cool_reviewer)
print(low_reviewer)

# Выводим сравнение
print(best_student > low_student)
print(best_lecturer > low_lecturer)

# Выводим среднее значение 
print(f'Средняя оценка всех студентов на курсе Python: {medium_student([best_student, low_student], "Python")}')

print(f'Средняя оценка всех лекторов на курсе Python: {medium_lecturer([best_lecturer, low_lecturer], "Python")}')