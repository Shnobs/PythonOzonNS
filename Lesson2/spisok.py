cars = ['volvo', 'bmw', 'citroen',[1,2,3,4]]
print(cars[0].title())
cars.append('audi') # Добавление элемента в конец списка
print(cars[3][2]) # Обращение к внутреннему списку
deleted = cars.pop(3) # Удаление элемента списка
print(cars, deleted)
