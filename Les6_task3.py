import os, pickle  # Импорт библиотек для работы с файлами
for file in os.listdir():  # Цикл по всем файлам в текущей директории
    if file.endswith('.dat'):  # Выборка по файлам с расширением .dat
        with open(file, 'rb') as text:  # Открытие .dat файлов
            print(file, pickle.load(text))  # Загрузка содержимого .dat файла
