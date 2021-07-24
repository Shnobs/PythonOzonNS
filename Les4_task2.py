anya = {'Секретные материалы': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
olya = {'Клан Сопрано': 'криминал', '24': 'драма', 'Во все тяжкие': 'криминал', 'Карточный домик': 'драма'}
nastya = {'Ведьмак': 'фэнтази', 'Игра престолов': 'фэнтази'}
sveta = {'Черное зеркало': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
# Преобразовываем словари во множества
anya_set = set(anya.keys())
olya_set = set(olya.keys())
nastya_set = set(nastya.keys())
sveta_set = set(sveta.keys())
# Находим повторяющиеся элементы
anya_olya = set.intersection(anya_set, olya_set)
anya_nastya = set.intersection(anya_set, nastya_set)
anya_sveta = set.intersection(anya_set, sveta_set)
# Выводим ответ с кем больше всего общих любимых сериалов
if len(anya_olya) > len(anya_nastya) and len(anya_olya) > len(anya_sveta):
    print(f'У Ани больше всего любимых сериалов с Олей их количество равно {len(anya_olya)}')
elif len(anya_nastya) > len(anya_olya) and len(anya_nastya) > len(anya_sveta):
    print(f'У Ани больше всего любимых сериалов с Настей их количество равно {len(anya_nastya)}')
else:
    print(f'У Ани больше всего любимых сериалов со Светой их количество равно {len(anya_sveta)}')
