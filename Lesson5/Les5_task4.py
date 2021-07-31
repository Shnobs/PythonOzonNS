vopros_date = input('Введите дату про которую хотите добавить запись: ')  # Получвем данные от пользователя
vopros_main = input('Добавьте описание событий: ')
dnevnik = open('dnevnik.txt', 'a+')  # Открываем или создаем дневник для добавления
dnevnik.write(f'Дата события: {vopros_date}. В этот день произошло: {vopros_main}\n')  # Добавлеям строку в дневник
dnevnik = open('dnevnik.txt', 'r')  # Открываем дневник для чтения, без этого команда read не работает
print(dnevnik.read())
dnevnik.close()  # Выводим данные и закрываем файл
