shows = {'Секретные материалы': 'фантастика', 'Ведьмак': 'фэнтази', 'Клан Сопрано': 'криминал', '24': 'драма',
         'Черное зеркало': 'фантастика', 'Во все тяжкие': 'криминал', 'Игра престолов': 'фэнтази',
         'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
ratings = {'Секретные материалы': 0.9, 'Ведьмак': 0.95, 'Клан Сопрано': 0.8, '24': 0.75, 'Черное зеркало': 0.98,
           'Во все тяжкие': 0.85, 'Игра престолов': 0.87, 'Карточный домик': 0.82, 'Рик и Морти': 1}
spisok = []
spisok_dlya_vasya = []
for key, value in shows.items():
    if value != 'фэнтази':
        spisok.append(key)
for key, value in ratings.items():  # Заполнение списка подходящими под условия сериалами
    if key in spisok and value >= 0.85:
        spisok_dlya_vasya.append(key)
i = 0
while True:
    if i >= len(spisok_dlya_vasya):  # Защита от ошибки обращения к несуществующему элементу списка
        break
    else:
        print(f'Рекомендуем для просмотра сериал {spisok_dlya_vasya[i]} ')
        otvet = input('Введите ДА для просмотра или НЕТ для следующего сериала: ')
        i += 1
        if otvet.upper() == 'ДА':
            break
        elif otvet.upper() == 'НЕТ':
            continue
        else:
            print('Введите нормальный ответ!')  # Защита от ошибочного ввода