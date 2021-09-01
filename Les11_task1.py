class Person:  # Объявляем новый класс Person
    def __init__(self, f_name, l_name):  # Собираем данные об имени и фамилии
        self.f_name = f_name
        self.l_name = l_name

    def __str__(self):  # Метод отвечают за строковое представления объекта
        return f'{self.f_name.title()} {self.l_name.title()}'


if __name__ == "__main__":  # Указание запустить код, если он выполняется как автономный файл.
    alex = Person('alex', 'martynov')
    shnobs = Person('shnobby', 'shnobbs')
    print(alex.__str__())
    print(shnobs.__str__())
