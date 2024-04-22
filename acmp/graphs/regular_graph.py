# по матрице смежности определить регулярный ли граф
# граф назыв. регулярным, если степени его вершин равны

n = int(input())
matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

ans = 'YES'
vertex_degree = sum(matrix[0])
for i in range(1, n):
    cur_vert_degree = 0
    for j in range(0, n):
        if matrix[i][j] == 1:
            cur_vert_degree += 1
    if vertex_degree != cur_vert_degree:
        ans = 'NO'
        break

print(ans)
