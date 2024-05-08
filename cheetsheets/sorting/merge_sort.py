# Сложность O(n*log(n)) - всегда
# Память O(n) - храним подмассивы

# Устойчивость - да, в случае равенства элементов приоритет отдается тому,
#   который находится в левой части подмассива

def merge_sort(array):
    if len(array) == 1:
        return array

    left = merge_sort(array[:len(array)//2])
    right = merge_sort(array[len(array)//2:])

    result = [0]*len(array)

    l, r, k = 0, 0, 0

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result[k] = left[l]
            l += 1
        else:
            result[k] = right[r]
            r += 1
        k += 1

    # Если один из подмассивов закончился раньше - добавляем оставшиеся элементы
    while l < len(left):
        result[k] = left[l]
        l += 1
        k += 1
    while r < len(right):
        result[k] = right[r]
        r += 1
        k += 1

    return result


test_arr = [5, 0, -1, -1, 5, 19, -1]
print(merge_sort(test_arr))
