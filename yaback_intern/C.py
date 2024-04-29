from sortedcontainers import SortedList


def solve(N, A, B):
    events = []

    # Собираем события для каждого отрезка
    for i in range(N):
        events.append((0, 'start', A[i]))  # События начала отрезка
        events.append((1, 'end', B[i]))    # События конца отрезка

    # Сортировка событий: первично по x, вторично начало перед концом
    events.sort(key=lambda x: (x[0], x[1] == 'end'))

    active_segments = SortedList()  # Активные отрезки
    max_active = 0

    # Обработка событий
    for x, typ, value in events:
        if typ == 'start':
            active_segments.add(value)
        elif typ == 'end':
            active_segments.remove(value)
        max_active = max(max_active, len(active_segments))

    return max_active


if __name__ == '__main__':
    N = 5
    A = [6, 9, 2, 9, 10]
    B = [8, 11, 5, 12, 13]

    max_intersection = solve(N, A, B)
    print(max_intersection)
