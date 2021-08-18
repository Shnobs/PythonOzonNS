from bs4 import BeautifulSoup
from urllib.request import urlopen
src = urlopen('https://store.steampowered.com/genre/Free%20to%20Play/')
soup = BeautifulSoup(src, 'html.parser')
tags_dict = {}
tags = soup.find_all('div', class_ = 'tag_count_button')
for elem in tags:
    key = elem.find(class_='tag_name').text
    value = elem.find(class_='tag_count').text
    tags_dict[key] = value
print(tags_dict)