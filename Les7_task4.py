import random, time
def selection_sort(input_list):  # Сортировка выбором
    start_time = time.time() # время старта функции
    for i in range(len(input_list)):
        min_i = i
        for j in range(i + 1, len(input_list)):
            if input_list[min_i] > input_list[j]:
                min_i = j
                input_list[i], input_list[min_i] = input_list[min_i], input_list[i]
    return time.time() - start_time # время выполнения в секундах

def insertion_sort(input_list):  # Сортировка вставкой
    start_time = time.time()
    for i in range(1, len(input_list)):
        temp = input_list[i]
        position = i - 1
        while position >= 0 and input_list[position] > temp:
            input_list[position + 1] = input_list[position]
            position -= 1
        input_list[position + 1] = temp
    return time.time() - start_time

list_1000 = [random.randint(1, 1000) for _ in range(1000)]  # Заполнение списков списковым включением
list_2000 = [random.randint(1, 2000) for _ in range(2000)]
list_5000 = [random.randint(1, 5000) for _ in range(5000)]
list_10000 = [random.randint(1, 10000) for _ in range(10000)]
print(f'Sorting by selecting {len(list_1000)} items was completed in {round(selection_sort(list_1000), 3)}')
print(f'Sorting by selecting {len(list_2000)} items was completed in {round(selection_sort(list_2000), 3)}')
print(f'Sorting by selecting {len(list_5000)} items was completed in {round(selection_sort(list_5000), 3)}')
print(f'Sorting by selecting {len(list_10000)} items was completed in {round(selection_sort(list_10000), 3)}')
print(f'Sorting by inserting  {len(list_1000)} items was completed in {round(insertion_sort(list_1000), 3)}')
print(f'Sorting by inserting  {len(list_2000)} items was completed in {round(insertion_sort(list_2000), 3)}')
print(f'Sorting by inserting  {len(list_5000)} items was completed in {round(insertion_sort(list_5000), 3)}')
print(f'Sorting by inserting  {len(list_10000)} items was completed in {round(insertion_sort(list_10000), 3)}')
# Общее время выполнения сортировкой вставкой в 3-4 раза быстреей сортировки выбором
