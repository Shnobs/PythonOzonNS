kotoschetchik = 0
with open('lesson05_cats_of_ulthar.txt', 'r+') as book:  # Открываем текстовый файл
    for line in book:  # Проходим файл по строкам
        if line.count('кошка ') > 0:  # Ищем строки со словом кошка
            kotoschetchik += line.count('кошка ')   # Добавляем количество слов к счетчику
            print(line)
print(f'Количество слов кошка в тексте равно {kotoschetchik}')
