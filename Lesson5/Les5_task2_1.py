def shows_janr(shows, janr):  # Создаем список ключей по заданному значению
    show = []
    for key, value in shows.items():
        if value == janr:
            show.append(key)  # Заполняем список
    return show  # Возвращем список сериалов


def ratings_janr(raitings, spisok):  # Рассчитываем рейтинг по заданным ключам
    average_rating = []  # Используем список, чтобы не вводить лишние переменные
    for key, value in raitings.items():
        if key in spisok:
            average_rating.append(value)
    return round(sum(average_rating) / len(average_rating), 3)  # Возвращем средний рейтинг, округляем до трех символов после запятой