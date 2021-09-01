class Person:  # Объявляем новый класс Person
    def __init__(self, f_name, l_name):  # Собираем данные об имени и фамилии
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


if __name__ == "__main__":  # Указание запустить код, если он выполняется как автономный файл.
    ivan = Student('иван', 'крылов', 'ти-2')
    bolvan = Student('болван', 'болванов', 'ит-7')
    ivan.set_score_test(3, 4)
    ivan.set_score_test(3, 2)
    ivan.set_score_test(5)
    bolvan.set_score_test(2, 2, 1, 2, 3)
    print(ivan.__str__())
    print(bolvan.__str__())
