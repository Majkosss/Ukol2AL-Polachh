array = [10, 20, 48, 52, 75, 60, 12, 8, 6, 1]
print("Základní pole:", array)

def bubble_sort():
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            print(array)
    return array

print(bubble_sort())

import random

array2 = [12, 1, 18, 5, 9, 14, 17, 11, 6, 20]
random.shuffle(array2)

print("Zamíchané pole:", array2)