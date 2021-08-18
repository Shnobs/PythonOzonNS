from bs4 import BeautifulSoup
from urllib.request import urlopen
src = urlopen('https://store.steampowered.com/genre/Free%20to%20Play/')  # Открываем ссылку из задачи
soup = BeautifulSoup(src, 'html.parser')  # Создается объект BeautifulSoup. Данные передаются конструктору.
ahref = soup.find_all('a', class_="tab_item")  # Нижний слэш так как class зарезервирован Python
dict_game = {}
for item in ahref:
    item_text = item.text  # Собираем название и жанры игр
    item_url = item.get('href')  # Собираем ссылки стоящие за href=
    if 'Free To Play' in item_text:  # Находим описание  F2P в тексте
        dict_game[item_text] = item_url  # Заполняем словарь названиями и ссылками
for key, value in dict_game.items():  # Выводим словарь на экран
    print(f'{key.strip()} : {value}')
