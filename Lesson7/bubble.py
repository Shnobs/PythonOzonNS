import random

def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

random_list = []
for i in range(10):
    random_list.append(random.randint(1,100))
print(random_list)
bubble_sort(random_list )
print(random_list)
