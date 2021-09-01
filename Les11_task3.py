import random


class Person:  # Объявляем новый класс Person
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name

    def __str__(self):  # Метод отвечают за строковое представления объекта
        return f'{self.f_name.title()} {self.l_name.title()}'


class Student(Person):  # Наследуем родительский класс Person
    def __init__(self, f_name, l_name, n_group):
        super().__init__(f_name, l_name)  # Обращаемся к конструктору __init__ базового класса
        self.n_group = n_group
        self.score_list = []

    def set_score_test(self, *score):  # Метод добавления любого количества оценок
        for elem in score:  # Проходим циклом по элементам кортежа и добавляем их в список
            self.score_list.append(elem)

    def __str__(self):  # Метод отвечают за строковое представления объекта
        return f'Студент: {self.f_name.title()} {self.l_name.title()}, группа {self.n_group.upper()}, ' \
               f'оценки {self.score_list}'


class Professor(Person):  # Наследуем родительский класс Person
    def __init__(self, f_name, l_name, course):
        super().__init__(f_name, l_name)
        self.course = course

    def test_students(self, spisok_students):
        for elem in spisok_students:
            elem.set_score_test(random.randint(1, 10))  # Обращаемся к методу класса Student, передаем случайную оценку

    def __str__(self):  # Метод отвечают за строковое представления объекта
        return f'Преподователь: {self.f_name.title()} {self.l_name.title()} читает курс {self.course.upper()}'


prepod = Professor('андрей', 'семенов', 'ооп')
ivan = Student('иван', 'крылов', 'ти-2')
bolvan = Student('болван', 'болванов', 'ит-7')
spisok = [ivan, bolvan]
print(prepod.__str__())
prepod.test_students(spisok)
print(ivan.__str__())
print(bolvan.__str__())
prepod.test_students(spisok)
print(ivan.__str__())
print(bolvan.__str__())
