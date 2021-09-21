# Технические переменные
devider = '\n'

# Создание необходиммых по условию задачи классов
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_avg_grade(self, grades):
        if len(grades.values()) == 0:
            return 'Нет оценок'
        else:
            total_grades = 0
            count = 0
            for grades in grades.values():
                for grade in grades:
                    total_grades += grade
                count += len(grades)
            if count != 0:
                return round(total_grades / count, 2)
            return 'Нет оценок'

    def __lt__(self, other):
        if isinstance(other, Student):
            avg_grade_self = self.get_avg_grade(self.grades)
            avg_grade_other = other.get_avg_grade(other.grades)
            return avg_grade_self < avg_grade_other
        else:
            print('Не принадлежит классу Student')

    def __str__(self):
        return f'Имя: {self.name}{devider}Фамилия: {self.surname}{devider}Средняя оценка за домашние задания: {self.get_avg_grade(self.grades)}{devider}Курсы в процессе изучения: {", ".join(self.courses_in_progress)}{devider}Завершенные курсы: {", ".join(self.finished_courses)}'
        
class Mentor():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_avg_grade(self, grades):
        if len(grades.values()) == 0:
            return 'Нет оценок'
        else:
            total_grades = 0
            count = 0
            for grades in grades.values():
                for grade in grades:
                    total_grades += grade
                count += len(grades)
            if count != 0:
                return round(total_grades / count, 2)
            return 'Нет оценок'

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            avg_grade_self = self.get_avg_grade(self.grades)
            avg_grade_other = other.get_avg_grade(other.grades)
            return avg_grade_self < avg_grade_other
        else:
            print('Не принадлежит классу Lecturer')

    def __str__(self):
        return f'Имя: {self.name}{devider}Фамилия: {self.surname}{devider}Средняя оценка за лекции: {self.get_avg_grade(self.grades)}'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return f'Имя: {self.name}{devider}Фамилия: {self.surname}'

# Создание экземпляров класса
mentor_1 = Mentor('Олег', 'Куликов')
mentor_2 = Mentor('Кирилл', 'Соколов')
lecturer_1 = Lecturer('Юрий', 'Воробьев')
lecturer_2 = Lecturer('Виталий', 'Орлов')
reviever_1 = Reviewer('Денис', 'Синицин')
reviever_2 = Reviewer('Геннадий', 'Воронин')
student_1 = Student('Егор', 'Журавлев', 'М')
student_2 = Student('Анна', 'Сорокина', 'Ж')

# Информация о менторе
print('Информация о менторах: ')
print('Ментор №1: ', mentor_1.name, mentor_1.surname)
print('Ментор №2: ', mentor_2.name, mentor_2.surname)
mentor_1.courses_attached = ['Python', 'Git', 'JavaScript']
mentor_2.courses_attached = ['React', 'Gatsby']
print('---')
print('Курсы ментора №1:', mentor_1.courses_attached)
print('Курсы ментора №2:', mentor_2.courses_attached)
print('')

# Информация о студенте
student_1.finished_courses = ['Python']
student_1.courses_in_progress = ['Git', 'JavaScript']

student_2.finished_courses = ['React', 'Gatsby']
student_2.courses_in_progress = ['JavaScript', 'Gatsby', 'React']
    
## Вызов методов экземпляра студент
student_1.rate_lecturer(lecturer_1, 'Git', 8)
student_1.rate_lecturer(lecturer_1, 'JavaScript', 6)
student_2.rate_lecturer(lecturer_1, 'JavaScript', 7)
student_2.rate_lecturer(lecturer_2, 'Gatsby', 9)
student_2.rate_lecturer(lecturer_2, 'React', 10)
### Присвоение необходимых параметров для экземпляра проверяющий
reviever_1.courses_attached = ['Git', 'JavaScript']
reviever_1.rate_hw(student_1, 'Git', 7)
reviever_1.rate_hw(student_1, 'JavaScript', 10)
reviever_2.courses_attached = ['JavaScript', 'Gatsby', 'React']
reviever_2.rate_hw(student_2, 'JavaScript', 5)
reviever_2.rate_hw(student_2, 'React', 9)
reviever_2.rate_hw(student_2, 'Gatsby', 10)
print('Информация о студентах: ')
print(student_1)
print('---')
print(student_2)
print('')
print('Средняя оценка студента №1 меньше средней оценки студента №2:', student_1 < student_2)
print('')

# Лекторы
print('Информация о лекторах: ')
print(lecturer_1)
print('---')
print(lecturer_2)
print('')
print('Средняя оценка лектора №1 меньше средней оценки лектора №2:', lecturer_1 < lecturer_2)
print('')

# Проверяющие
print('Информация о проверяющих: ')
print(reviever_1)
print('---')
print(reviever_2)
print('')

# Вызов функций
students = [student_1, student_2]
lecturers = [lecturer_1, lecturer_2]
course = 'JavaScript'

## Оценка студентов
def get_avg_grade_students(students, course):
    total_grade = 0
    count = 0
    for student in students:
        if course in student.grades.keys():
            total_grade += sum(student.grades[course])
            count += len(student.grades[course])
    if count != 0 and total_grade != 0:
        return total_grade / count
    return 'Нет оценок по указанному курсу или курса нет в списке'

## Оценка лекторов
def get_avg_grade_lecturers(lecturers, course):
    total_grade = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades.keys():
            total_grade += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    if count != 0 and total_grade != 0:
        return total_grade / count
    return 'Нет оценок по указанному курсу или курса нет в списке'
print('Вызов функций')
print(f'Средняя оценка по курсу {course} среди всех студентов = {get_avg_grade_students(students, course)}')
print(f'Средняя оценка по лекциям курса {course} среди всех лекторов = {get_avg_grade_lecturers(lecturers, course)}')