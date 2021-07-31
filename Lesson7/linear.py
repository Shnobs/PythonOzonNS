array = [1, 2, 4, 7, 44, 443, 88, 235, 239]
#  Линейный поиск
def search(elem, arr):
    for i in range(len(arr)):
        if arr[i] == elem:
            return i
    return - 1

print(search(4, array))
print(search(5, array))

# Бинарный поиск
array_2 = [x for x in range(1, 100, 3)]
def binary_search(elem, arr):
    left = 0
    right = len(arr)
    mid = (left + right) // 2
    while right >= left:
        if arr[mid] == elem:
            return mid
        elif arr[mid] > elem:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return -1
print(binary_search(1, array_2))