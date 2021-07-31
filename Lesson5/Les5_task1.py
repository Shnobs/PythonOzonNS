anya = {'Секретные материалы': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
olya = {'Клан Сопрано': 'криминал', '24': 'драма', 'Во все тяжкие': 'криминал', 'Карточный домик': 'драма'}
nastya = {'Ведьмак': 'фэнтази', 'Игра престолов': 'фэнтази'}
sveta = {'Черное зеркало': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}


def common_interests(spisok1, spisok2):  # Создание функции для проверки совпадений по жанрам
    sovpadenie1 = set()
    sovpadenie2 = set()
    for key, value in spisok1.items():  # Заполнение первого множества
        sovpadenie1.add(value)
    for key, value in spisok2.items():  # Заполнение второго множества
        sovpadenie2.add(value)
    if len(sovpadenie1.intersection(sovpadenie2)) > 0:  # Проверка, что общее множество не пустое
        return sovpadenie1.intersection(sovpadenie2)  # Возвращение множества содержащего общие элементы обоих множеств
    else:
        return 'отсутсвуют'  # Возвращение строки вместо пустого множества


print(f'У Ани и Насти общие вкусы по жанрам {common_interests(anya, nastya)}')
print(f'У Оли и Светы общие вкусы по жанрам {common_interests(olya, sveta)}')
print(f'У Светы и Ани общие вкусы по жанрам {common_interests(sveta, anya)}')
