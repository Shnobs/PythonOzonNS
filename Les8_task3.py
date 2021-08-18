from bs4 import BeautifulSoup
from urllib.request import urlopen
src = urlopen('https://store.steampowered.com/genre/Free%20to%20Play/')  # Открываем ссылку из задачи
soup = BeautifulSoup(src, 'html.parser')  # Создается объект BeautifulSoup. Данные передаются конструктору.
dict_f2p = {}
ahref = soup.find('div', class_="tabarea").find_all('a', class_="tab_item")  # Проворачиваем операцию с двойным поиском
for elem in ahref:
    key = elem.find(class_='tab_item_name').text  # Получаем название игры, присваеваем его ключу
    value = elem.find(class_='tab_item_top_tags').text  # Получаем название жанров, присваеваем его значению
    dict_f2p[key] = value  # Заполняем словарь связкой ключ: значение
print(dict_f2p)
