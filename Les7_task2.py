random_list = [19, 2, 31, 45, 6, 11, 121, 27]
def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]: # Порядок обработки изменен в обратную сторону заменой знака > на <
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
    return arr
print(random_list)
print(bubble_sort(random_list ))
