n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# Сначала находим 1D преф.сумму (по строкам)
pref_sums_1D = []
for i in range(n):
    row_1D = [0]*(n+1)
    for j in range(m):
        row_1D[j+1] = row_1D[j] + arr[i][j]
    pref_sums_1D.append(row_1D)


# Теперь находим 2D преф.сумму (по столбцам)
pref_sums_2D = [[0] * (m+1) for _ in range(n+1)]
for i in range(n+1):
    print(' '.join(map(str, pref_sums_2D[i])))

for j in range(1, m+1):
    for i in range(n):
        pref_sums_2D[i+1][j] = pref_sums_2D[i][j] + pref_sums_1D[i][j]

for i in range(n+1):
    print(' '.join(map(str, pref_sums_2D[i])))
