shows = {'Секретные материалы': 'фантастика', 'Ведьмак': 'фэнтази', 'Клан Сопрано': 'криминал', '24': 'драма',
         'Черное зеркало': 'фантастика', 'Во все тяжкие': 'криминал', 'Игра престолов': 'фэнтази',
'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
ratings = {'Секретные материалы': 0.9, 'Ведьмак': 0.95, 'Клан Сопрано': 0.8, '24': 0.75, 'Черное зеркало': 0.98,
           'Во все тяжкие': 0.85, 'Игра престолов': 0.87, 'Карточный домик': 0.82, 'Рик и Морти': 1}
spisok = []
average_rating = 0
i = 0
for key, value in shows.items():
    if value == 'фантастика':
        spisok.append(key)
for key, value in ratings.items():
    if key in spisok:
        average_rating += value
        i += 1
average_rating = average_rating / i
print(f'Средний рейтинг сериалов в жанре фантастика составляет {average_rating}')
