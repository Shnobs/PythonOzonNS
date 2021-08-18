shows = {'Секретные материалы': 'фантастика', 'Ведьмак': 'фэнтази', 'Клан Сопрано': 'криминал', '24': 'драма',
         'Черное зеркало': 'фантастика', 'Во все тяжкие': 'криминал', 'Игра престолов': 'фэнтази',
         'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}

shows_dict_comprehension = {key: value for key, value in shows.items() if value == 'фантастика' or value == 'фэнтази'}
# Создаем словарь по условию, что значение равно фантастика или фэнтази
print(f'"Это словарь {type(shows_dict_comprehension)} - {shows_dict_comprehension}')
shows_list_comprehension = [key for key in shows_dict_comprehension.keys()]
# Создаем список с ключами из словаря shows_dict_comprehension
print(f'"Это список {type(shows_list_comprehension)}  - {shows_list_comprehension}')
