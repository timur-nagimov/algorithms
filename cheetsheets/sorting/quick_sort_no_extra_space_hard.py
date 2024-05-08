# Для реализации алгоритма быстрой сортировки будем использовать разбиение Хоара, т.е ..
# .. за pivot мы будем брать 0-й элемент, за low - 1-й, а за high - последний
# т.к в Python достаточно 'удобное' сравнение списков по умолчанию, то можно не модифицировать код для списка из неск. элементов ..
# .. ( только развернуть список )

# Сложность по времени в среднем: O(n*log(n))
# Сложность по памяти: O(1), т.е храним только входные данные ( ну и пара переменных, которые не учитываются )

def partition(array, low, high):
    pivot = array[low]  # выбираем 0-й элемент в качестве pivot
    i = low + 1  # сдвигаем левый указатель на следующий элемент
    j = high  # ставим правый указатель на конец массива

    while True:
        # сдвигаем левый указатель до тех пор ..
        while i < high and array[i] < pivot:
            i += 1                           # .. пока не найдем элемент < pivot

        while array[j] > pivot:  # сдвигаем налево пока не найдем elem > pivot
            j -= 1

        if i >= j:  # если левый указатель больше правого - выходим из цикла
            break
        # меняем элементы местами и двигаем указатели
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1
    # меняем pivot и элемент. который > pivot
    array[low], array[j] = array[j], array[low]
    return j


def quick_sort(array, low=None, high=None):
    if (low is None):
        low = 0
    if (high is None):
        high = len(array) - 1
    if (low >= high):  # базовый случай
        return None
    center = partition(array, low, high)
    quick_sort(array, low, center-1)  # рекурсивно перебираем левую часть
    quick_sort(array, center+1, high)  # рекурсивно перебираем правую часть


n = int(input())
array = []
for i in range(n):
    elem = input().split()
    elem[1], elem[2] = int(elem[1]), int(elem[2])
    elem = [-elem[1], elem[2], elem[0]]
    array.append(elem)

quick_sort(array)
for i in array:
    print(i[2])
