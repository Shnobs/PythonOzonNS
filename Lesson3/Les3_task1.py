string1 = 'Съешь ещё этих мягких французских булок ДА выпей же чаю'
spisok = string1.split(' ') # Разбиваем строку по пробелам
print(f'Четвертый элемент списка в верхнем регистре это - {spisok[3].upper()}')
print(f'Седьмой элемент списка в нижнем регистре это - {spisok[6].lower()}')
a = list(spisok[7])
print(f'Третья буква в восьмом элементе списка это - {a[2]}')
for elem in spisok:
    print(f'{spisok.index(elem)}. {elem}') # Построчно выводим готовые речи


