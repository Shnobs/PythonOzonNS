from bs4 import BeautifulSoup
from urllib.request import urlopen
src = urlopen('https://store.steampowered.com/genre/Free%20to%20Play/')
soup = BeautifulSoup(src, 'html.parser')
dict_f2p ={}
ahref = soup.find('div', class_="tabarea").find_all('a', class_="tab_item")
for elem in ahref:
    key = elem.find(class_='tab_item_name').text
    value = elem.find(class_='tab_item_top_tags').text
    dict_f2p[key] = value
print(dict_f2p)