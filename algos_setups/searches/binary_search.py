arr = [1, 2, 3, 5, 9, 11, 15]

l = 0
r = len(arr) - 1
ans = 0
while l <= r:
    mid = (l+r)//2
    """
    В данном случае функция ok - условие проверки (истинности).
    Она должна вернуть True, если arr[mid] подходит по условию задачи.
    """
    if ok(arr, mid):
        # Теперь надо ответить на вопрос: мы хотим найти `максимальный` или `минимальный` элемент?
        # Максимальный - последний подходящий элемент.
        # Минимальный - первый подходящий элемент.

        # Если хотим минимизировать(найти минимальный) - сдвигаем правую границу.
        # Если хотим максимизировать(найти максимальный) - сдвигаем левую границу.
        r = mid - 1  # минимизация
        # l = mid + 1 - максимизация
        ans = mid
    else:
        # Тут мы должны сдвигать другую границу
        l = mid + 1  # минимизация
        # r = mid - 1 - максимизация
