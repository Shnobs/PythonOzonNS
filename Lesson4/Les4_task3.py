shows = {'Секретные материалы': 'фантастика', 'Ведьмак': 'фэнтази', 'Клан Сопрано': 'криминал', '24': 'драма',
         'Черное зеркало': 'фантастика', 'Во все тяжкие': 'криминал', 'Игра престолов': 'фэнтази',
'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
ratings = {'Секретные материалы': 0.9, 'Ведьмак': 0.95, 'Клан Сопрано': 0.8, '24': 0.75, 'Черное зеркало': 0.98,
           'Во все тяжкие': 0.85, 'Игра престолов': 0.87, 'Карточный домик': 0.82, 'Рик и Морти': 1}
spisok_genre = list(shows.values())
spisok_rating = list(ratings.values())
average_rating = 0
kolichestvo = 0
# for elem in spisok_genre:
#     if elem == 'фантастика':
#         average_rating += int(spisok_rating(spisok_genre.index(elem)))
print(spisok_genre)
print(spisok_rating)
print(spisok_genre.index('фантастика'))