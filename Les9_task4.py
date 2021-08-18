from bs4 import BeautifulSoup
import re
from urllib.request import urlopen

html = urlopen('https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B1%D1%8C%D1%8E%D0%BB%D0%B0')  # Открываем ссылку из задачи
bs = BeautifulSoup(html, 'html.parser')  # Создается объект BeautifulSoup. Данные передаются конструктору.
content = bs.find('div', id='content')  # Собираем данные с основного div-блока
all_links = content.find_all('a', href=re.compile(r'^http'))  # Находим все, что напоминает ссылку
links_wiki = content.find_all('a', href=re.compile(r'wiki'))  # Находим все, что содекржит wiki в ссылке
diff_set = set(all_links).difference(set(links_wiki))  # С помощью пересечения множеств удаляем все ссылки на wiki
for elem in diff_set:  # Проходим список по элементам, выводим результаты построчно
    print(elem.text, elem.get('href'))  # Получаем текст ссылки и саму гиперссылку

