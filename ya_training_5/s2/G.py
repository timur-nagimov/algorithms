def ban_race_and_class(n, m, stats):
    # первый максимум
    max_1 = i_1 = j_1 = -1
    for i in range(n):
        for j in range(m):
            if stats[i][j] > max_1:
                max_1 = stats[i][j]
                i_1 = i
                j_1 = j
    # второй максимум без строки макс. элемента
    max_2 = i_2 = j_2 = -1
    for i in range(n):
        if i == i_1:
            continue
        for j in range(m):
            if stats[i][j] > max_2:
                max_2 = stats[i][j]
                i_2 = i
                j_2 = j
    # третий максимум без столбца макс. элемента
    max_3 = i_3 = j_3 = -1
    for i in range(n):
        for j in range(m):
            if j == j_1:
                continue
            if stats[i][j] > max_3:
                max_3 = stats[i][j]
                i_3 = i
                j_3 = j
    # Выбираем что больше: max_2 или max_3
    second_max = second_i = second_j = - 1
    if max_2 < max_3:
        # second_max = max_2
        second_i = i_2
        second_j = j_2
    else:
        # second_max = max_3
        second_i = i_3
        second_j = j_3

    max_2 = i_2 = j_2 = -1
    # максимум, но без i_1 и second_j
    for i in range(n):
        if i == i_1:
            continue
        for j in range(m):
            if j == second_j:
                continue
            if stats[i][j] > max_2:
                max_2 = stats[i][j]
                i_2 = i
                j_2 = j

    # максимум, но без second_i и j_1
    max_3 = i_3 = j_3 = -1
    for i in range(n):
        if i == second_i:
            continue
        for j in range(m):
            if j == j_1:
                continue
            if stats[i][j] > max_3:
                max_3 = stats[i][j]
                i_3 = i
                j_3 = j

    if max_2 > max_3:
        return second_i, j_1
    return i_1, second_j


n, m = map(int, input().split())
stats = []
for i in range(n):
    stats.append(list(map(int, input().split())))


race, klass = ban_race_and_class(n, m, stats)
print(race+1, klass+1)
