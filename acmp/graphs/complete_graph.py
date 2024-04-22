# по списку смежности проверить является ли граф полным
n, m = map(int, input().split())

matrix = [[0]*n for i in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    matrix[u-1][v-1] = 1
    matrix[v-1][u-1] = 1

ans = 'YES'
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if matrix[i][j] == 0:
            ans = 'NO'
            break

print(ans)
