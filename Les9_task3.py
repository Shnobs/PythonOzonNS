import re
with open('lesson09_cats_of_ulthar.txt') as book:  # Открываем текстовый файл
    dict_cats = re.findall(r"[Кк]ош\w{1,3}\b", book.read())  # Читаем файл и ищем все совпадения с паттерном, вносим их в список
print(f'Количество кошек в тектсе равно {len(dict_cats)}')  # Считаем длину получившегося списка
