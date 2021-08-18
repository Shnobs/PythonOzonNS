import re
galaxy = []  # Создаем пустой список и переменную для цикла
galaxy_andromeda = []
i = 0
with open('lesson09_closest_galaxies.csv', 'r', encoding="utf-8") as file:  # Открываем файл, без кодировки не работает
    for row in file.read().splitlines():  # Проходим файл по строкам, удаляем символ начала строки
        galaxy.append(row.split(','))  # Разбиваем строки по разделютелю в виде запятой, заполняем список
for i in range(len(galaxy)):  # Проходим список по индексам
    if re.search(r'Андромед\w+', galaxy[i][3]):  # and galaxy[i][2] ==:  # Проверяем 4 колонку каждой строки на совпадение
        try:  # Создаем список со словарями по заданным условиям
            galaxy_andromeda.append({'Название': galaxy[i][0], 'Расстояние': float(galaxy[i][2]), 'Примечание': galaxy[i][3]})
        except ValueError:  # Обходим ошибки в исходном csv файле, выводим сообщение
            print(f'Исправьте значение {galaxy[i][2]} в строке номер {i}')
galaxy_andromeda.sort(key=lambda dictionary: dictionary['Расстояние'])  # Сортировка списка по значению ключа по возрастанию
print(galaxy_andromeda)
