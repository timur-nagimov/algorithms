# по матрице смежности определить
# является ли граф ориентированным и без петель
# граф ориетнированный, если матрица не симметрична

n = int(input())
matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

ans = 'NO'
for i in range(n):
    if matrix[i][i] == 1:
        ans = 'NO'
        break
    for j in range(i+1, n):
        if matrix[i][j] != matrix[j][i]:
            ans = 'YES'


print(ans)
