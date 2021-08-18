from bs4 import BeautifulSoup
from urllib.request import urlopen
src = urlopen('https://store.steampowered.com/genre/Free%20to%20Play/')  # Открываем ссылку из задачи
soup = BeautifulSoup(src, 'html.parser')  # Создается объект BeautifulSoup. Данные передаются конструктору.
tags_dict = {}
tags = soup.find_all('div', class_='tag_count_button')  # Нижний слэш так как class зарезервирован Python
for elem in tags:
    key = elem.find(class_='tag_name').text  # Получаем название жанра, присваеваем его ключу
    value = elem.find(class_='tag_count').text  # Получаем количество игр, присваеваем его значению
    tags_dict[key] = value  # Заполняем словарь связкой ключ: значение
print(tags_dict)
