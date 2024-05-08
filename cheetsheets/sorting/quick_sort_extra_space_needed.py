import random


def partition(arr, pivot):
    left = [x for x in arr if x < pivot]
    center = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return left, center, right


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left, center, right = partition(arr, pivot)
    return quicksort(left) + center + quicksort(right)


test_arr = [5, 0, -1, -1, 5, 19, -1]
print(quicksort(test_arr))
