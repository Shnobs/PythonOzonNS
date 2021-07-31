import random
def insert_sort(arr):
    result = arr.copy()

    for i in range(1, len(result)):
        currentValue = result[i]
        currentPosition = i

        while currentPosition > 0 and result[currentPosition - 1] > currentValue:
            result[currentPosition] = result[currentPosition -1]
            currentPosition = currentPosition - 1

        result[currentPosition] = currentValue

    return result

random_list = []
for i in range(10):
    random_list.append(random.randint(1,100))
print(random_list)
print(insert_sort(random_list ))

