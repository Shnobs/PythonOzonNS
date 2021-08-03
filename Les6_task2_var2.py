import pickle
shows = {'Секретные материалы': {'Жанр': 'фантастика', 'Рейтинг': 0.9}, 'Ведьмак': {'Жанр': 'фэнтази', 'Рейтинг': 0.95},
        'Клан Сопрано': {'Жанр': 'криминал', 'Рейтинг': '0.8'}, '24': {'Genre': 'драма', 'Rating': 0.75},
        'Черное зеркало': {'Жанр': 'фантастика', 'Рейтинг': 0.98}, 'Во все тяжкие': {'Жанр': 'криминал',
        'Рейтинг': '0.85'}, 'Игра престолов': {'Жанр': 'фэнтази', 'Рейтинг': 0.87}, 'Карточный домик': {'Genre': 'драма',
        'Rating': 0.82}, 'Рик и Морти': {'Жанр': 'фантастика', 'Рейтинг': 1}}
def func_janr(janr):
    spisok_shows = shows.copy()  # Создаем резервную копию словаря для работы внутри функции
    new_dict = {}
    new_list = []
    for key in spisok_shows.keys():  # Перебираем словарь по ключам
        if list(spisok_shows[key].values())[0] == janr:  # Сооружаем эту конструкцию для обхода ошибок KeyError
            new_list.append(list(spisok_shows[key].values())[1])  # Добавлем в список рейтинг сериала взяв только значение
            new_dict[key] = list(spisok_shows[key].values())[1]  # Заполняем словарь с ключом и рейтингом как значение
    with open(f'{janr.upper()}.dat', 'wb') as file:  # Создаем бинарный файл с переменным значением названия
         pickle.dump(new_dict, file)  # Записываем в файл словарь
    new_list = list(map(float, new_list))  # Через функию map преобразуем возможные строчные значения во float
    return f'В жанре {janr} количество сериалов {len(new_list)} средний рейтинг {round(sum(new_list)/len(new_list), 3)}'
""" return возращает f-строку с заданными значениями средний рейтинг округляется до трех знаков после запятой 
и рассчитывается по элементам списка"""

list_janr = []  # Создаем set через List
for key, value in shows.items():  # Перебервем элементы словаря
    list_janr.append(list(shows[key].values())[0])  # Заполняем список всеми жанрами включая повторы
set_janr = set(list_janr)  # Избавляемся от повторов переводом во множество
for elem in set_janr:  # Прогоняем циклом все элементы множества и выводим ответ передачей элемента в функцию
    print(func_janr(elem))