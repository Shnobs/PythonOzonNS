from bs4 import BeautifulSoup
from urllib.request import urlopen
src = urlopen('https://store.steampowered.com/genre/Free%20to%20Play/')
soup = BeautifulSoup(src, 'html.parser')
ahref = soup.find_all('a', class_="tab_item")  # Нижний слэш так как class зарезервирован Python
dict_game ={}
for item in ahref:
    item_text = item.text
    item_url = item.get('href')  # Собираем ссылки стоящие за href=
    if 'Free To Play' in item_text:
        dict_game[item_text] = item_url
for key, value in dict_game.items():
    print(f'{key.strip()} : {value}')
