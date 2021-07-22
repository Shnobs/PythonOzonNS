# Задаем необходимые переменные
x = list(range(1,11))
y = 1
tablica = []
i = 0 # Индекс элементов списка
while y < 11: # Запускаем цикл
    if i < 10:
        z = y * x[i] # Производим умножение
        tablica.append(f'{y} * {x[i]} = {z}') # Заполняем список таблицой умножения
        i += 1
    else:
        y += 1
        i = 0
for elem in range(len(tablica)): # Построчно выводим таблицу умножения
    print(tablica[elem])