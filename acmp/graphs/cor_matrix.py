# из матрицы смежности в список ребер
# граф - ориентированный без петель

n = int(input())
matrix = []
cor_list = [[] for i in range(n)]

for i in range(n):
    matrix.append(list(map(int, input().split())))


edges = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            edges += 1
            cor_list[i].append(j+1)

print(n, edges)
for i in range(n):
    for j in cor_list[i]:
        print(f'{i+1} {j}')
